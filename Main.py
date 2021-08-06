import pygame, sys
from pygame import gfxdraw
from lib import backgrounds, lvls, rocket


WIDTH = 1280
HEIGHT = 720
FPS = 60
FPSCLOCK = pygame.time.Clock()

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
STARS = backgrounds.get_stars(WIDTH,HEIGHT)

active_lvl = lvls.lvls["1"]
rocket_ = rocket.Rocket(active_lvl[1])

def update():
    #Roketi guncelleyelim
    rocket_.update_rocket()

def draw():
    #zemin
    SCREEN.fill((0, 0, 0))
    #yildizlar
    for star in STARS:
        gfxdraw.filled_circle(SCREEN,*star)
        gfxdraw.aacircle(SCREEN,*star)
    #Gezegenler
    for planet in active_lvl:
        planet.draw_planet(SCREEN)
    #roket
    rocket_.draw_rocket(SCREEN)

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