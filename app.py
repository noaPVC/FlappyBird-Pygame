import pygame
from pygame import mixer
from os import path
import sys
import random


# files
import constants
from constants import *
import const_btns
from bird_vars import *

dir_current = path.dirname(__file__)
FPS = 60
WIDTH, HEIGHT = 577, 780
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FlappyBird")
icon = constants.frame_icon.convert_alpha()
pygame.display.set_icon(icon)

home_screen = True
game_run = False
settings = False
help_screen = False
play_sound = False

volume = True
music = True

score = 0
gravitation = 0.25
bird_move = 0
score = 0

# global vars used in game

currentBG = constants.BG_NIGHT.convert_alpha()
currentPipe = constants.GREEN_PIPE.convert_alpha()

# loading our data here as alike currency or scores


def load_data():
    global highscore
    # load highscore
    with open(path.join(dir_current, "saved.txt"), "r") as f:
        highscore = int(f.read())


load_data()


clock = pygame.time.Clock()
x_pos_floor = 0

ANIMATEBIRD = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATEBIRD, 200)

list_of_pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1600)


# FUNCTIONS
def draw_bg():
    WIN.blit(currentBG, (0, 0))

def draw_floor():
    global x_pos_floor
    x_pos_floor -= 1
    WIN.blit(constants.base_img.convert_alpha(), (x_pos_floor, 700))
    WIN.blit(constants.base_img.convert_alpha(), (x_pos_floor + WIDTH, 700))
    if x_pos_floor <= -WIDTH:
        x_pos_floor = 0


pipe_heights = [370, 400, 300, 500]

def create_pipes():
    rand_pipe_pos = random.choice(pipe_heights)

    new_bottom_pipe = currentPipe.get_rect(midtop=(650, rand_pipe_pos))
    new_top_pipe = currentPipe.get_rect(midbottom=(650, rand_pipe_pos - 250))
    return new_bottom_pipe, new_top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5

    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= WIDTH:
            WIN.blit(currentPipe, pipe)
        else:
            reversed_pipe = pygame.transform.flip(currentPipe, False, True)
            WIN.blit(reversed_pipe, pipe)


def remove_pipes_crossed():
    if list_of_pipes:
        for pipe in list_of_pipes:
            if pipe.centerx == 100:
                return True
    else:
        return False


def display_score_update_highscore():
    global highscore

    score_label = main_game_font.render(f"{score}", 1, WHITE)
    WIN.blit(score_label, (WIDTH / 2 - 50, 50))

    if score >= highscore:
        highscore = score
        with open(path.join(dir_current, "saved.txt"), "w") as f:
            f.write(str(score))


def destroy_pipe(pipes):
    # destroying the pipes when they leave the screen
    for pipe in list_of_pipes:
        if pipe.centerx <= -100:
            list_of_pipes.remove(pipe)


def check_collide(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= HEIGHT - 100:
        return False

    return True


def rotate_bird(bird_surface):
    new_bird = pygame.transform.rotate(bird_surface, -bird_move * 3)
    return new_bird


def init_new_game():
    global list_of_pipes, game_run, bird_move, bird_rect, score

    game_run = True
    list_of_pipes.clear()
    bird_move = 0
    bird_rect = bird.get_rect(center=(100, -50))
    score = 0


def animate_bird():
    new_bird = bird_animate_frames[bird_animate_frame_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))

    return new_bird, new_bird_rect


