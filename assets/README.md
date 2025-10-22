# Assets Folder

This folder is for game assets like images, sounds, and music.

## Current Status
Right now, the game uses simple colored rectangles drawn with Pygame. This works great for prototyping and learning!

## Adding Visual Assets

When you're ready to add custom graphics, you can place them here:

### Images
- `player.png` - Player spaceship sprite
- `enemy.png` - Enemy/asteroid sprite
- `bullet.png` - Projectile sprite
- `background.png` - Background image
- `heart.png` - Life/health icon

### Sounds
- `shoot.wav` - Shooting sound effect
- `explosion.wav` - Enemy destruction sound
- `hit.wav` - Player damage sound
- `music.mp3` - Background music

### Fonts
- `game_font.ttf` - Custom font for menus and HUD

## Where to Find Free Assets

### Sprite Graphics
- [OpenGameArt.org](https://opengameart.org/) - Huge collection of free game art
- [Kenney.nl](https://kenney.nl/assets) - High-quality free assets, lots of space themes!
- [itch.io](https://itch.io/game-assets/free) - Free and paid asset packs
- [Pixabay](https://pixabay.com/) - Free images and vectors

### Sound Effects
- [Freesound.org](https://freesound.org/) - Community-uploaded sound effects
- [OpenGameArt.org](https://opengameart.org/art-search-advanced?keys=&field_art_type_tid%5B%5D=13) - Sound effects section
- [Zapsplat](https://www.zapsplat.com/) - Free sound effects library
- [Bfxr](https://www.bfxr.net/) - Generate retro game sounds (online tool)

### Music
- [OpenGameArt.org](https://opengameart.org/art-search-advanced?keys=&field_art_type_tid%5B%5D=12) - Game music
- [Incompetech](https://incompetech.com/music/royalty-free/) - Kevin MacLeod's royalty-free music
- [FreePD](https://freepd.com/) - Public domain music

### Fonts
- [Google Fonts](https://fonts.google.com/) - Free fonts
- [DaFont](https://www.dafont.com/bitmap.php) - Lots of retro/pixel fonts

## How to Use Assets in Your Code

### Loading Images
```python
# In your entity class (e.g., player.py)
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load the image
        self.image = pygame.image.load("assets/player.png")
        # Optional: scale to desired size
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rect = self.image.get_rect()
        # ... rest of code
```

### Loading Sounds
```python
# In your game engine or entity
import pygame

# Load a sound effect
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")

# Play it when needed
shoot_sound.play()
```

### Loading Music
```python
# In your main.py
import pygame

pygame.mixer.init()
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.set_volume(0.5)  # 50% volume
pygame.mixer.music.play(-1)  # -1 means loop forever
```

### Loading Fonts
```python
# In your HUD or Menu class
import pygame

# Load a custom font
custom_font = pygame.font.Font("assets/game_font.ttf", 36)

# Use it to render text
text = custom_font.render("Score: 100", True, (255, 255, 255))
```

## File Format Notes

### Images
- **PNG** - Best for sprites (supports transparency)
- **JPG** - Good for backgrounds (no transparency, smaller file size)
- Recommended sizes: Keep sprites under 512x512 pixels for performance

### Sounds
- **WAV** - Uncompressed, best for short sound effects
- **OGG** - Compressed, good for longer sounds/music
- **MP3** - Also works, but OGG is preferred for games

### Fonts
- **TTF** - TrueType fonts, widely supported
- **OTF** - OpenType fonts, also works

## License Compliance

When using assets you didn't create:

1. **Check the license!** Make sure you're allowed to use it
2. **Give credit** - Most free assets require attribution
3. **Keep a list** - Document where each asset came from

You can track this in `docs/sprint-brief.md` under "Resources You Used"

## Creating Your Own Assets

Don't have art skills? No problem!

### Pixel Art Tools (beginner-friendly)
- [Piskel](https://www.piskelapp.com/) - Free online pixel art editor
- [Aseprite](https://www.aseprite.org/) - Professional tool ($20, but worth it)
- [GIMP](https://www.gimp.org/) - Free alternative to Photoshop

### Sound Creation
- [Bfxr](https://www.bfxr.net/) - Generate retro game sounds
- [ChipTone](https://sfbgames.itch.io/chiptone) - 8-bit sound generator
- [Audacity](https://www.audacityteam.org/) - Free audio editor

### Music Creation
- [BeepBox](https://www.beepbox.co/) - Browser-based chiptune maker
- [LMMS](https://lmms.io/) - Free music production software

## Tips for Beginners

1. **Start simple** - Colored rectangles work fine while you learn!
2. **Consistency matters** - If you use pixel art, use it for everything
3. **Size matters** - Keep file sizes reasonable (< 1MB per file)
4. **Test early** - Load one asset and test before adding many
5. **Backup** - Keep originals in case you need to edit later

Happy creating! 🎨🎵
