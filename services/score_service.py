"""
Score Service

This module handles everything related to scoring:
- Tracking the current score
- Saving and loading high scores
- Persisting scores to a file so they survive between game sessions

Seeing a high score motivates players to keep trying to beat it!
"""

import json
import os

# The file where we'll save high scores
# It will be created in the same directory as the game
HIGHSCORE_FILE = "highscores.json"


class ScoreService:
    """
    Manages scoring and high score persistence.

    This class keeps track of:
    - The current score during gameplay
    - The all-time high score
    - Saving/loading scores from a file
    """

    def __init__(self):
        """
        Initialize the score service.

        Sets up the current score and loads the high score from file.
        """
        self.current_score = 0
        self.high_score = self.load_high_score()

    def add_points(self, points):
        """
        Add points to the current score.

        Args:
            points (int): The number of points to add

        This is called whenever the player does something good:
        - Destroying an enemy
        - Collecting a power-up
        - Completing a wave
        - Etc.

        Example:
            score_service.add_points(10)  # Player destroyed an enemy
        """
        self.current_score += points

        # Check if we've beaten the high score!
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            # TODO: You could add a visual effect or sound here to celebrate!
            # print("NEW HIGH SCORE!")

    def get_current_score(self):
        """
        Get the current score.

        Returns:
            int: The current score

        Example:
            score = score_service.get_current_score()
            print(f"Score: {score}")
        """
        return self.current_score

    def get_high_score(self):
        """
        Get the all-time high score.

        Returns:
            int: The high score

        Example:
            high = score_service.get_high_score()
            print(f"High Score: {high}")
        """
        return self.high_score

    def reset_score(self):
        """
        Reset the current score to 0.

        Called when starting a new game.
        The high score is NOT reset - it persists across games!

        Example:
            score_service.reset_score()  # Start a new game
        """
        self.current_score = 0

    def save_high_score(self):
        """
        Save the high score to a file.

        This writes the score to a JSON file so it persists
        even after you close the game.

        JSON is a simple text format that looks like Python dictionaries.
        You can open highscores.json in a text editor to see it!

        Called automatically when the game ends.
        """
        try:
            # Create a dictionary with our score data
            data = {
                "high_score": self.high_score
                # TODO: You could add more data here:
                # "player_name": name,
                # "date": datetime.now(),
                # "top_10_scores": [scores...],
            }

            # Write it to a file in JSON format
            # 'w' means "write mode" - create the file if it doesn't exist
            with open(HIGHSCORE_FILE, 'w') as file:
                # json.dump() converts the dictionary to JSON and saves it
                # indent=4 makes it pretty and readable
                json.dump(data, file, indent=4)

        except Exception as e:
            # If something goes wrong (disk full, permissions, etc.),
            # print an error but don't crash the game
            print(f"Warning: Could not save high score: {e}")

    def load_high_score(self):
        """
        Load the high score from a file.

        Returns:
            int: The saved high score, or 0 if no save file exists

        Called when the game starts to restore the previous high score.

        If the file doesn't exist (first time playing), we return 0.
        If the file is corrupted, we also return 0 and print a warning.
        """
        # Check if the save file exists
        if not os.path.exists(HIGHSCORE_FILE):
            # First time playing - no high score yet!
            return 0

        try:
            # 'r' means "read mode"
            with open(HIGHSCORE_FILE, 'r') as file:
                # json.load() reads the file and converts it back to a dictionary
                data = json.load(file)

                # Get the high score from the dictionary
                # .get() is safer than [] because it returns 0 if the key doesn't exist
                return data.get("high_score", 0)

        except Exception as e:
            # If the file is corrupted or can't be read, print a warning
            # and return 0 so the game can still run
            print(f"Warning: Could not load high score: {e}")
            return 0

    def is_high_score(self):
        """
        Check if the current score is a new high score.

        Returns:
            bool: True if current score equals or beats the high score

        This is useful for showing a "NEW HIGH SCORE!" message
        on the game over screen.

        Example:
            if score_service.is_high_score():
                show_celebration_animation()
        """
        return self.current_score >= self.high_score


# =============================================================================
# EXPANSION IDEAS
# =============================================================================
"""
Here are some cool features you could add to the score system:

1. LEADERBOARD: Store top 10 scores instead of just one
   - Keep a list of {"name": "Player", "score": 1000, "date": "2024-01-01"}
   - Sort by score and keep only top 10

2. PLAYER NAMES: Let players enter their name for the high score
   - Add a text input screen after getting a high score
   - Save name alongside score

3. STATISTICS: Track more than just score
   - Total enemies destroyed
   - Total shots fired
   - Accuracy percentage (hits / shots)
   - Time played

4. ACHIEVEMENTS: Award points for special accomplishments
   - "First Blood" - destroy first enemy
   - "Sharpshooter" - 10 hits in a row
   - "Survivor" - last 60 seconds

5. COMBO SYSTEM: Bonus points for consecutive hits
   - Track time since last hit
   - Multiply points: 2x, 3x, 5x for combos
   - Reset combo if player misses for too long

6. SAVE TO CLOUD: Use an online database
   - Compare scores with friends
   - Global leaderboards
   - (This is advanced - requires backend/API knowledge)

TODO: Pick one of these ideas and try implementing it in Week 2!
"""
