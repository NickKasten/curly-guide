# Adding Local 2-Player Mode

This guide will help you extend the game to support local multiplayer, where two players can play on the same keyboard!

## Overview

Local multiplayer means two players share one computer and keyboard. This is different from online multiplayer (which requires networking and is much more complex).

**Key Concept:** Instead of having one player, you'll have two player objects that update and render independently.

## Architecture Changes Needed

### 1. Config Changes

First, open `config.py` and you'll see there are already some Player 2 settings commented out:

```python
# Player 2 color (for when you add local multiplayer)
PLAYER2_COLOR = (255, 100, 200)  # Pink/magenta

# Player 2 starting position
PLAYER2_START_X_RATIO = 0.5
PLAYER2_START_Y_RATIO = 0.15  # Top of screen (opposite of player 1)
```

These are ready to use! Player 2 will start at the top of the screen and shoot downward.

### 2. Input Service Changes

Open `services/input_service.py`. You'll need to modify it to return input for BOTH players.

**Current approach (single player):**
```python
def get_input_state(self):
    keys = pygame.key.get_pressed()
    return {
        "move_left": keys[pygame.K_LEFT],
        "move_right": keys[pygame.K_RIGHT],
        "shoot": keys[pygame.K_SPACE],
    }
```

**New approach (two players):**

#### Option A: Return two separate dictionaries
```python
def get_input_state(self):
    """Returns (player1_input, player2_input)"""
    keys = pygame.key.get_pressed()

    player1_input = {
        "move_left": keys[pygame.K_LEFT],
        "move_right": keys[pygame.K_RIGHT],
        "shoot": keys[pygame.K_SPACE],
    }

    player2_input = {
        "move_left": keys[pygame.K_a],      # WASD controls
        "move_right": keys[pygame.K_d],
        "shoot": keys[pygame.K_LSHIFT],     # Left Shift to shoot
    }

    return player1_input, player2_input
```

#### Option B: Return one dictionary with both players
```python
def get_input_state(self):
    keys = pygame.key.get_pressed()
    return {
        "p1_move_left": keys[pygame.K_LEFT],
        "p1_move_right": keys[pygame.K_RIGHT],
        "p1_shoot": keys[pygame.K_SPACE],
        "p2_move_left": keys[pygame.K_a],
        "p2_move_right": keys[pygame.K_d],
        "p2_shoot": keys[pygame.K_LSHIFT],
    }
```

**Recommendation:** Use Option A (two dictionaries) as it's cleaner and matches the current player code structure.

### 3. Game Engine Changes

Open `services/game_engine.py`. This is where most of the multiplayer logic goes!

#### Step 1: Add a second player in `__init__`

Find the section where the player is created (around line 50):
```python
# === PLAYER ===
start_x = SCREEN_WIDTH * PLAYER_START_X_RATIO
start_y = SCREEN_HEIGHT * PLAYER_START_Y_RATIO
self.player = Player(start_x, start_y)
self.all_sprites.add(self.player)
```

Add Player 2 right after:
```python
# === PLAYER 2 ===
start_x2 = SCREEN_WIDTH * PLAYER2_START_X_RATIO
start_y2 = SCREEN_HEIGHT * PLAYER2_START_Y_RATIO
self.player2 = Player(start_x2, start_y2, PLAYER2_COLOR)
self.all_sprites.add(self.player2)
```

#### Step 2: Add a second projectile group

Find where `self.player_projectiles` is created:
```python
self.player_projectiles = pygame.sprite.Group()
```

Add Player 2's projectiles:
```python
self.player_projectiles = pygame.sprite.Group()
self.player2_projectiles = pygame.sprite.Group()
```

#### Step 3: Update both players in `update()`

Find the player update section in the `update()` method:
```python
# === UPDATE PLAYER ===
self.player.update(input_state, self.delta_time)
```

Change it to:
```python
# === UPDATE PLAYERS ===
# Get input for both players
player1_input, player2_input = input_state  # Unpack the tuple

# Update both players
self.player.update(player1_input, self.delta_time)
self.player2.update(player2_input, self.delta_time)
```

#### Step 4: Handle shooting for both players

Find the shooting section:
```python
if input_state["shoot"] and self.player.can_shoot():
    projectile = self.player.shoot()
    if projectile:
        self.player_projectiles.add(projectile)
        self.all_sprites.add(projectile)
```

