"""
Input Service

This module handles all keyboard input for the game.
Instead of checking for keys all over the code, we do it once here
and return a clean dictionary of what's currently pressed.

This makes it easy to:
1. Add new controls without changing game logic
2. Switch to gamepad/joystick input later
3. Add Player 2 controls for multiplayer
"""

import pygame

class InputService:
    """
    Manages keyboard input state for the game.

    This class checks which keys are currently pressed and returns
    that information in an easy-to-use format.
    """

    def __init__(self):
        """
        Initialize the input service.

        Currently doesn't need any setup, but having __init__ here
        makes it easy to add configuration later (like custom key bindings).
        """
        # TODO: You could add custom key mapping here, loaded from a config file
        # For example: self.key_map = {"move_left": pygame.K_LEFT, ...}
        pass

    def get_input_state(self):
        """
        Check which keys are currently pressed and return the input state.

        Returns:
            dict: A dictionary with boolean values for each action
                  For example: {"move_left": True, "shoot": False, ...}

        This is called every frame by the game loop to see what the player is doing.
        """
        # Get the current state of ALL keys on the keyboard
        # This returns an array where each index represents a key
        # True = pressed, False = not pressed
        keys = pygame.key.get_pressed()

        # Build a dictionary of meaningful actions from the raw key state
        # This is much easier to work with than checking individual keys!
        input_state = {
            # Movement controls - arrow keys
            "move_left": keys[pygame.K_LEFT],
            "move_right": keys[pygame.K_RIGHT],
            "move_up": keys[pygame.K_UP],     # Not used in basic version, but here for expansion
            "move_down": keys[pygame.K_DOWN],  # Not used in basic version, but here for expansion

            # Shooting control - spacebar
            "shoot": keys[pygame.K_SPACE],

            # Alternative movement - WASD keys (common in PC games)
            # TODO: These are here for when you add Player 2!
            # Player 1 could use arrows, Player 2 could use WASD
            "move_left_alt": keys[pygame.K_a],
            "move_right_alt": keys[pygame.K_d],
            "move_up_alt": keys[pygame.K_w],
            "move_down_alt": keys[pygame.K_s],

            # Alternative shoot button for Player 2
            "shoot_alt": keys[pygame.K_LSHIFT],  # Left Shift key
        }

        return input_state

    def is_key_pressed(self, key):
        """
        Check if a specific Pygame key is currently pressed.

        Args:
            key: A Pygame key constant (like pygame.K_SPACE)

        Returns:
            bool: True if the key is pressed, False otherwise

        This is a simpler helper method for checking individual keys.
        Useful for menu navigation or special actions.
        """
        keys = pygame.key.get_pressed()
        return keys[key]


# =============================================================================
# MULTIPLAYER EXTENSION HINTS
# =============================================================================
"""
When you're ready to add 2-player mode, here's what you could do:

1. Create a get_input_state_player2() method that checks WASD keys:
   - W = move up
   - S = move down
   - A = move left
   - D = move right
   - Left Shift = shoot

2. Or, make get_input_state() return TWO dictionaries:
   player1_input, player2_input = input_service.get_input_state()

3. Make sure the game_engine.py can handle two players
   (check docs/multiplayer-extension.md for more details!)

4. Test with a friend! Two-player mode is more fun to test together.
"""
