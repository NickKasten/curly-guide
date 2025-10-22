"""
Menu UI

This module handles all the menu screens:
- Start menu (title screen)
- Pause menu
- Game over screen

Menus are the first and last thing players see, so make them good!
"""

import pygame
from config import *


class Menu:
    """
    Manages all menu screens in the game.

    Each menu is drawn as an overlay on top of the game screen.
    """

    def __init__(self):
        """
        Initialize the menu system.

        Sets up fonts and any pre-rendered menu elements.
        """
        pygame.font.init()

        # Create fonts for different text sizes
        self.title_font = pygame.font.Font(None, 72)
        self.large_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

    def draw_start_menu(self, screen):
        """
        Draw the start menu (title screen).

        Args:
            screen (pygame.Surface): The screen to draw on

        This is what players see when they first launch the game.
        """
        # Semi-transparent background overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BACKGROUND_COLOR)
        overlay.set_alpha(250)
        screen.blit(overlay, (0, 0))

        # === GAME TITLE ===
        title_text = self.title_font.render(GAME_TITLE, True, PLAYER_COLOR)
        title_rect = title_text.get_rect()
        title_rect.centerx = SCREEN_WIDTH // 2
        title_rect.centery = SCREEN_HEIGHT // 3
        screen.blit(title_text, title_rect)

        # === INSTRUCTIONS ===
        instructions = [
            "CONTROLS:",
            "Arrow Keys - Move",
            "Spacebar - Shoot",
            "",
            "Press SPACE to Start"
        ]

        y_offset = SCREEN_HEIGHT // 2
        for i, line in enumerate(instructions):
            # Make the last line (start prompt) more prominent
            if i == len(instructions) - 1:
                text = self.medium_font.render(line, True, TEXT_COLOR)
            else:
                text = self.small_font.render(line, True, TEXT_COLOR_SECONDARY)

            text_rect = text.get_rect()
            text_rect.centerx = SCREEN_WIDTH // 2
            text_rect.centery = y_offset + (i * 30)
            screen.blit(text, text_rect)

        # === FOOTER ===
        footer_text = self.small_font.render("A DevSprint Mini-Game", True, TEXT_COLOR_SECONDARY)
        footer_rect = footer_text.get_rect()
        footer_rect.centerx = SCREEN_WIDTH // 2
        footer_rect.bottom = SCREEN_HEIGHT - 20
        screen.blit(footer_text, footer_rect)

        # TODO: Add animated elements!
        # - Blinking "Press Space" text
        # - Floating stars or particles
        # - Demo gameplay in the background
        # - High score display

    def draw_pause_menu(self, screen):
        """
        Draw the pause menu overlay.

        Args:
            screen (pygame.Surface): The screen to draw on

        Shown when the player presses ESC during gameplay.
        The game is drawn underneath, but frozen.
        """
        # Semi-transparent dark overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)  # Transparent so you can see the frozen game
        screen.blit(overlay, (0, 0))

        # === PAUSED TEXT ===
        paused_text = self.large_font.render("PAUSED", True, TEXT_COLOR)
        paused_rect = paused_text.get_rect()
        paused_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        screen.blit(paused_text, paused_rect)

        # === RESUME INSTRUCTION ===
        resume_text = self.medium_font.render("Press ESC to Resume", True, TEXT_COLOR_SECONDARY)
        resume_rect = resume_text.get_rect()
        resume_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
        screen.blit(resume_text, resume_rect)

        # TODO: Add pause menu options:
        # - Resume
        # - Restart
        # - Options/Settings
        # - Quit to Main Menu

    def draw_game_over(self, screen, final_score):
        """
        Draw the game over screen.

        Args:
            screen (pygame.Surface): The screen to draw on
            final_score (int): The player's final score

        Shown when the player runs out of lives.
        """
        # Dark overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BACKGROUND_COLOR)
        overlay.set_alpha(240)
        screen.blit(overlay, (0, 0))

        # === GAME OVER TEXT ===
        game_over_text = self.title_font.render("GAME OVER", True, ENEMY_COLOR)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.centerx = SCREEN_WIDTH // 2
        game_over_rect.centery = SCREEN_HEIGHT // 3
        screen.blit(game_over_text, game_over_rect)

        # === FINAL SCORE ===
        score_text = self.large_font.render(f"Score: {final_score}", True, TEXT_COLOR)
        score_rect = score_text.get_rect()
        score_rect.centerx = SCREEN_WIDTH // 2
        score_rect.centery = SCREEN_HEIGHT // 2
        screen.blit(score_text, score_rect)

        # === HIGH SCORE CHECK ===
        # TODO: Load high score and compare
        # if final_score >= high_score:
        #     new_high_text = self.medium_font.render("NEW HIGH SCORE!", True, PLAYER_COLOR)
        #     new_high_rect = new_high_text.get_rect()
        #     new_high_rect.centerx = SCREEN_WIDTH // 2
        #     new_high_rect.centery = SCREEN_HEIGHT // 2 + 60
        #     screen.blit(new_high_text, new_high_rect)

        # === RESTART INSTRUCTION ===
        restart_text = self.medium_font.render("Press SPACE to Return to Menu", True, TEXT_COLOR_SECONDARY)
        restart_rect = restart_text.get_rect()
        restart_rect.centerx = SCREEN_WIDTH // 2
        restart_rect.centery = SCREEN_HEIGHT - 100
        screen.blit(restart_text, restart_rect)

        # TODO: Add stats summary:
        # - Enemies destroyed
        # - Accuracy
        # - Time survived
        # - Achievements unlocked

    def draw_button(self, screen, text, x, y, width, height, color, hover_color, action=None):
        """
        Draw a clickable button.

        Args:
            screen (pygame.Surface): The screen to draw on
            text (str): Button text
            x, y (int): Top-left position
            width, height (int): Button dimensions
            color (tuple): Normal button color
            hover_color (tuple): Color when mouse is over the button
            action (callable): Function to call when clicked (optional)

        This is a helper for creating clickable menu buttons with mouse support.
        """
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Create the button rectangle
        button_rect = pygame.Rect(x, y, width, height)

        # Check if mouse is hovering over the button
        is_hovering = button_rect.collidepoint(mouse_pos)

        # Choose color based on hover state
        current_color = hover_color if is_hovering else color

        # Draw the button
        pygame.draw.rect(screen, current_color, button_rect)
        pygame.draw.rect(screen, TEXT_COLOR, button_rect, 2)  # Border

        # Draw the text centered on the button
        text_surface = self.medium_font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

        # Handle click
        if is_hovering and mouse_click[0] and action:
            action()


