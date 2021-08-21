import pygame, sys
from pygame import gfxdraw
from sglib import backgrounds, lvls, rocket, buttons


WIDTH = 1280
HEIGHT = 720
FPS = 60
FPSCLOCK = pygame.time.Clock()

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
STARS = backgrounds.get_stars(WIDTH,HEIGHT)

active_lvl = lvls.lvls["1"]
rocket_ = rocket.Rocket(active_lvl[1])
#buton işleri
restart_img_load = pygame.image.load("./assets/buttons/restart_1.png")
close_img_load = pygame.image.load("./assets/buttons/close_1.png")
#1.si restart 2. si close
button_list = [buttons.Button(restart_img_load, (800,500),100),buttons.Button(close_img_load, (900,500),100)]

def update():
    #Roketi guncelleyelim
    rocket_.update_rocket()
    if not rocket_.planet:
        rocket_.rocket_in_planet(active_lvl)
#ölüm kontrol
def is_dead():
    x,y = rocket_.location
    if x < 0 or x > WIDTH:
        print("dead")
        restart()
        
    elif y < 0 or y > HEIGHT:
        print("dead")
        restart()


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
        #planet.gravity_field(SCREEN)
    #roket
    rocket_.draw_rocket(SCREEN)
    #draw button list
    for buton_ in button_list:
        buton_.draw_button(SCREEN)
#yeniden başlat
def restart():
    if rocket_.planet != active_lvl[1]:
        print("restart")
        rocket_.planet = active_lvl[1]
        rocket_.angle = 0
        rocket_vector = (1,1)
        rocket_.rocket_direction = 0

#oyun dongusu
while True:
    #tuş eventleri
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_list[1].isoverlap(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()

            if button_list[0].isoverlap(pygame.mouse.get_pos()):
                restart()
            else:
                rocket_.remove_planet()

    update()
    draw()
    is_dead()

    pygame.display.flip()
    FPSCLOCK.tick(FPS)