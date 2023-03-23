import pygame
import os

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

pygame.mixer.init()

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
UMBRELLA_TYPE = "umbrella"

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/Game-Over.jpg"))

SPACE_BAR =  [
    pygame.image.load(os.path.join(IMG_DIR, "Other/SpaceBar.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/SpaceBar2.png"))
]

MENUBG = pygame.image.load(os.path.join(IMG_DIR, "Other/menuBG.png"))

DINO_CRY = pygame.image.load(os.path.join(IMG_DIR, "Other/cry_dino.png"))


RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png"))
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png"))
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png"))
]

RUNNING_UMBRELLA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Umbrella.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Umbrella.png"))
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_UMBRELLA = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpUmbrella.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png"))
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png"))
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png"))
]
DUCKING_UMBRELLA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Umbrella.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Umbrella.png"))
]
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

METEOR = [
    pygame.image.load(os.path.join(IMG_DIR, "meteoro/meteoro.jpeg")),
    pygame.image.load(os.path.join(IMG_DIR, "meteoro/meteoro2.jpeg")),
    ]
SONGS = [
    pygame.mixer.Sound(os.path.join(IMG_DIR, "song/more_100.wav")),
    pygame.mixer.Sound(os.path.join(IMG_DIR, "song/jump_dino.wav")),
    pygame.mixer.Sound(os.path.join(IMG_DIR, "song/dinoDie.wav")),
    pygame.mixer.music.load(os.path.join(IMG_DIR, "song/soundtrack.ogg")),
    pygame.mixer.Sound(os.path.join(IMG_DIR, "song/explode.wav"))
]

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
UMBRELLA = pygame.image.load(os.path.join(IMG_DIR, 'Other/Umbrella.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

DEFAULT_TYPE = "default"
