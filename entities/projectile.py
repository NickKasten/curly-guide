"""
Projectile Entity

Projectiles are the bullets/lasers that the player shoots.

They're simple objects that:
- Move in a straight line
- Disappear when they leave the screen
- Destroy enemies on contact

Despite being simple, projectiles are crucial to the gameplay!
"""

import pygame
from config import *


class Projectile(pygame.sprite.Sprite):
    """
    A projectile (bullet) fired by the player.

    Moves in a straight line at constant speed.
    """

    def __init__(self, x, y, velocity_x, velocity_y, color=PROJECTILE_COLOR):
        """
        Initialize a projectile.

        Args:
            x (float): Starting X position
            y (float): Starting Y position
            velocity_x (float): Horizontal speed (pixels per frame)
            velocity_y (float): Vertical speed (pixels per frame, negative = upward)
            color (tuple): RGB color for the projectile
        """
        super().__init__()

        # === VISUAL REPRESENTATION ===
        # Create a simple colored rectangle
        # TODO: You could use a different shape or load an image:
        # - self.image = pygame.image.load("assets/bullet.png")
        # - Or draw a circle: pygame.draw.circle(...)
        self.image = pygame.Surface((PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        self.image.fill(color)

        # For transparency (if you want the bullet to glow or fade)
        # Uncomment this to make bullets semi-transparent:
        # self.image.set_alpha(200)

        # === POSITION ===
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # === VELOCITY ===
        # How fast and in what direction the projectile moves
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self, delta_time):
        """
        Update the projectile's position.

        Args:
            delta_time (float): Time since last frame in seconds

        Projectiles just move in a straight line, so this is simple!
        """
        # Move based on velocity
        # Multiply by delta_time for frame-rate independence
        # Multiply by 60 to match the baseline of 60 FPS
        self.rect.x += self.velocity_x * delta_time * 60
        self.rect.y += self.velocity_y * delta_time * 60

        # The game engine will handle removing projectiles that go off-screen
        # See game_engine.py's cleanup_sprites() method


# =============================================================================
# EXPANSION IDEAS FOR PROJECTILES
# =============================================================================
"""
Projectiles seem simple, but you can make them much more interesting:

1. DIFFERENT PROJECTILE TYPES:
   - Create classes like LaserProjectile, MissileProjectile, etc.
   - Each type has different:
     * Speed
     * Damage
     * Size
     * Visual appearance
     * Behavior (tracking, bouncing, exploding, etc.)

2. HOMING MISSILES:
   - Track the nearest enemy
   - Gradually turn toward it in update()
   - Requires finding enemy position and calculating angle

3. BOUNCING PROJECTILES:
   - Reflect off screen edges instead of disappearing
   - Change velocity_x when hitting left/right edges
   - Change velocity_y when hitting top/bottom edges

4. PIERCING BULLETS:
   - Don't get destroyed on hit
   - Can hit multiple enemies
   - Maybe limit to X enemies before disappearing

5. EXPLOSIVE PROJECTILES:
   - On impact, damage nearby enemies (area of effect)
   - Requires checking distance to all enemies
   - Visual explosion effect

6. SPLIT PROJECTILES:
   - After traveling X distance, split into multiple projectiles
   - Track self.distance_traveled in update()
   - Create new projectiles in different directions

7. PROJECTILE ANIMATIONS:
   - Rotate the sprite as it moves
   - Pulse or glow effect
   - Trail effect (leave particles behind)

8. DIFFERENT PLAYER WEAPONS:
   - Spread shot (3-5 projectiles in a fan pattern)
   - Rapid fire (many small bullets)
   - Charge beam (continuous damage while holding shoot)

IMPLEMENTATION EXAMPLE - Homing Missile:

class HomingMissile(Projectile):
    def __init__(self, x, y, enemy_group):
        super().__init__(x, y, 0, -PROJECTILE_SPEED)
        self.enemy_group = enemy_group
        self.turn_speed = 2  # How fast it can turn

    def update(self, delta_time):
        # Find nearest enemy
        if self.enemy_group:
            nearest = min(self.enemy_group,
                         key=lambda e: ((e.rect.x - self.rect.x)**2 +
                                       (e.rect.y - self.rect.y)**2)**0.5)
            # Calculate angle to enemy and adjust velocity
            # (angle math goes here)

        # Call parent update to move
        super().update(delta_time)

TODO: Try implementing one of these projectile types!
      Start with something simple like bouncing or piercing bullets.
"""
