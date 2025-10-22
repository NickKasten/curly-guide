# Quick Start Guide

Want to get the game running in 5 minutes? Follow these steps!

## Prerequisites
- Python 3.8 or newer installed
- Terminal/Command Prompt access

## Installation (One-Time Setup)

### 1. Navigate to the project folder
```bash
cd path/to/curly-guide
```

### 2. Create a virtual environment (recommended)
```bash
# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install Pygame
```bash
pip install -r requirements.txt
```

## Running the Game

```bash
# macOS/Linux:
python3 main.py

# Windows:
python main.py
```

That's it! The game window should appear.

## Controls

**Movement:** Arrow keys (← →)
**Shoot:** Spacebar
**Pause:** ESC
**Start Game:** Space or Enter (from menu)

## What to Do Next

1. **Play the game** - Get familiar with the mechanics
2. **Read the code** - Start with `main.py` and `config.py`
3. **Tweak settings** - Change values in `config.py` and see what happens
4. **Check the docs** - Read `docs/sprint-brief.md` for ideas
5. **Start building** - Pick one feature and implement it!

## Troubleshooting

**"python3: command not found"**
→ Try `python` instead of `python3`, or install Python from python.org

**"No module named 'pygame'"**
→ Make sure you ran `pip install -r requirements.txt` with venv activated

**Game window appears then closes**
→ Check the terminal for error messages

**Need help?**
→ Check the full README.md or ask in the DevSprint community!

---

Ready to build something awesome? Let's go! 🚀
