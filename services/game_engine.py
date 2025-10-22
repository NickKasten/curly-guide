"""
Game Engine

This is the "brain" of the game! It coordinates everything:
- Creating and updating all game objects (player, enemies, bullets)
- Checking for collisions
- Updating the score
- Spawning new enemies
- Determining when the game is over

The main.py file calls the engine's update() and render() methods every frame.
Everything else happens automatically!

Think of this like a conductor leading an orchestra - each instrument (player, enemies, etc.)
knows its own part, but the conductor makes sure they all play together in harmony.
"""

import pygame
import random
from config import *
from entities.player import Player
from entities.enemy import Enemy
from entities.projectile import Projectile
from services.collision_service import check_group_collision, check_out_of_bounds
from services.score_service import ScoreService
from ui.hud import HUD


class GameEngine:
    """
    The main game engine that manages all game logic and state.

    This class ties together all the pieces of the game and makes them work as one.
    """

    def __init__(self):
        """
        Initialize the game engine.

        Sets up all the sprite groups, creates the player, and
        initializes the game systems.
        """

        # === SPRITE GROUPS ===
        # Sprite groups are like containers for game objects
        # They make it easy to update and draw many objects at once
        # and to check collisions between groups

        # All sprites in the game (for easy drawing)
        self.all_sprites = pygame.sprite.Group()

        # Player's projectiles (bullets)
        self.player_projectiles = pygame.sprite.Group()

        # Enemy sprites
        self.enemies = pygame.sprite.Group()

        # === GAME SYSTEMS ===
        # Create instances of our service classes
        self.score_service = ScoreService()
        self.hud = HUD()

        # === PLAYER ===
        # Create the player at the starting position
        # We calculate the actual pixel position from the ratios in config.py
        start_x = SCREEN_WIDTH * PLAYER_START_X_RATIO
        start_y = SCREEN_HEIGHT * PLAYER_START_Y_RATIO
        self.player = Player(start_x, start_y)
        self.all_sprites.add(self.player)

        # === GAME STATE VARIABLES ===
        # Track when to spawn the next enemy
        self.enemy_spawn_timer = 0.0
        self.current_spawn_rate = ENEMY_SPAWN_RATE

        # Track difficulty progression
        self.next_difficulty_score = DIFFICULTY_INCREASE_INTERVAL

        # Track current enemy speed for difficulty scaling
        self.current_enemy_speed_min = ENEMY_SPEED_MIN
        self.current_enemy_speed_max = ENEMY_SPEED_MAX

        # Invulnerability timer for the player
        self.player_invulnerable_timer = 0.0

        # Track delta time (time since last frame)
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0

    def reset(self):
        """
        Reset the game to initial state.

        Called when starting a new game after a game over.
        Clears all sprites, resets score, and recreates the player.
        """
        # Clear all sprite groups
        self.all_sprites.empty()
        self.player_projectiles.empty()
        self.enemies.empty()

        # Reset score
        self.score_service.reset_score()

        # Recreate the player
        start_x = SCREEN_WIDTH * PLAYER_START_X_RATIO
        start_y = SCREEN_HEIGHT * PLAYER_START_Y_RATIO
        self.player = Player(start_x, start_y)
        self.all_sprites.add(self.player)

        # Reset difficulty
        self.enemy_spawn_timer = 0.0
        self.current_spawn_rate = ENEMY_SPAWN_RATE
        self.current_enemy_speed_min = ENEMY_SPEED_MIN
        self.current_enemy_speed_max = ENEMY_SPEED_MAX
        self.next_difficulty_score = DIFFICULTY_INCREASE_INTERVAL

        # Reset invulnerability
        self.player_invulnerable_timer = 0.0

    def update(self, input_state):
        """
        Update the game state for one frame.

        This is called every frame by the main game loop.
        It updates all game objects and checks for collisions.

        Args:
            input_state (dict): Dictionary of input actions from InputService
        """
        # Calculate delta time (time since last frame in seconds)
        # This makes movement frame-rate independent
        self.delta_time = self.clock.tick(FPS) / 1000.0

        # === UPDATE PLAYER ===
        self.player.update(input_state, self.delta_time)

        # Check if player wants to shoot
        if input_state["shoot"] and self.player.can_shoot():
            projectile = self.player.shoot()
            if projectile:
                self.player_projectiles.add(projectile)
                self.all_sprites.add(projectile)

        # === UPDATE ALL SPRITES ===
        # This calls the update() method on every sprite in the group
        self.all_sprites.update(self.delta_time)

        # === SPAWN ENEMIES ===
        self.enemy_spawn_timer += self.delta_time
        if self.enemy_spawn_timer >= self.current_spawn_rate:
            self.spawn_enemy()
            self.enemy_spawn_timer = 0.0

        # === CHECK COLLISIONS ===
        self.check_collisions()

        # === CLEAN UP OFF-SCREEN OBJECTS ===
        self.cleanup_sprites()

        # === UPDATE DIFFICULTY ===
        self.update_difficulty()

        # === UPDATE INVULNERABILITY TIMER ===
        if self.player_invulnerable_timer > 0:
            self.player_invulnerable_timer -= self.delta_time

    def render(self, screen):
        """
        Draw all game objects to the screen.

        Args:
            screen (pygame.Surface): The screen surface to draw on
        """
        # Draw all sprites
        # This calls the draw() method (which Pygame provides automatically)
        # on every sprite in the group
        self.all_sprites.draw(screen)

        # Draw the HUD (score, lives, etc.) on top of everything
        self.hud.draw(screen, self.score_service.get_current_score(), self.player.lives)

        # Visual feedback for invulnerability
        # TODO: You could make the player flash or add a shield graphic here
        if self.player_invulnerable_timer > 0:
            # For now, we'll just let the player sprite handle its own flashing
            pass

    def spawn_enemy(self):
        """
        Create a new enemy at a random position at the top of the screen.

        Enemies spawn just above the visible area and move downward.
        Their speed varies based on the current difficulty.
        """
        # Random X position across the width of the screen
        # We add some margin so enemies don't spawn right at the edge
        margin = ENEMY_SIZE_MAX
        x = random.randint(margin, SCREEN_WIDTH - margin)

        # Spawn just above the screen so they "fall" into view
        y = -ENEMY_SIZE_MAX

        # Random speed within the current difficulty range
        speed = random.uniform(self.current_enemy_speed_min, self.current_enemy_speed_max)

        # Random size
        size = random.randint(ENEMY_SIZE_MIN, ENEMY_SIZE_MAX)

        # Create the enemy
        enemy = Enemy(x, y, speed, size)

        # Add to groups
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def check_collisions(self):
        """
        Check for all types of collisions and handle them.

        This includes:
        - Player projectiles hitting enemies
        - Enemies hitting the player
        """
        # === PROJECTILES HIT ENEMIES ===
        # Check which projectiles hit which enemies
        # Both sprites are destroyed on collision (True, True)
        hits = check_group_collision(self.player_projectiles, self.enemies, True, True)

        # Award points for each destroyed enemy
        for projectile, hit_enemies in hits.items():
            for enemy in hit_enemies:
                self.score_service.add_points(ENEMY_POINTS)
                # TODO: Add explosion effect or sound here!

        # === ENEMIES HIT PLAYER ===
        # Only check if player is not invulnerable
        if self.player_invulnerable_timer <= 0:
            # Check if any enemy hit the player
            # Don't destroy the enemy (False) so the player can see what hit them
            player_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)

            if player_hits:
                # Player was hit!
                self.player.take_damage()
                # Make player temporarily invulnerable
                self.player_invulnerable_timer = PLAYER_INVULNERABILITY_TIME
                # Destroy the enemy that hit the player
                for enemy in player_hits:
                    enemy.kill()
                # TODO: Add damage sound/effect here!

    def cleanup_sprites(self):
        """
        Remove sprites that have left the screen.

        This prevents memory leaks and keeps the game running smoothly.
        We give a margin so things can go slightly offscreen before removal.
        """
        margin = 100  # Pixels beyond screen edge before removal

        # Check projectiles
        for projectile in self.player_projectiles:
            if check_out_of_bounds(projectile.rect, SCREEN_WIDTH, SCREEN_HEIGHT, margin):
                projectile.kill()  # Remove from all groups

        # Check enemies (that made it past the player)
        for enemy in self.enemies:
            if check_out_of_bounds(enemy.rect, SCREEN_WIDTH, SCREEN_HEIGHT, margin):
                enemy.kill()
                # TODO: You could subtract points or a life here
                # as penalty for letting enemies through

    def update_difficulty(self):
        """
        Gradually increase the difficulty as the player's score increases.

        Makes the game more challenging and engaging over time!
        """
        current_score = self.score_service.get_current_score()

        # Check if we've reached the next difficulty threshold
        if current_score >= self.next_difficulty_score:
            # Increase spawn rate (enemies appear more frequently)
            self.current_spawn_rate *= SPAWN_RATE_MULTIPLIER

            # Increase enemy speed
            self.current_enemy_speed_min *= ENEMY_SPEED_MULTIPLIER
            self.current_enemy_speed_max *= ENEMY_SPEED_MULTIPLIER

            # Set the next threshold
            self.next_difficulty_score += DIFFICULTY_INCREASE_INTERVAL

            # TODO: You could show a message: "LEVEL UP!" or "DIFFICULTY INCREASED!"
            print(f"Difficulty increased! Spawn rate: {self.current_spawn_rate:.2f}")

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            bool: True if the player has no lives left, False otherwise
        """
        is_over = self.player.lives <= 0

        # If game just ended, save the high score
        if is_over:
            self.score_service.save_high_score()

        return is_over

    def get_score(self):
        """
        Get the current score (convenience method).

        Returns:
            int: The current score
        """
        return self.score_service.get_current_score()


# =============================================================================
# MULTIPLAYER EXTENSION HINTS
# =============================================================================
"""
To add 2-player local multiplayer, you'll need to modify this class:

1. ADD A SECOND PLAYER:
   - self.player2 = Player(start_x, start_y, PLAYER2_COLOR)
   - Give player2 a different starting position (top of screen?)
   - self.player2_projectiles = pygame.sprite.Group()

2. UPDATE BOTH PLAYERS:
   - Get separate input for each: input1, input2 = input_service.get_both_inputs()
   - Update both: self.player.update(input1, ...) and self.player2.update(input2, ...)

3. HANDLE TWO SETS OF PROJECTILES:
   - Check both players' shooting
   - Check both projectile groups for enemy hits

4. GAME OVER CONDITION:
   - Does game end when ONE player dies or BOTH players die?
   - If both must die: return self.player.lives <= 0 and self.player2.lives <= 0

5. COOPERATIVE SCORING:
   - Should players share a score or have separate scores?
   - For shared: one score_service
   - For separate: score_service1 and score_service2

See docs/multiplayer-extension.md for a more detailed guide!
"""