# =============================================================================
# EXPANSION IDEAS FOR MENUS
# =============================================================================
"""
Menus can be much more than just text on a screen:

1. ANIMATED BACKGROUNDS:
   - Stars scrolling by
   - Demo gameplay running in background
   - Particle effects
   - Rotating 3D title

2. MOUSE SUPPORT:
   - Clickable buttons (see draw_button above)
   - Hover effects
   - More accessible than keyboard-only

3. SETTINGS MENU:
   - Volume sliders
   - Difficulty selection
   - Key rebinding
   - Graphics options (fullscreen, resolution)

4. CREDITS SCREEN:
   - Scrolling credits
   - List of developers, artists, musicians
   - Links to resources used

5. LEVEL SELECT:
   - If you add multiple levels/stages
   - Show unlocked levels
   - Best score for each level

6. LEADERBOARD:
   - Top 10 high scores
   - Player names
   - Maybe even online global leaderboard

7. ACHIEVEMENTS:
   - List of achievements
   - Show locked/unlocked status
   - Progress bars for partial achievements

8. TUTORIALS:
   - How to play screen with images/animations
   - Tips and tricks
   - Control diagram

9. SOUND EFFECTS:
   - Menu navigation sounds
   - Button click sounds
   - Music for each menu screen

10. TRANSITIONS:
    - Fade in/out between screens
    - Slide animations
    - Make the game feel polished

IMPLEMENTATION EXAMPLE - Animated "Press Space" Text:

class Menu:
    def __init__(self):
        # ... existing code ...
        self.blink_timer = 0.0
        self.show_start_prompt = True

    def update(self, delta_time):
        # Toggle visibility every 0.5 seconds
        self.blink_timer += delta_time
        if self.blink_timer >= 0.5:
            self.show_start_prompt = not self.show_start_prompt
            self.blink_timer = 0.0

    def draw_start_menu(self, screen):
        # ... existing code ...

        # Only show "Press SPACE" when visible
        if self.show_start_prompt:
            start_text = self.medium_font.render("Press SPACE to Start", True, TEXT_COLOR)
            # ... draw code ...

IMPLEMENTATION EXAMPLE - Settings Menu:

class Menu:
    def __init__(self):
        # ... existing code ...
        self.volume = 0.5

    def draw_settings_menu(self, screen):
        # Title
        settings_text = self.large_font.render("SETTINGS", True, TEXT_COLOR)
        # ... positioning ...

        # Volume slider
        self.draw_slider(screen, "Volume", 100, 200, 400, self.volume)

        # Buttons
        self.draw_button(screen, "Back", 300, 400, 200, 50,
                        (50, 50, 50), (100, 100, 100),
                        action=self.return_to_main_menu)

    def draw_slider(self, screen, label, x, y, width, value):
        # Draw slider background
        pygame.draw.rect(screen, (50, 50, 50), (x, y, width, 20))
        # Draw slider position
        slider_x = x + int(value * width)
        pygame.draw.circle(screen, PLAYER_COLOR, (slider_x, y + 10), 15)
        # Draw label
        label_text = self.small_font.render(label, True, TEXT_COLOR)
        screen.blit(label_text, (x, y - 30))

TODO: Pick a few menu improvements and make your game feel professional!
"""
