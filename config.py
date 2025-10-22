"""
Game Configuration File

This file contains all the "magic numbers" and settings for the game.
By keeping them all in one place, it's super easy to tweak and experiment!

Want the game to run faster? Change FPS.
Want bigger enemies? Change ENEMY_SIZE.
Want the player to move slower? Change PLAYER_SPEED.

This is the FIRST place you should look when you want to adjust how the game feels.
Think of it as the game's "settings panel" for developers!
"""

from enum import Enum

# =============================================================================
# SCREEN SETTINGS
# =============================================================================

# The size of the game window in pixels
# Try changing these to make the window bigger or smaller!
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# The title that appears in the window's title bar
GAME_TITLE = "Space Defender"

# How many frames (updates) per second the game should run
# 60 FPS is standard for smooth gameplay. Try 30 to see the difference!
FPS = 60

# =============================================================================
# COLORS (in RGB format)
# =============================================================================
# RGB stands for Red, Green, Blue. Each value is 0-255.
# You can use a color picker tool online to find RGB values for any color!

# Background color - the color that fills the screen
BACKGROUND_COLOR = (10, 10, 30)  # Dark blue, like space!

# Player spaceship color
PLAYER_COLOR = (100, 200, 255)  # Light blue

# Enemy/asteroid color
ENEMY_COLOR = (200, 50, 50)  # Red

# Projectile (bullet) color
PROJECTILE_COLOR = (255, 255, 100)  # Yellow

# Text colors for UI elements
TEXT_COLOR = (255, 255, 255)  # White
TEXT_COLOR_SECONDARY = (150, 150, 150)  # Gray

# Health/lives indicator color
HEALTH_COLOR = (0, 255, 0)  # Green

# =============================================================================
# PLAYER SETTINGS
# =============================================================================

# How fast the player moves in pixels per frame
# Higher = faster movement. Try 3 (slow) or 10 (super fast)!
PLAYER_SPEED = 5

# Player spaceship size (width and height in pixels)
# We're using a simple square/rectangle for now
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 40

# Player starting position (percentage of screen dimensions)
# 0.5 = center of screen
PLAYER_START_X_RATIO = 0.5  # Start in the horizontal center
PLAYER_START_Y_RATIO = 0.85  # Start near the bottom (0.0 = top, 1.0 = bottom)

# How many lives the player starts with
PLAYER_STARTING_LIVES = 3

# How long the player is invulnerable after being hit (in seconds)
# This prevents losing multiple lives instantly
PLAYER_INVULNERABILITY_TIME = 2.0

# =============================================================================
# PROJECTILE (BULLET) SETTINGS
# =============================================================================

# How fast projectiles move in pixels per frame
# Should be faster than the player so it looks like they're shooting forward!
PROJECTILE_SPEED = 8

# Projectile size
PROJECTILE_WIDTH = 4
PROJECTILE_HEIGHT = 12

# How long to wait between shots (in seconds)
# Lower = faster firing rate. Try 0.1 for rapid fire!
PROJECTILE_COOLDOWN = 0.3

# =============================================================================
# ENEMY SETTINGS
# =============================================================================

# How fast enemies move downward in pixels per frame
# Enemies get faster as the game progresses - this is the starting speed
ENEMY_SPEED_MIN = 1
ENEMY_SPEED_MAX = 3

# Enemy size (they're square)
ENEMY_SIZE_MIN = 20
ENEMY_SIZE_MAX = 40

# How often new enemies spawn (in seconds)
# Lower = more frequent spawning = harder game
ENEMY_SPAWN_RATE = 1.5

# How many points you get for destroying an enemy
ENEMY_POINTS = 10

# =============================================================================
# GAME PROGRESSION
# =============================================================================

# How much to increase difficulty every X points
# This makes the game gradually harder as you play
DIFFICULTY_INCREASE_INTERVAL = 100  # Increase difficulty every 100 points

# How much to speed up enemy spawn rate (multiply by this value)
# 0.9 means spawns become 10% faster
SPAWN_RATE_MULTIPLIER = 0.9

# How much to speed up enemy movement (multiply by this value)
ENEMY_SPEED_MULTIPLIER = 1.1

# =============================================================================
# GAME STATES
# =============================================================================
# This enum defines all the different "modes" the game can be in
# An enum is just a way to give names to values so code is more readable

class GameState(Enum):
    """
    Represents the different states the game can be in.

    Think of this like different "scenes" in a movie:
    - MENU: The title screen before you start playing
    - PLAYING: The actual game is running
    - PAUSED: Game is frozen but can resume
    - GAME_OVER: Player lost all lives, showing final score
    """
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"

# =============================================================================
# MULTIPLAYER SETTINGS (for future expansion!)
# =============================================================================
# TODO: These settings are here as hints for when you want to add 2-player mode!
# You don't need to use them yet, but they show where multiplayer features would go.

# Player 2 color (for when you add local multiplayer)
PLAYER2_COLOR = (255, 100, 200)  # Pink/magenta

# Player 2 starting position
PLAYER2_START_X_RATIO = 0.5
PLAYER2_START_Y_RATIO = 0.15  # Top of screen (opposite of player 1)

# =============================================================================
# TIPS FOR TWEAKING
# =============================================================================
"""
Here are some fun experiments to try by changing values in this file:

1. BULLET HELL MODE: Set ENEMY_SPAWN_RATE to 0.3 and ENEMY_SPEED_MAX to 5
2. SLOW MOTION: Set FPS to 30 (game runs at half speed)
3. RAPID FIRE: Set PROJECTILE_COOLDOWN to 0.05
4. GIANT PLAYER: Set PLAYER_WIDTH and PLAYER_HEIGHT to 60 and 80
5. TINY ENEMIES: Set ENEMY_SIZE_MAX to 15
6. PEACEFUL MODE: Set PLAYER_STARTING_LIVES to 100 (for testing without dying)
7. HARD MODE: Set PLAYER_STARTING_LIVES to 1 (one hit and you're done!)

Remember: After changing values, save this file and re-run main.py to see the changes!
"""
