import pygame
import constants
from constants import *


blue_bird_frames = [constants.bluebird_f_1,
                    constants.bluebird_f_2, constants.bluebird_f_3]

red_bird_frames = [constants.redbird_f_1,
                   constants.redbird_f_2, constants.redbird_f_3]

yellow_bird_frames = [constants.yellowbird_f_1,
                      constants.yellowbird_f_2, constants.yellowbird_f_3]


bird_animate_frame_index = 0
bird_animate_frames = blue_bird_frames
bird = bird_animate_frames[bird_animate_frame_index]
bird_rect = bird.get_rect(center=(100, WIDTH/2))
