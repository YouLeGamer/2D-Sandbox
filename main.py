import scripts.random_things as rt
from classes.inventory import *
from classes.advancements import Advancements
from objects.player import *
from objects.weapon import *
from other.settings import *
from classes.image import *
import pygame
import time
import os

# Init pygame
pygame.init()

game_version = "- Classic 23w14"

screen_size = (800, 600)
screen_color = (0, 0, 0)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("2D Sandbox Game " + game_version)

# GAME LOOP -----------------------------------------------------------------------------------------

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False