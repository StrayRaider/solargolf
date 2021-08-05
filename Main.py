import pygame, sys
from pygame import gfxdraw
from lib import backgrounds


WIDTH = 1280
HEIGHT = 720
FPS = 60
FPSCLOCK = pygame.time.Clock()

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
STARS = backgrounds.get_stars(WIDTH,HEIGHT)

def update():
    pass

def draw():
    #zemin
    SCREEN.fill((0, 0, 0))
    #yildizlar
    for star in STARS:
        gfxdraw.filled_circle(SCREEN,*star)
        gfxdraw.aacircle(SCREEN,*star)

#oyun dongusu
while True:
    #tuş eventleri
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update()
    draw()
    
    pygame.display.flip()
    FPSCLOCK.tick(FPS)