def draw_gameover_screen():

    draw_bg()
    draw_floor()

    WIN.blit(constants.gameover_img.convert_alpha(), (WIDTH / 2 - 195, 70))

    info_restart_label = info_font.render(
        "Or just press the spacebar to restart the game.", 1, WHITE
    )

    score_label = regular_font.render(f"Score:  {score}", 1, WHITE)
    highscore_label = regular_font.render(f"Highscore:  {highscore}", 1, WHITE)

    # BTNS returning a specific state each we can detect what scene we display
    if mouseOver(WIDTH / 2 - 130, 200, BTN_SIZE, BTN_SIZE):
        currentRestart = const_btns.restart_hover
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return 1  # start game
    else:
        currentRestart = const_btns.restart

    if mouseOver(WIDTH / 2 + 20, 200, BTN_SIZE, BTN_SIZE):
        currentHome = const_btns.home_hover
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 2  # home menu
    else:
        currentHome = const_btns.home

    WIN.blit(currentRestart, (WIDTH / 2 - 130, 200))
    WIN.blit(currentHome, (WIDTH / 2 + 20, 200))
    WIN.blit(info_restart_label, (16, HEIGHT - 120))
    WIN.blit(score_label, (WIDTH / 2 - 70, 360))
    WIN.blit(highscore_label, (WIDTH / 2 - 105, 410))


