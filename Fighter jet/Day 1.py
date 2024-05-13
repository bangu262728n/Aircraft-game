import random
import pygame
import pygame.display

pygame.init()
SCREEN=WIDTH,HEIGHT=288,512
info=pygame.display.Info()
width=info.current_w
height=info.current_h
if width>=height:
    win=pygame.display.set_mode(SCREEN,pygame.NOFRAME)
else:
    win=pygame.display.set_mode(SCREEN,pygame.N0FRAME|pygame.SCALED|pygame.FULLSCREEN)
clock=pygame.time.Clock()
FPS=60
WHITE=(255,255,255)
BLUE=(30,144,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,20)