Update it for both players:
```python
# Player 1 shooting
if player1_input["shoot"] and self.player.can_shoot():
    projectile = self.player.shoot()
    if projectile:
        self.player_projectiles.add(projectile)
        self.all_sprites.add(projectile)

# Player 2 shooting
if player2_input["shoot"] and self.player2.can_shoot():
    projectile = self.player2.shoot()
    if projectile:
        self.player2_projectiles.add(projectile)
        self.all_sprites.add(projectile)
```

#### Step 5: Check collisions for both players' projectiles

Find the collision checking in `check_collisions()`:
```python
# === PROJECTILES HIT ENEMIES ===
hits = check_group_collision(self.player_projectiles, self.enemies, True, True)
for projectile, hit_enemies in hits.items():
    for enemy in hit_enemies:
        self.score_service.add_points(ENEMY_POINTS)
```

Duplicate this for Player 2:
```python
# === PLAYER 1 PROJECTILES HIT ENEMIES ===
hits = check_group_collision(self.player_projectiles, self.enemies, True, True)
for projectile, hit_enemies in hits.items():
    for enemy in hit_enemies:
        self.score_service.add_points(ENEMY_POINTS)

# === PLAYER 2 PROJECTILES HIT ENEMIES ===
hits2 = check_group_collision(self.player2_projectiles, self.enemies, True, True)
for projectile, hit_enemies in hits2.items():
    for enemy in hit_enemies:
        self.score_service.add_points(ENEMY_POINTS)
```

#### Step 6: Check enemies hitting both players

Find where enemies hit the player:
```python
player_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
if player_hits:
    self.player.take_damage()
    # ... rest of code
```

Add Player 2 collision checking:
```python
# Player 1 collisions
player_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
if player_hits:
    self.player.take_damage()
    self.player_invulnerable_timer = PLAYER_INVULNERABILITY_TIME
    for enemy in player_hits:
        enemy.kill()

# Player 2 collisions
if self.player2_invulnerable_timer <= 0:  # Add this timer in __init__!
    player2_hits = pygame.sprite.spritecollide(self.player2, self.enemies, False)
    if player2_hits:
        self.player2.take_damage()
        self.player2_invulnerable_timer = PLAYER_INVULNERABILITY_TIME
        for enemy in player2_hits:
            enemy.kill()
```

Don't forget to add `self.player2_invulnerable_timer = 0.0` in the `__init__` method!

#### Step 7: Update cleanup for both projectile groups

In `cleanup_sprites()`, add Player 2's projectiles:
```python
# Check projectiles
for projectile in self.player_projectiles:
    if check_out_of_bounds(projectile.rect, SCREEN_WIDTH, SCREEN_HEIGHT, margin):
        projectile.kill()

for projectile in self.player2_projectiles:
    if check_out_of_bounds(projectile.rect, SCREEN_WIDTH, SCREEN_HEIGHT, margin):
        projectile.kill()
```

#### Step 8: Update reset() method

Don't forget to reset Player 2 when starting a new game!

```python
def reset(self):
    # ... existing reset code ...

    # Recreate Player 2
    start_x2 = SCREEN_WIDTH * PLAYER2_START_X_RATIO
    start_y2 = SCREEN_HEIGHT * PLAYER2_START_Y_RATIO
    self.player2 = Player(start_x2, start_y2, PLAYER2_COLOR)
    self.all_sprites.add(self.player2)

    # Clear Player 2 projectiles
    self.player2_projectiles.empty()

    # Reset Player 2 invulnerability
    self.player2_invulnerable_timer = 0.0
```

### 4. Game Over Condition

You need to decide: does the game end when ONE player dies or when BOTH players die?

**Option A: Game ends when either player dies**
```python
def is_game_over(self):
    is_over = self.player.lives <= 0 or self.player2.lives <= 0
    if is_over:
        self.score_service.save_high_score()
    return is_over
```

**Option B: Game ends only when both players die (more forgiving)**
```python
def is_game_over(self):
    is_over = self.player.lives <= 0 and self.player2.lives <= 0
    if is_over:
        self.score_service.save_high_score()
    return is_over
```

### 5. Main.py Changes

Open `main.py` and find where `get_input_state()` is called:

