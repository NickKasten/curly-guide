# Fall 2025 DevSprint StarterStubs: Space Defender Mini-Game
- Theme: Gaming Console Launch Title

## Program Context
- ACM Introduces: the DevSprint program! If you are looking for resume-building developer experience with current tools in a low-stakes, collaborative, constructive, and growth-centered environment, this is the place for you! Working on a 4-week rotation between projects and workshops, students will have the opportunity to build and present up to 3 unique, 2-week-long projects. Hope to see you there learning, building, and failing with style 😎

## Sprint #2 Prompt
- Your client is asking for a small-scale mini-game to launch on their next "state-of-art" console. Attached are stubs for an example arcade-style game built with Python and Pygame.

## Repository Layout
- `main.py` — entry point that initializes Pygame, sets up the game window, and runs the main game loop.
- `config.py` — centralized configuration file with tweakable constants (speeds, colors, spawn rates, screen dimensions).
- `requirements.txt` — list of Python package dependencies (just pygame for now).
- `services/game_engine.py` — core game loop logic, handling update and render cycles with detailed comments.
- `services/collision_service.py` — helper functions for detecting collisions between game objects using Pygame rects.
- `services/score_service.py` — manages score tracking, high score persistence to a JSON file.
- `services/input_service.py` — wraps keyboard input handling for cleaner game code.
- `entities/base_entity.py` — base class for all game objects, demonstrating OOP patterns.
- `entities/player.py` — player spaceship sprite with movement and shooting mechanics.
- `entities/enemy.py` — asteroid/enemy sprite with spawning and movement logic.
- `entities/projectile.py` — bullet/laser sprite that the player shoots.
- `ui/hud.py` — renders score, lives counter, and game-over messages on screen.
- `ui/menu.py` — start screen and pause menu rendering.
- `assets/` — placeholder folder for images and sounds (currently uses simple shapes drawn with Pygame).
- `docs/sprint-brief.md` — condensed copy of the description and prompt plus tasks to tackle next.
- `docs/multiplayer-extension.md` — hints and architecture guidance for adding local 2-player mode later.

## Getting Started

### 1. Star and fork the repo
On GitHub, click ⭐ "Star" to bookmark the project and hit "Fork" so you can push changes to your own copy.

### 2. Get the files onto your computer
Click the green `<> Code` button on GitHub, choose "Download ZIP", and unzip it somewhere easy to find (e.g., your Desktop). Alternatively, if you already know Git, clone the repo instead:
```bash
git clone https://github.com/YOUR-USERNAME/curly-guide.git
cd curly-guide
```

### 3. Install Python
You need Python 3.8 or newer. Check if you already have it:
```bash
python3 --version
```
If you don't have Python or have an older version, download it from [python.org](https://www.python.org/downloads/). During installation on Windows, make sure to check "Add Python to PATH".

