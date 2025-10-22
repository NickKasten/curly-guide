# Sprint 2 Brief

## Program Snapshot
ACM Introduces: the DevSprint program! If you are looking for resume-building developer experience with current tools in a low-stakes, collaborative, constructive, and growth-centered environment, this is the place for you! Working on a 4-week rotation between projects and workshops, students will have the opportunity to build and present up to 3 unique, 2-week-long projects. Hope to see you there learning, building, and failing with style 😎

## Client Prompt
Your client is asking for a small-scale mini-game to launch on their next "state-of-art" console. The game should be simple, fun, and completable within a 2-week development sprint. It should demonstrate core game mechanics and be expandable for future updates.

## Working Goals
- Understand your player's experience: who will play this game, and what makes it fun?
- Implement the core game loop: movement, shooting, collision, scoring
- Polish the user interface: menus, HUD, and visual feedback
- Collect feedback from playtesters and iterate during the two-week sprint
- Document your code thoroughly to help future developers (including yourself!)

## Core Features (MVP - Minimum Viable Product)
- ✓ Player movement with arrow keys
- ✓ Player shooting with spacebar
- ✓ Enemies spawning from the top of the screen
- ✓ Collision detection (bullets hitting enemies, enemies hitting player)
- ✓ Score tracking and display
- ✓ Lives/health system
- ✓ Game over condition
- ✓ Start menu and game over screen
- ✓ Increasing difficulty over time

## Ideas for Extensions
Once you have the basic game working, here are some features to add:

### Week 1 Extensions (Polish the basics)
- Add sound effects (shooting, explosions, damage)
- Add background music
- Create visual effects (explosions, particle trails)
- Improve the sprites (replace colored rectangles with actual art)
- Add a pause menu
- Display high score on game over screen
- Save high scores between sessions

### Week 2 Extensions (New mechanics)
- Power-ups (faster shooting, spread shot, shield, etc.)
- Different enemy types with unique behaviors
- Boss battles every X points
- Combo/multiplier system for consecutive hits
- Screen shake and camera effects
- Achievements/challenges
- Multiple difficulty modes
- Local 2-player mode (see multiplayer-extension.md)

### Stretch Goals (If you have time)
- Persistent progression (unlockables, upgrades)
- Multiple levels or stages
- Enemy formations and wave patterns
- Player ship upgrades
- Online leaderboards
- Mobile/touch controls
- Procedural enemy generation
- Story mode with cutscenes

## User Stories
Write 2-3 user stories to guide your development. Focus on the player experience!

Example user stories:
- "As a casual gamer, I want simple controls so that I can start playing immediately without a tutorial."
- "As a competitive player, I want to see my high score so that I have a goal to beat."
- "As someone with 5 minutes to spare, I want quick gameplay sessions so I can play during short breaks."

**Your user stories:**
1.
2.
3.

## Development Log
Use this section to track your progress, note what worked, and plan next steps.

### Day 1 (Date: _______)
**What I did:**
-

**What worked:**
-

**Challenges:**
-

**Next steps:**
-

### Day 2 (Date: _______)
**What I did:**
-

**What worked:**
-

**Challenges:**
-

**Next steps:**
-

### Day 3 (Date: _______)
**What I did:**
-

**What worked:**
-

**Challenges:**
-

**Next steps:**
-

_(Continue this pattern for each work session)_

## Testing Checklist
Before considering a feature "done", test these scenarios:

### Basic Gameplay
- [ ] Player can move in all allowed directions
- [ ] Player cannot move off-screen
- [ ] Player can shoot by pressing spacebar
- [ ] Bullets travel upward and disappear off-screen
- [ ] Enemies spawn at regular intervals
- [ ] Enemies move downward at consistent speed
- [ ] Game doesn't crash after playing for 5+ minutes

### Collision Detection
- [ ] Bullets destroy enemies on contact
- [ ] Enemies damage player on contact
- [ ] Player loses a life when hit
- [ ] Score increases when enemy is destroyed
- [ ] Player becomes temporarily invulnerable after being hit

### Game Flow
- [ ] Game starts in menu state
- [ ] Pressing Space/Enter starts the game
- [ ] Game over screen appears when lives reach 0
- [ ] Final score is displayed correctly
- [ ] Player can return to menu from game over
- [ ] ESC pauses the game
- [ ] Game can be resumed from pause

### UI/UX
- [ ] Score is visible and updates correctly
- [ ] Lives/health is clearly displayed
- [ ] Controls are explained on the start screen
- [ ] Text is readable (good contrast, font size)
- [ ] Game runs smoothly without lag

### Edge Cases
- [ ] Game handles spam-clicking shoot button
- [ ] Game handles holding down movement keys
- [ ] Difficulty increases as score goes up
- [ ] High score is saved when game closes
- [ ] High score loads correctly when game restarts

## Playtesting Feedback
Get 2-3 people to play your game and note their feedback here:

### Playtester 1 (Name: _______)
**What they liked:**
-

**What confused them:**
-

**Suggestions:**
-

**Observations:**
-

### Playtester 2 (Name: _______)
**What they liked:**
-

**What confused them:**
-

**Suggestions:**
-

**Observations:**
-

## Presentation Prep
At the end of the sprint, you'll demo your game! Prepare to answer:

1. **What is your game?** (30-second pitch)
   -

2. **What was the most challenging part?**
   -

3. **What are you most proud of?**
   -

4. **If you had more time, what would you add?**
   -

5. **What did you learn?**
   -

## Resources You Used
Keep track of tutorials, assets, and resources that helped you:

### Code/Tutorials
-

### Art/Sprites
-

### Sound Effects/Music
-

### Tools
-

## Notes and Ideas
Random thoughts, future ideas, or things to remember:

-
-
-

---

Update this brief as your sprint evolves. Good luck and have fun! 🚀
