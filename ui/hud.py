"""
HUD (Heads-Up Display)

The HUD shows important information during gameplay:
- Current score
- Lives remaining
- High score
- Any other stats you want to display

The HUD should be clear and readable but not distracting from the action!
"""

import pygame
from config import *


class HUD:
    """
    Manages the heads-up display shown during gameplay.

    Draws score, lives, and other game information on top of the game.
    """

    def __init__(self):
        """
        Initialize the HUD.

        Sets up fonts and any cached visual elements.
        """
        # Initialize Pygame's font system
        pygame.font.init()

        # Create fonts for different text sizes
        # The second parameter is the font size in pixels
        # None means "use the default system font"
        # TODO: You can load a custom font file instead:
        # self.large_font = pygame.font.Font("assets/game_font.ttf", 48)
        self.large_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)

        # Padding from screen edges
        self.padding = 20

    def draw(self, screen, score, lives):
        """
        Draw the HUD on the screen.

        Args:
            screen (pygame.Surface): The screen to draw on
            score (int): Current score to display
            lives (int): Number of lives remaining
        """
        # === SCORE ===
        # Render the score text
        # The second parameter (True) enables anti-aliasing for smoother text
        score_text = self.medium_font.render(f"Score: {score}", True, TEXT_COLOR)
        # Get the rectangle for positioning
        score_rect = score_text.get_rect()
        # Position in top-left corner
        score_rect.topleft = (self.padding, self.padding)
        # Draw to the screen
        screen.blit(score_text, score_rect)

        # === LIVES ===
        # Show lives in top-right corner
        lives_text = self.medium_font.render(f"Lives: {lives}", True, HEALTH_COLOR)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (SCREEN_WIDTH - self.padding, self.padding)
        screen.blit(lives_text, lives_rect)

        # Alternative: Draw hearts instead of numbers
        # self.draw_hearts(screen, lives)

        # === HIGH SCORE (optional) ===
        # TODO: You could show the high score during gameplay
        # high_score_text = self.small_font.render(f"High: {high_score}", True, TEXT_COLOR_SECONDARY)
        # high_score_rect = high_score_text.get_rect()
        # high_score_rect.midtop = (SCREEN_WIDTH // 2, self.padding)
        # screen.blit(high_score_text, high_score_rect)

    def draw_hearts(self, screen, lives):
        """
        Draw heart icons to represent lives.

        Args:
            screen (pygame.Surface): The screen to draw on
            lives (int): Number of hearts to draw

        This is a more visual way to show lives than just a number!
        """
        heart_size = 30
        heart_spacing = 35
        start_x = SCREEN_WIDTH - self.padding - (lives * heart_spacing)
        start_y = self.padding

        for i in range(lives):
            x = start_x + (i * heart_spacing)
            y = start_y

            # Draw a simple heart shape using a rectangle
            # TODO: Replace with an actual heart image!
            # heart_img = pygame.image.load("assets/heart.png")
            # heart_img = pygame.transform.scale(heart_img, (heart_size, heart_size))
            # screen.blit(heart_img, (x, y))

            # For now, draw a red square
            pygame.draw.rect(screen, HEALTH_COLOR, (x, y, heart_size, heart_size))

    def draw_message(self, screen, message, position="center"):
        """
        Draw a centered message on the screen.

        Args:
            screen (pygame.Surface): The screen to draw on
            message (str): The message to display
            position (str): Where to show it ("center", "top", "bottom")

        Useful for showing temporary messages like "LEVEL UP!" or "WAVE COMPLETE!"
        """
        text = self.large_font.render(message, True, TEXT_COLOR)
        rect = text.get_rect()

        if position == "center":
            rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif position == "top":
            rect.midtop = (SCREEN_WIDTH // 2, self.padding * 2)
        elif position == "bottom":
            rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - self.padding * 2)

        # Draw a semi-transparent background behind the text for readability
        background = pygame.Surface((rect.width + 40, rect.height + 20))
        background.fill((0, 0, 0))
        background.set_alpha(128)  # Semi-transparent
        bg_rect = background.get_rect(center=rect.center)
        screen.blit(background, bg_rect)

        # Draw the text
        screen.blit(text, rect)


# =============================================================================
# EXPANSION IDEAS FOR THE HUD
# =============================================================================
"""
Here are some ways to make your HUD more informative and attractive:

1. ANIMATED SCORE:
   - When score increases, make the number pop or flash
   - Track self.score_display and animate it toward the real score
   - Makes scoring feel more satisfying!

2. COMBO METER:
   - Show current combo multiplier
   - Visual bar that fills up with consecutive hits
   - Drains over time if no hits

3. WEAPON INDICATOR:
   - Show what weapon/power-up is active
   - Icon + name
   - Duration bar for timed power-ups

4. MINIMAP:
   - Small overview of enemy positions
   - Draw scaled-down versions of sprites
   - Helps player plan their movements

5. WARNINGS:
   - Flash "LOW HEALTH" when down to 1 life
   - Show arrows pointing to off-screen enemies
   - Alert when boss is coming

6. STATS TRACKING:
   - Accuracy percentage (hits / shots fired)
   - Time survived
   - Enemies destroyed this session
   - Show at game over

7. ACHIEVEMENTS/BADGES:
   - Show toast notification when unlocked
   - "First Blood", "100 Kills", etc.
   - Slide in from side, fade out after 2 seconds

8. PROGRESSIVE INDICATORS:
   - Progress bar to next level/wave
   - Boss health bar at top of screen
   - Charge meter for special weapons

9. PARTICLE EFFECTS:
   - Sparkles when score increases
   - Trail effect on score numbers
   - Pulse effect on low health warning

10. CUSTOM FONTS AND COLORS:
    - Load retro pixel fonts for authentic arcade feel
    - Color-code information (green = good, red = danger)
    - Gradient text for high scores

IMPLEMENTATION EXAMPLE - Animated Score:

class HUD:
    def __init__(self):
        # ... existing code ...
        self.displayed_score = 0
        self.score_animation_speed = 10

    def update(self, delta_time, actual_score):
        # Smoothly animate displayed score toward actual score
        if self.displayed_score < actual_score:
            self.displayed_score += self.score_animation_speed
            if self.displayed_score > actual_score:
                self.displayed_score = actual_score

    def draw(self, screen, score, lives):
        # Use self.displayed_score instead of score directly
        score_text = self.medium_font.render(
            f"Score: {int(self.displayed_score)}", True, TEXT_COLOR
        )
        # ... rest of drawing code ...

TODO: Try adding one or two of these features to make your HUD stand out!
"""
