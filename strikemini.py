#initialize the game
import pygame
from playerA import Player1
from playerB import Player2
from bomb import Bomb

def build_background(screen):

    # returns pygame surface that will be the background for the game

    # define each tile we will be using
    full_dirt = pygame.image.load('assets/ground_textures/')
    edge_dirt =
    wall_dirt =

    # get size and width of game screen

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # make a surface that will be the background

    bg = pygame.Surface((screen_width, screen_height))
    bg.fill (0,0,88)

    # get tile size

    # build matrix to define where all tiles go

    # define default value to pad the track with

    # loop over each piece of matrix and blit it to the surface

    # return the surface we made


# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#create the background/map