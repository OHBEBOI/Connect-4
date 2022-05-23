# importing modules
import sys
import pygame as pg
from pygame.locals import *

# initialising pg
pg.init()

#Defining basic parameters of the program such as the window size and name
SCR_SIZE = (1280, 700)
SCR = pg.display.set_mode(SCR_SIZE)
pg.display.set_caption("pygame ")

#limiting the FPS of the window
FramePerSec = pg.time.Clock()
FPS = 60

#Sprites


#main game loop
while True:
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    FramePerSec.tick(FPS)
