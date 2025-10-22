"""
Player Entity

This is the player's spaceship - the character the player controls!

The player can:
- Move left and right (and optionally up/down)
- Shoot projectiles
- Take damage and lose lives
- Be temporarily invulnerable after being hit

This is the most important entity in the game - everything revolves around
keeping the player alive and having fun!
"""

import pygame
from config import *
from entities.projectile import Projectile
from services.collision_service import keep_in_bounds


class Player(pygame.sprite.Sprite):
    """
    The player's spaceship.

    Controls: Arrow keys to move, Spacebar to shoot
    """

    def __init__(self, x, y, color=PLAYER_COLOR):
        """
        Initialize the player.

        Args:
            x (float): Starting X position
            y (float): Starting Y position
            color (tuple): RGB color for the player (default from config)
        """
        super().__init__()

        # === VISUAL REPRESENTATION ===
        # Create a simple colored rectangle for the player
        # TODO: Replace this with an actual spaceship image!
        # You can load an image like this:
        # self.image = pygame.image.load("assets/player.png")
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)

        # Store original for flashing effect when hit
        self.original_image = self.image.copy()
        self.color = color

        # === POSITION ===
        # The rect is used for both positioning and collision detection
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # === GAMEPLAY STATS ===
        # How many hits the player can take
        self.lives = PLAYER_STARTING_LIVES
        self.max_lives = PLAYER_STARTING_LIVES

        # === SHOOTING ===
        # Track time since last shot to limit fire rate
        self.shoot_cooldown = 0.0

        # === INVULNERABILITY ===
        # Timer for visual flashing effect
        self.invulnerable_flash_timer = 0.0
        self.is_flashing = False

    def update(self, input_state, delta_time):
        """
        Update the player's state each frame.

        Args:
            input_state (dict): Dictionary of input actions (from InputService)
            delta_time (float): Time since last frame in seconds
        """
        # === MOVEMENT ===
        # Calculate movement based on input
        move_x = 0
        move_y = 0

        if input_state["move_left"]:
            move_x -= PLAYER_SPEED
        if input_state["move_right"]:
            move_x += PLAYER_SPEED

        # Vertical movement (optional - uncomment if you want it)
        # if input_state["move_up"]:
        #     move_y -= PLAYER_SPEED
        # if input_state["move_down"]:
        #     move_y += PLAYER_SPEED

        # Apply movement
        self.rect.x += move_x
        self.rect.y += move_y

        # Keep player on screen
        keep_in_bounds(self.rect, SCREEN_WIDTH, SCREEN_HEIGHT)

        # === SHOOTING COOLDOWN ===
        # Decrease the cooldown timer
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= delta_time

        # === INVULNERABILITY FLASH EFFECT ===
        # This makes the player blink when invulnerable (handled by game engine)
        # Here we just handle the visual flashing
        if self.invulnerable_flash_timer > 0:
            self.invulnerable_flash_timer -= delta_time
            # Flash by alternating between visible and semi-transparent
            # We change the alpha (transparency) every 0.1 seconds
            if int(self.invulnerable_flash_timer * 10) % 2 == 0:
                # Make semi-transparent
                self.image.set_alpha(100)
            else:
                # Make fully visible
                self.image.set_alpha(255)
        else:
            # Normal visibility
            self.image.set_alpha(255)

    def can_shoot(self):
        """
        Check if the player is allowed to shoot right now.

        Returns:
            bool: True if cooldown has expired, False otherwise
        """
        return self.shoot_cooldown <= 0

    def shoot(self):
        """
        Create and return a projectile.

        Returns:
            Projectile: A new projectile sprite, or None if on cooldown

        The game engine will add this to the appropriate sprite groups.
        """
        if not self.can_shoot():
            return None

        # Calculate where the bullet should spawn
        # (at the top center of the player)
        bullet_x = self.rect.centerx
        bullet_y = self.rect.top

        # Create the projectile moving upward (negative Y velocity)
        projectile = Projectile(bullet_x, bullet_y, 0, -PROJECTILE_SPEED)

        # Reset the cooldown
        self.shoot_cooldown = PROJECTILE_COOLDOWN

        # TODO: Play a shooting sound effect here!
        # shoot_sound.play()

        return projectile

    def take_damage(self):
        """
        Reduce the player's lives by one.

        Called when the player is hit by an enemy.
        Also triggers the invulnerability flash effect.
        """
        self.lives -= 1

        # Start the flashing effect
        self.invulnerable_flash_timer = PLAYER_INVULNERABILITY_TIME

        # TODO: Play a damage sound effect here!
        # hit_sound.play()

        # TODO: You could add a visual explosion effect here
        # Or make the player shake briefly

        # Check if player is out of lives
        if self.lives <= 0:
            # TODO: Play game over sound or trigger game over animation
            pass

    def heal(self, amount=1):
        """
        Restore lives to the player.

        Args:
            amount (int): Number of lives to restore

        This would be called if you add health pickups!
        """
        self.lives = min(self.lives + amount, self.max_lives)
        # Don't go over the maximum

        # TODO: Play a healing sound effect!
        # heal_sound.play()


# =============================================================================
# EXPANSION IDEAS FOR THE PLAYER
# =============================================================================
"""
Here are some cool features you could add to make the player more interesting:

1. POWER-UPS:
   - self.power_level = 1
   - Higher levels = shoot multiple bullets, faster bullets, etc.
   - Add a power_up() method

2. SPECIAL WEAPONS:
   - self.weapon_type = "laser" or "spread" or "missile"
   - Different shoot() behavior based on weapon
   - Timed power-ups that revert after X seconds

3. SHIELD/ARMOR:
   - self.shield = 0
   - Take damage from shield first, then lives
   - Draw a shield visual around the player

4. CHARGE SHOT:
   - Hold shoot button to charge
   - Release for a more powerful shot
   - Track self.charge_level in update()

5. DASH/DODGE:
   - Quick movement burst in a direction
   - Makes player invulnerable briefly
   - Add a dash_cooldown timer

6. ANIMATIONS:
   - Different images for: idle, moving left, moving right, shooting
   - Animate engine thrust, weapon firing, etc.
   - Use self.animation_frame and self.animation_timer

7. SCORE MULTIPLIER:
   - self.multiplier = 1.0
   - Increases with consecutive hits
   - Resets when player takes damage

8. ENERGY SYSTEM:
   - self.energy = 100
   - Shooting costs energy
   - Regenerates over time
   - Can't shoot when empty

TODO: Pick one of these ideas and try implementing it!
     Start with something simple like a shield or power-up system.
"""
