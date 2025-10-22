"""
Space Defender - Main Entry Point

This is the heart of the game! When you run `python3 main.py`, this file:
1. Initializes Pygame and creates the game window
2. Sets up all the game systems (score tracking, input handling, etc.)
3. Runs the main game loop that keeps everything moving
4. Handles cleanup when you close the window

As a beginner, start by reading through the comments here to understand
the flow, then explore the other files to see how each piece works.
"""

import pygame
import sys
from config import *
from services.game_engine import GameEngine
from services.input_service import InputService
from ui.menu import Menu

def main():
    """
    Main function that sets up and runs the entire game.

    Think of this as the "director" of your game - it sets up the stage,
    tells everyone when to act, and keeps things running smoothly.
    """

    # Initialize Pygame - this MUST happen before using any Pygame features
    # It sets up all the systems Pygame needs (graphics, sound, input, etc.)
    pygame.init()

    # Create the game window
    # SCREEN_WIDTH and SCREEN_HEIGHT are defined in config.py
    # pygame.RESIZABLE lets users resize the window (you can remove this if you want a fixed size)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the window title that appears in the title bar
    pygame.display.set_caption(GAME_TITLE)

    # Create a clock object to control the frame rate
    # This ensures the game runs at the same speed on different computers
    clock = pygame.time.Clock()

    # Initialize our custom game systems
    # These are defined in the services/ folder - check them out to learn more!
    input_service = InputService()
    game_engine = GameEngine()
    menu = Menu()

    # Track what "state" the game is in
    # The game can be in different states: MENU, PLAYING, PAUSED, or GAME_OVER
    # We start in the MENU state
    game_state = GameState.MENU

    # This is the GAME LOOP - the heart of any game!
    # It runs over and over, many times per second, until you quit
    # Each time through the loop is called a "frame"
    running = True
    while running:
        # STEP 1: Handle Events
        # Events are things that happen: mouse clicks, key presses, window closing, etc.
        # We need to check for these every frame
        for event in pygame.event.get():
            # Check if the user clicked the X button to close the window
            if event.type == pygame.QUIT:
                running = False

            # Check for key presses
            # TODO: You could add other event types here, like mouse clicks for UI buttons
            if event.type == pygame.KEYDOWN:
                # ESC key toggles between PLAYING and PAUSED states
                if event.key == pygame.K_ESCAPE:
                    if game_state == GameState.PLAYING:
                        game_state = GameState.PAUSED
                    elif game_state == GameState.PAUSED:
                        game_state = GameState.PLAYING

                # SPACE or RETURN key in MENU state starts the game
                if game_state == GameState.MENU:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        game_state = GameState.PLAYING
                        game_engine.reset()  # Start fresh when beginning a new game

                # SPACE or RETURN in GAME_OVER state returns to menu
                if game_state == GameState.GAME_OVER:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        game_state = GameState.MENU

        # STEP 2: Update Game State
        # This is where all the game logic happens: moving objects, checking collisions, etc.
        # We only update when actually playing - not in menus or when paused
        if game_state == GameState.PLAYING:
            # Get the current input state (which keys are pressed right now)
            input_state = input_service.get_input_state()

            # Update the game (move everything, check collisions, update score, etc.)
            # The game_engine handles all of this - check services/game_engine.py to see how!
            game_engine.update(input_state)

            # Check if the game is over (player ran out of lives)
            if game_engine.is_game_over():
                game_state = GameState.GAME_OVER

        # STEP 3: Render (Draw) Everything
        # Clear the screen with a background color
        # This erases everything from the last frame so we can draw fresh
        screen.fill(BACKGROUND_COLOR)

        # Draw different things depending on what state we're in
        if game_state == GameState.MENU:
            menu.draw_start_menu(screen)

        elif game_state == GameState.PLAYING:
            # Draw all the game objects (player, enemies, projectiles)
            game_engine.render(screen)

        elif game_state == GameState.PAUSED:
            # Draw the game in the background, then draw the pause overlay on top
            game_engine.render(screen)
            menu.draw_pause_menu(screen)

        elif game_state == GameState.GAME_OVER:
            # Draw the game over screen with the final score
            menu.draw_game_over(screen, game_engine.get_score())

        # STEP 4: Flip the Display
        # Pygame uses "double buffering" - we draw to an invisible surface,
        # then "flip" it to make it visible all at once. This prevents flickering.
        pygame.display.flip()

        # STEP 5: Control Frame Rate
        # Wait just long enough to maintain the target FPS
        # This makes the game run at a consistent speed
        # FPS is defined in config.py - try changing it to see what happens!
        clock.tick(FPS)

    # When the game loop ends (user closed the window), clean up and exit
    pygame.quit()
    sys.exit()


# This is a Python idiom that means "only run main() if this file is being run directly"
# (not if it's being imported by another file)
if __name__ == "__main__":
    main()
