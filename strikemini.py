#initialize the game
import pygame
from helpers import *
from playerA import Player1
from playerB import Player2
from bomb import Bomb


# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#create the background/map