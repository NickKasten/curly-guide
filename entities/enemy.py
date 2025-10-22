"""
Enemy Entity

Enemies are the asteroids/ships that fall from the top of the screen.

The player must avoid or destroy them to survive and score points!

Enemies:
- Spawn at the top and move downward
- Have random sizes and speeds
- Are destroyed when hit by projectiles
- Damage the player on contact
"""

import pygame
import random
from config import *


class Enemy(pygame.sprite.Sprite):
    """
    An enemy asteroid or ship.

    Falls from the top of the screen at a constant speed.
    """

    def __init__(self, x, y, speed, size, color=ENEMY_COLOR):
        """
        Initialize an enemy.

        Args:
            x (float): Starting X position
            y (float): Starting Y position
            speed (float): How fast the enemy moves downward (pixels per frame)
            size (int): Width and height of the enemy (it's square)
            color (tuple): RGB color for the enemy
        """
        super().__init__()

        # === VISUAL REPRESENTATION ===
        # Create a simple colored square
        # TODO: Replace with an actual asteroid/enemy sprite image!
        # self.image = pygame.image.load("assets/asteroid.png")
        # self.image = pygame.transform.scale(self.image, (size, size))
        self.image = pygame.Surface((size, size))
        self.image.fill(color)

        # Store the original image for rotation effects
        self.original_image = self.image.copy()

        # === POSITION ===
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # === MOVEMENT ===
        self.speed = speed
        # Enemies only move downward in the basic version
        # But you could add horizontal movement for variety!

        # === VISUAL EFFECTS ===
        # Random rotation for visual variety
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-2, 2)  # Degrees per frame

        # === SIZE AND DIFFICULTY ===
        self.size = size
        # Larger enemies could give more points or take multiple hits!

    def update(self, delta_time):
        """
        Update the enemy's state each frame.

        Args:
            delta_time (float): Time since last frame in seconds
        """
        # === MOVEMENT ===
        # Move downward at the enemy's speed
        # Multiply by delta_time for frame-rate independence
        self.rect.y += self.speed * delta_time * 60  # *60 for 60 FPS baseline

        # === ROTATION EFFECT ===
        # Rotate the sprite for a more dynamic look
        self.rotation += self.rotation_speed
        # Create a rotated version of the original image
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        # Update the rect to match the new rotated size
        # (rotation can change the size of the bounding box)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center  # Keep it centered on the same spot

        # The game engine will remove enemies that go off the bottom of the screen


# =============================================================================
# EXPANSION IDEAS FOR ENEMIES
# =============================================================================
"""
There are SO many ways to make enemies more interesting:

1. DIFFERENT ENEMY TYPES:
   class FastEnemy(Enemy):
       # Small, fast, worth fewer points
   class TankEnemy(Enemy):
       # Slow, takes multiple hits, worth more points
   class BossEnemy(Enemy):
       # Huge, complex patterns, lots of health

2. MOVEMENT PATTERNS:
   - Zigzag: self.rect.x += sin(self.rect.y) * speed
   - Circular: Move in circles or spirals
   - Targeting: Move toward the player
   - Swooping: Dive down, then back up

3. ENEMY SHOOTING:
   - Enemies shoot back at the player!
   - Create enemy_projectiles group
   - Track shooting cooldown like player

4. HEALTH SYSTEM:
   - self.health = 3
   - Take multiple hits to destroy
   - Change color/sprite as health decreases

5. SPECIAL ABILITIES:
   - Splitting: Break into 2-3 smaller enemies when destroyed
   - Shielded: Immune to damage from certain directions
   - Kamikaze: Speed up when near player

6. SPAWN PATTERNS:
   - Waves: Spawn groups in formation
   - Swarms: Many small enemies at once
   - Mixed: Different types together

7. DROP ITEMS:
   - When destroyed, chance to drop:
     * Health pickups
     * Power-ups
     * Score multipliers
     * Weapon upgrades

8. VISUAL VARIETY:
   - Different colors for different types
   - Animated sprites
   - Particle trails
   - Glowing effects

IMPLEMENTATION EXAMPLE - Zigzag Enemy:

class ZigzagEnemy(Enemy):
    def __init__(self, x, y, speed, size):
        super().__init__(x, y, speed, size)
        self.zigzag_speed = 2
        self.zigzag_offset = 0

    def update(self, delta_time):
        # Normal downward movement
        super().update(delta_time)

        # Add horizontal zigzag
        self.zigzag_offset += self.zigzag_speed
        self.rect.x += sin(self.zigzag_offset * 0.1) * 3

IMPLEMENTATION EXAMPLE - Enemy with Health:

class TankEnemy(Enemy):
    def __init__(self, x, y, speed, size):
        super().__init__(x, y, speed, size)
        self.health = 3
        self.max_health = 3

    def take_damage(self):
        self.health -= 1
        # Change color based on health
        health_ratio = self.health / self.max_health
        red = 200
        green = int(50 + 150 * health_ratio)
        self.image.fill((red, green, 50))

        if self.health <= 0:
            self.kill()  # Destroy the enemy

NOTE: If you add health to enemies, you'll need to modify the collision
      detection in game_engine.py to call enemy.take_damage() instead
      of directly destroying enemies!

TODO: Try creating a new enemy type with different behavior!
      Start with something simple like a different color/size combination.
"""