### 4. Install a friendly code editor
[VS Code](https://code.visualstudio.com/) is free and works on macOS, Windows, and Linux. Install it if you don't already have a preferred editor. Once installed, consider adding the Python extension for better syntax highlighting and debugging.

### 5. Open the project folder
Launch your editor, pick `File → Open Folder…`, and select the `curly-guide` directory. You should now see the `services`, `entities`, `ui`, `docs`, and other folders in the sidebar.

### 6. Set up a virtual environment (recommended)
A virtual environment keeps your project dependencies isolated. In your terminal (inside the project folder):
```bash
# Create a virtual environment
python3 -m venv venv

# Activate it:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
You'll see `(venv)` appear in your terminal prompt when it's active.

### 7. Install dependencies
With your virtual environment active, install Pygame:
```bash
pip install -r requirements.txt
```
This reads `requirements.txt` and installs pygame automatically.

### 8. Run the game
```bash
python3 main.py
```
A window should appear with the starter game! You can move the player spaceship with arrow keys and shoot with the spacebar.

### 9. Skim the TODOs
Every file contains `TODO:` markers and extensive comments explaining what each part does and where you can expand. Start with `main.py` and `config.py` to see how everything connects, then explore `entities/player.py` to understand the player mechanics.

### 10. Edit one thing at a time
Make a tiny change (for example, tweak `PLAYER_SPEED` in `config.py`), save the file, re-run `python3 main.py`, and confirm the result. This builds confidence as you go and helps you understand how each piece affects the game.

### 11. Document your progress
Use `docs/sprint-brief.md` to note what you tried, what worked, and what you'd like to improve next. Keep a dev journal of your learning journey!

## Suggested Next Steps
- Jot down 2-3 user stories in `docs/sprint-brief.md` that describe who will play your game and what "fun" looks like for them. A user story is just a single sentence in plain language (e.g., "As a retro-game fan, I want satisfying collision feedback so that destroying asteroids feels rewarding.") with focus on the player experience.
- Sketch (paper is fine) the game screens: start menu, gameplay, game over. What does the player see and do at each stage?
- Outline what makes your game unique: will you add power-ups? Different enemy types? Boss battles? Note your ideas and prioritize them.
- Decide on a visual style: will you stick with simple colored shapes, find free pixel art, or draw your own sprites? List resources you'll need.
- Plan your scoring system: how do players earn points? Is there a combo multiplier? Write down the rules before coding them.
- **Pick one small improvement to build first** and plan how you will test it manually. Start simple and iterate!

## Beginner-Friendly Resources

### Python Basics
- [Python.org Official Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — free book, great for beginners
- [Real Python — Python Basics](https://realpython.com/tutorials/basics/)
- [Codecademy — Learn Python 3](https://www.codecademy.com/learn/learn-python-3)

### Pygame Game Development
- [Pygame Official Documentation](https://www.pygame.org/docs/)
- [Pygame Tutorial — Real Python](https://realpython.com/pygame-a-primer/)
- [Kids Can Code — Pygame Tutorials (YouTube)](https://www.youtube.com/c/KidsCanCodeOrg/playlists)
- [Clear Code — Ultimate Introduction to Pygame (YouTube)](https://www.youtube.com/watch?v=AY9MnQ4x3zk)
- [Program Arcade Games with Python and Pygame](http://programarcadegames.com/)
- [Pygame Zero — Simpler Pygame for absolute beginners](https://pygame-zero.readthedocs.io/)

### Game Development Concepts
- [Game Programming Patterns](https://gameprogrammingpatterns.com/) — free online book
- [Extra Credits — Making Your First Game (YouTube series)](https://www.youtube.com/watch?v=z06QR-tz1_o&list=PLhyKYa0YJ_5C6QC36h5eApOyXtx98ehGi)
- [GDC — Game Developer's Conference talks (YouTube)](https://www.youtube.com/c/Gdconf)

### Assets and Art
- [OpenGameArt.org](https://opengameart.org/) — free game sprites, sounds, and music
- [itch.io Free Game Assets](https://itch.io/game-assets/free)
- [Kenney.nl](https://kenney.nl/assets) — quality free game assets
- [Piskel](https://www.piskelapp.com/) — free online pixel art editor

### Git and Version Control
- [GitHub Guides — Hello World](https://guides.github.com/activities/hello-world/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Learn Git Branching (interactive)](https://learngitbranching.js.org/)

### Python Environment Help
- [Python Virtual Environments Explained](https://realpython.com/python-virtual-environments-a-primer/)
- [pip Documentation](https://pip.pypa.io/en/stable/getting-started/)

## Troubleshooting

### "python3: command not found" or "python: command not found"
- Make sure Python is installed and added to your PATH
- On Windows, try `py` or `python` instead of `python3`
- On macOS, you might need to install Python via [Homebrew](https://brew.sh/): `brew install python`

### "No module named 'pygame'"
- Make sure your virtual environment is activated (you should see `(venv)` in your terminal)
- Run `pip install -r requirements.txt` again
- Try `pip3 install pygame` directly

### Game window doesn't appear or closes immediately
- Check the terminal for error messages
- Make sure you're running `python3 main.py` from the project root directory
- Look for syntax errors in any files you've edited

### Game runs slowly or feels choppy
- Check that your computer meets basic requirements (any computer from the last 10 years should be fine)
- Try reducing `SCREEN_WIDTH` and `SCREEN_HEIGHT` in `config.py`
- Close other resource-intensive programs

## Tips for Success
- **Start small**: Get one feature working before adding another
- **Test frequently**: Run the game after every small change
- **Read the comments**: Every file has explanations to guide you
- **Ask for help**: Use the DevSprint community, office hours, or online forums
- **Have fun**: This is about learning and experimenting, not perfection!

Good luck, and enjoy building your mini-game!