**Current code:**
```python
input_state = input_service.get_input_state()
game_engine.update(input_state)
```

**New code (if using Option A from Input Service):**
```python
player1_input, player2_input = input_service.get_input_state()
game_engine.update((player1_input, player2_input))
```

Or you can leave it as-is if you made the input service return a tuple - the game engine will unpack it.

### 6. HUD Changes (Optional)

You might want to show both players' lives separately. Open `ui/hud.py`:

```python
def draw(self, screen, score, lives_p1, lives_p2):
    # Score in the center-top
    score_text = self.medium_font.render(f"Score: {score}", True, TEXT_COLOR)
    score_rect = score_text.get_rect()
    score_rect.midtop = (SCREEN_WIDTH // 2, self.padding)
    screen.blit(score_text, score_rect)

    # Player 1 lives (bottom-left)
    p1_lives_text = self.medium_font.render(f"P1: {lives_p1}", True, PLAYER_COLOR)
    p1_lives_rect = p1_lives_text.get_rect()
    p1_lives_rect.bottomleft = (self.padding, SCREEN_HEIGHT - self.padding)
    screen.blit(p1_lives_text, p1_lives_rect)

    # Player 2 lives (bottom-right)
    p2_lives_text = self.medium_font.render(f"P2: {lives_p2}", True, PLAYER2_COLOR)
    p2_lives_rect = p2_lives_text.get_rect()
    p2_lives_rect.bottomright = (SCREEN_WIDTH - self.padding, SCREEN_HEIGHT - self.padding)
    screen.blit(p2_lives_text, p2_lives_rect)
```

Then update the call in `game_engine.py`'s `render()` method:
```python
self.hud.draw(screen, self.score_service.get_current_score(),
              self.player.lives, self.player2.lives)
```

## Testing Your Multiplayer Game

### Test Checklist
- [ ] Both players can move independently
- [ ] Both players can shoot independently
- [ ] Player 1 uses arrow keys + spacebar
- [ ] Player 2 uses WASD + left shift
- [ ] Both players' bullets destroy enemies
- [ ] Both players take damage from enemies
- [ ] Both players' lives are displayed correctly
- [ ] Score increases regardless of which player gets the kill
- [ ] Game ends when appropriate (based on your chosen condition)
- [ ] Players can't shoot each other (friendly fire is disabled)

### Common Issues

**Problem:** Player 2 shoots downward but Player 1 shoots upward
**Solution:** Make Player 2's `shoot()` method return a projectile with positive Y velocity:

In `entities/player.py`, you could add a parameter:
```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color=PLAYER_COLOR, shoot_direction=-1):
        # ... existing code ...
        self.shoot_direction = shoot_direction

    def shoot(self):
        # ... existing code ...
        projectile = Projectile(bullet_x, bullet_y, 0,
                               PROJECTILE_SPEED * self.shoot_direction)
        # ...
```

Then create Player 2 with `shoot_direction=1`:
```python
self.player2 = Player(start_x2, start_y2, PLAYER2_COLOR, shoot_direction=1)
```

**Problem:** Controls feel cramped on one keyboard
**Solution:** This is normal! Local multiplayer on keyboard is cozy. Consider:
- Using game controllers (requires pygame.joystick)
- One player using mouse clicks to shoot
- Different key layouts (Player 1: WASD, Player 2: Arrow keys)

## Optional Enhancements

### Co-op Power-ups
- Shared score (already implemented if you followed the guide)
- Power-ups that affect both players
- Revive system (one player can revive the other)

### Versus Mode
- Players compete for score
- Separate score tracking
- Enemies give points only to the player who kills them

### Different Ship Abilities
- Player 1 has fast shooting, Player 2 has powerful shots
- Encourages teamwork and different play styles

## Summary

To add 2-player mode:
1. ✅ Add Player 2 in game engine `__init__`
2. ✅ Modify input service to return two input states
3. ✅ Update both players in `update()`
4. ✅ Handle shooting for both players
5. ✅ Check collisions for both players
6. ✅ Decide on game over condition
7. ✅ Update HUD to show both players' lives
8. ✅ Test thoroughly!

The code is already structured to make this easier - look for the TODO comments about multiplayer throughout the codebase!

Good luck, and have fun playing with a friend! 🎮
