"""
Entities Package

This folder contains all the game objects (sprites) that appear on screen:
- base_entity.py: Base class that all other entities inherit from
- player.py: The player's spaceship
- enemy.py: Asteroids/enemies that fall from the top
- projectile.py: Bullets that the player shoots

Each entity is a Pygame sprite, which means it:
- Has a rect (rectangle) for position and collision detection
- Has an image (or surface) for drawing
- Can be added to sprite groups for easy management
- Has an update() method called every frame

This is object-oriented programming (OOP) in action!
"""
