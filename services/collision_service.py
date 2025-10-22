"""
Collision Detection Service

This module handles detecting when objects in the game collide (bump into each other).

Collisions are crucial in games! They determine when:
- A player's bullet hits an enemy
- An enemy crashes into the player
- The player picks up a power-up
- And much more!

Pygame makes this easy with built-in rectangle collision detection.
"""

import pygame

def check_collision(rect1, rect2):
    """
    Check if two rectangles are overlapping (colliding).

    Args:
        rect1 (pygame.Rect): First rectangle
        rect2 (pygame.Rect): Second rectangle

    Returns:
        bool: True if the rectangles overlap, False otherwise

    Pygame's Rect.colliderect() method does the heavy lifting for us.
    It checks if ANY part of rect1 touches ANY part of rect2.

    Example:
        player_rect = pygame.Rect(100, 100, 30, 40)
        enemy_rect = pygame.Rect(105, 110, 25, 25)
        if check_collision(player_rect, enemy_rect):
            print("Hit!")
    """
    return rect1.colliderect(rect2)


def check_collision_with_group(rect, sprite_group):
    """
    Check if a rectangle collides with any sprite in a group.

    Args:
        rect (pygame.Rect): The rectangle to check
        sprite_group (pygame.sprite.Group): A group of sprites to check against

    Returns:
        list: A list of sprites that collided with the rect (empty if none)

    This is useful for checking things like:
    - "Did this bullet hit ANY enemy?"
    - "Did the player touch ANY power-up?"

    Example:
        bullet_rect = my_bullet.rect
        hit_enemies = check_collision_with_group(bullet_rect, all_enemies)
        for enemy in hit_enemies:
            enemy.take_damage()
    """
    # pygame.sprite.spritecollide() is a built-in function that does this efficiently
    # The False parameter means "don't remove the sprites from the group"
    collided_sprites = pygame.sprite.spritecollide(
        # We need a sprite, not just a rect, so we create a dummy sprite
        # This is a little hack - you could also pass a real sprite object
        type('DummySprite', (), {'rect': rect})(),
        sprite_group,
        False
    )
    return collided_sprites


def check_group_collision(group1, group2, destroy_first=False, destroy_second=False):
    """
    Check for collisions between two groups of sprites.

    Args:
        group1 (pygame.sprite.Group): First group of sprites
        group2 (pygame.sprite.Group): Second group of sprites
        destroy_first (bool): If True, remove sprites from group1 when they collide
        destroy_second (bool): If True, remove sprites from group2 when they collide

    Returns:
        dict: A dictionary where keys are sprites from group1 and values are
              lists of sprites from group2 that collided with them

    This is perfect for things like:
    - Bullets (group1) hitting enemies (group2)
    - Enemies (group1) hitting players (group2)

    Example:
        # Check which bullets hit which enemies, and destroy both
        collisions = check_group_collision(bullets, enemies, True, True)
        for bullet, hit_enemies in collisions.items():
            for enemy in hit_enemies:
                score += 10  # Add points for each hit
    """
    return pygame.sprite.groupcollide(group1, group2, destroy_first, destroy_second)


def check_out_of_bounds(rect, screen_width, screen_height, margin=0):
    """
    Check if a rectangle has left the screen boundaries.

    Args:
        rect (pygame.Rect): The rectangle to check
        screen_width (int): Width of the game screen
        screen_height (int): Height of the game screen
        margin (int): How far outside the screen to allow before considering it out of bounds
                      (useful for letting things go slightly offscreen before removing them)

    Returns:
        bool: True if the rectangle is out of bounds, False if still on screen

    This is useful for cleaning up objects that have left the screen:
    - Bullets that flew off the top
    - Enemies that made it past the player
    - Anything that went too far left/right

    Example:
        if check_out_of_bounds(bullet.rect, SCREEN_WIDTH, SCREEN_HEIGHT, margin=50):
            bullet.kill()  # Remove the bullet from the game
    """
    # Check all four sides with the margin
    if rect.right < -margin:  # Left side
        return True
    if rect.left > screen_width + margin:  # Right side
        return True
    if rect.bottom < -margin:  # Top side
        return True
    if rect.top > screen_height + margin:  # Bottom side
        return True

    return False


def keep_in_bounds(rect, screen_width, screen_height):
    """
    Clamp a rectangle to stay within the screen boundaries.

    Args:
        rect (pygame.Rect): The rectangle to clamp
        screen_width (int): Width of the game screen
        screen_height (int): Height of the game screen

    This modifies the rect in-place to keep it on screen.
    Perfect for keeping the player from moving off the edges!

    Example:
        # Update player position
        player.rect.x += movement
        # Make sure they don't go off screen
        keep_in_bounds(player.rect, SCREEN_WIDTH, SCREEN_HEIGHT)
    """
    # Clamp horizontal position
    if rect.left < 0:
        rect.left = 0
    if rect.right > screen_width:
        rect.right = screen_width

    # Clamp vertical position
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > screen_height:
        rect.bottom = screen_height


# =============================================================================
# ADVANCED COLLISION CONCEPTS (for later!)
# =============================================================================
"""
The functions above use "bounding box" collision detection - treating everything
as rectangles. This is fast and works well for most games!

If you want more precise collisions later, here are some concepts to explore:

1. CIRCLE COLLISION: Better for round objects
   - Check if distance between centers < sum of radii
   - More realistic for spherical enemies or power-ups

2. PIXEL-PERFECT COLLISION: Ultra-precise
   - pygame.sprite.collide_mask() checks actual pixel overlap
   - Slower but perfect for complex shapes
   - Good for polish in later stages

3. COLLISION LAYERS: Organize what can hit what
   - Enemies can't hit enemies
   - Player bullets don't hit player
   - Use different groups for different types

4. COLLISION CALLBACKS: Execute code when things collide
   - on_hit() methods in sprite classes
   - Trigger animations, sounds, effects

TODO: When you're comfortable with basic collisions, try implementing
      one of these advanced techniques!
"""
