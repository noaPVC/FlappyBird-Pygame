# BTNS IN UI
import pygame
import os

BTN_SIZE = 100
BTN_SMALL_SIZE = 60

home = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'home.png')), (BTN_SIZE, BTN_SIZE))
home_hover = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'home_hover.png')), (BTN_SIZE, BTN_SIZE))

play = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'play.png')), (150, 150))
play_hover = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'play_hover.png')), (150, 150))

restart = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'restart.png')), (BTN_SIZE, BTN_SIZE))
restart_hover = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'restart_hover.png')), (BTN_SIZE, BTN_SIZE))


# btns home small

settings = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'settings.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))
settings_hover = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'settings_hover.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))

help_btn = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'help.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))
help_btn_hover = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'help_hover.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))

exit_game = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'exit.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))
exit_game_hover = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'exit_hover.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))

back = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'back.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))
back_hover = pygame.transform.scale(pygame.image.load(
    os.path.join('vis/assets/btns', 'back_hover.png')), (BTN_SMALL_SIZE, BTN_SMALL_SIZE))


# VOLUME

volume = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'volume.png')), (50, 50))

volume_off = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'volume_off.png')), (50, 50))


music = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'music.png')), (50, 50))

music_off = pygame.transform.scale(pygame.image.load(os.path.join(
    'vis/assets/btns', 'music_off.png')), (50, 50))


# external buttons/other style

# used to reset the highscore
reset = pygame.image.load(
    os.path.join('vis/assets/btns', 'reset.png'))
reset_hover = pygame.image.load(
    os.path.join('vis/assets/btns', 'reset_hover.png'))