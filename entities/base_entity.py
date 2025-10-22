"""
Base Entity Class

This is a base class that other game objects can inherit from.
It provides common functionality that all game entities need.

Inheritance is a key OOP concept - instead of copying code into
every entity class, we write it once here and let others inherit it!

You don't HAVE to use this class (you can make entities directly from pygame.sprite.Sprite),
but it's here to show you how inheritance works and to provide some helpful utilities.
"""

import pygame


class BaseEntity(pygame.sprite.Sprite):
    """
    Base class for all game entities.

    Inherits from pygame.sprite.Sprite to get all the sprite functionality,
    then adds some common features that our specific entities might need.
    """

    def __init__(self, x, y, width, height, color):
        """
        Initialize a basic entity.

        Args:
            x (float): Starting X position
            y (float): Starting Y position
            width (int): Width in pixels
            height (int): Height in pixels
            color (tuple): RGB color tuple (e.g., (255, 0, 0) for red)
        """
        # Call the parent class (Sprite) constructor
        # This is REQUIRED when using inheritance
        super().__init__()

        # Create the visual representation (a colored rectangle for now)
        # In a more advanced game, you'd load an image here instead
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Store the original image for rotation/scaling without quality loss
        self.original_image = self.image.copy()

        # Get the rect (rectangle) for position and collision detection
        # The rect has properties like: x, y, centerx, centery, top, bottom, left, right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Store dimensions for reference
        self.width = width
        self.height = height
        self.color = color

        # Velocity (speed and direction of movement)
        # Positive x = moving right, negative x = moving left
        # Positive y = moving down, negative y = moving up
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self, delta_time):
        """
        Update the entity's state.

        This is called every frame. Override this in child classes
        to add specific behavior.

        Args:
            delta_time (float): Time since last frame in seconds
        """
        # Move based on velocity
        # Multiply by delta_time for frame-rate independent movement
        self.rect.x += self.velocity_x * delta_time * 60  # *60 to match 60 FPS baseline
        self.rect.y += self.velocity_y * delta_time * 60

    def set_position(self, x, y):
        """
        Set the entity's position.

        Args:
            x (float): New X position
            y (float): New Y position
        """
        self.rect.x = x
        self.rect.y = y

    def get_position(self):
        """
        Get the entity's current position.

        Returns:
            tuple: (x, y) position
        """
        return (self.rect.x, self.rect.y)

    def set_velocity(self, vx, vy):
        """
        Set the entity's velocity.

        Args:
            vx (float): Velocity in X direction (horizontal)
            vy (float): Velocity in Y direction (vertical)
        """
        self.velocity_x = vx
        self.velocity_y = vy

    def get_velocity(self):
        """
        Get the entity's current velocity.

        Returns:
            tuple: (vx, vy) velocity
        """
        return (self.velocity_x, self.velocity_y)


# =============================================================================
# WHY USE A BASE CLASS?
# =============================================================================
"""
You might be wondering: "Why bother with a base class? Can't I just make
Player, Enemy, and Projectile directly from pygame.sprite.Sprite?"

Yes, you could! But using a base class has benefits:

1. DON'T REPEAT YOURSELF (DRY):
   - If Player, Enemy, and Projectile all need velocity, write it once here
   - Changes to common functionality only need to happen in one place

2. CONSISTENCY:
   - All entities work the same way for common operations
   - Makes the code more predictable and easier to understand

3. EASY EXTENSION:
   - Want to add health to ALL entities? Add it to BaseEntity!
   - Want ALL entities to flash when hit? Add it here!

4. LEARNING OOP:
   - Great practice for understanding inheritance
   - Common pattern in professional game development

WHEN NOT TO USE:
- If entities are very different and share little code, skip the base class
- For this simple game, you could honestly skip it and just use pygame.sprite.Sprite
- It's here mainly as a learning tool and for future expansion!

TODO: Try adding a new method here (like draw_outline() or flash()) and use it
      in multiple entity types to see how inheritance saves you work!
"""