def draw_home_screen():
    global settings
    global help_screen
    global volume
    global music
    global highscore

    if volume:
        currentVolume = const_btns.volume
    else:
        currentVolume = const_btns.volume_off

    if music:
        currentMusic = const_btns.music
    else:
        currentMusic = const_btns.music_off

    if not settings and not help_screen:
        draw_bg()
        mouseOver(WIDTH / 2 - 90, 250, 150, 150)

        if (
            mx >= WIDTH / 2 - 90
            and mx <= WIDTH / 2 - 90 + 150
            and my >= 250
            and my <= 250 + 150
        ):
            currentPlay = const_btns.play_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 1
        else:
            currentPlay = const_btns.play

        # SETTINGS BTN
        if mouseOver(10, HEIGHT - 70, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            currentSettings = const_btns.settings_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    settings = True
        else:
            currentSettings = const_btns.settings

        # HELP INFO
        if mouseOver(10, HEIGHT - 140, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            currentHelp = const_btns.help_btn_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    help_screen = True
        else:
            currentHelp = const_btns.help_btn

        # EXIT GAME
        if mouseOver(WIDTH - 70, HEIGHT - 70, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            currentExit = const_btns.exit_game_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
        else:
            currentExit = const_btns.exit_game

        highscore_label = regular_font.render("Highscore", 1, WHITE)
        highscore_int_label = big_font.render(str(highscore), 1, WHITE)

        if highscore > 0:
            WIN.blit(highscore_label, (WIDTH / 2 - 100, 620))
            if highscore > 9:  # just for designing purposes
                WIN.blit(highscore_int_label, (WIDTH / 2 - 50, 665))
            else:
                WIN.blit(highscore_int_label, (WIDTH / 2 - 30, 665))

        WIN.blit(currentExit, (WIDTH - 70, HEIGHT - 70))
        WIN.blit(currentHelp, (10, HEIGHT - 140))
        WIN.blit(currentSettings, (10, HEIGHT - 70))
        WIN.blit(constants.title_img, (WIDTH / 2 - 195, 70))
        WIN.blit(currentPlay, (WIDTH / 2 - 90, 250))

    elif settings:
        draw_bg()

        if mouseOver(10, 10, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            currentBack = const_btns.back_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    settings = False
        else:
            currentBack = const_btns.back

        settings_title = settings_title_font.render("Settings", 1, WHITE)
        music_label = settings_font.render("MUSIC", 1, WHITE)
        sfx_label = settings_font.render("SFX", 1, WHITE)

        if mouseOver(300, 395, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if currentVolume == const_btns.volume:
                        currentVolume = const_btns.volume_off
                        volume = False
                    elif currentVolume == const_btns.volume_off:
                        currentVolume = const_btns.volume
                        volume = True
        else:
            if currentVolume == const_btns.volume:
                currentVolume = const_btns.volume
            else:
                currentVolume = const_btns.volume_off

        if mouseOver(300, 295, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if currentMusic == const_btns.music:
                        currentMusic = const_btns.music_off
                        music = False
                        pygame.mixer.fadeout(6)
                        mixer.music.set_volume(0)
                    elif currentMusic == const_btns.music_off:
                        currentMusic = const_btns.music
                        music = True
                        mixer.music.set_volume(0.3)
        else:
            if currentMusic == const_btns.music:
                currentMusic = const_btns.music
            else:
                currentMusic = const_btns.music_off

        #

        if mouseOver(135, 650, 204, 80):
            currentReset = const_btns.reset_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    with open(path.join(dir_current, "saved.txt"), "w") as f:
                        f.write("0")
                        highscore = 0
        else:
            currentReset = const_btns.reset

        WIN.blit(currentReset, (135, 650))
        WIN.blit(currentMusic, (300, 295))
        WIN.blit(currentVolume, (300, 395))
        WIN.blit(music_label, (130, 300))
        WIN.blit(sfx_label, (130, 400))
        WIN.blit(settings_title, (140, 10))
        WIN.blit(currentBack, (10, 10))

    else:

        draw_bg()

        if mouseOver(10, 10, BTN_SMALL_SIZE, BTN_SMALL_SIZE):
            currentBack = const_btns.back_hover
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    help_screen = False
        else:
            currentBack = const_btns.back

        WIN.blit(constants.help_title.convert_alpha(), (105, 10))
        WIN.blit(constants.tap_img.convert_alpha(), (40, 170))
        WIN.blit(constants.txt1.convert_alpha(), (180, 200))
        WIN.blit(constants.collision_sign.convert_alpha(), (20, 560))
        WIN.blit(constants.txt2.convert_alpha(), (180, 550))
        WIN.blit(currentBack.convert_alpha(), (10, 10))


def play_audio(sfx, theme):
    global volume
    global music

    if sfx != None:
        sfx.set_volume(0.3)

    if volume and play_sound:
        if sfx == constants.point_sfx:
            constants.point_sfx.play()
        elif sfx == constants.swooshing_sfx:
            constants.swooshing_sfx.play()
        elif sfx == constants.wing_sfx:
            constants.wing_sfx.play()
        elif sfx == None:
            pass

    if music:
        if theme == "theme":
            mixer.music.set_volume(0.3)
            mixer.music.play(-1)
        elif theme == None:
            pass


def set_bird(color):

    if color == "red":
        return red_bird_frames
    elif color == "blue":
        return blue_bird_frames
    elif color == "yellow":
        return yellow_bird_frames
    else:
        return bird_animate_frames


def mouseOver(x, y, width, height):
    if mx >= x and mx <= x + width and my >= y and my <= y + height:
        return True
    else:
        return False


play_audio(None, "theme")

# game
while True:
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SPAWNPIPE and game_run:
            list_of_pipes.extend(create_pipes())
        elif event.type == ANIMATEBIRD and game_run:
            if bird_animate_frame_index < 2:
                bird_animate_frame_index += 1
            else:
                bird_animate_frame_index = 0

            bird, bird_rect = animate_bird()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_run:
                play_audio(constants.wing_sfx, None)
                bird_move = 0
                bird_move -= 9
            elif event.key == pygame.K_SPACE and not game_run:
                play_audio(constants.swooshing_sfx, None)
                init_new_game()

    # SCENE MANAGEMENT
    if home_screen:
        play_sound = False
        if draw_home_screen() == 1:
            home_screen = False
            init_new_game()

    elif game_run:
        play_sound = True
        draw_bg()

        bird_move += gravitation
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_move

        WIN.blit(rotated_bird, bird_rect)

        game_run = check_collide(list_of_pipes)
        list_of_pipes = move_pipes(list_of_pipes)
        draw_pipes(list_of_pipes)

        if remove_pipes_crossed():
            score += 1
            play_audio(constants.point_sfx, None)

        display_score_update_highscore()

        destroy_pipe(list_of_pipes)

        draw_floor()

    else:
        if draw_gameover_screen() == 1:
            init_new_game()
        elif draw_gameover_screen() == 2:
            home_screen = True

    pygame.display.update()
    clock.tick(FPS)
