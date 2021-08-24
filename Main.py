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
lvl_no = 5
active_lvl = lvls.lvls[lvl_no]
rocket_ = rocket.Rocket(active_lvl[0])
button_list = [buttons.Button("./assets/buttons/restart_1.png", (1150,10),50),buttons.Button("./assets/buttons/close_1.png", (1210,10),50)]

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

def draw_scor_table():
    print("\n" , rocket_.scored_planets)
    start_pos = (930,35)
    end_leght = len(rocket_.scored_planets)/len(active_lvl)*200
    pygame.draw.line(SCREEN,(255,255,255) ,(start_pos[0]-10,start_pos[1]), (start_pos[0]+210,start_pos[1]), 25)
    pygame.draw.line(SCREEN,(80,120,250) , start_pos, (start_pos[0]+end_leght,start_pos[1]), 15)
    if len(rocket_.scored_planets) / len(active_lvl) == 1:
        print("lvl over")
        lvl_change()
        
def lvl_change():
    global active_lvl, lvl_no
    lvl_no += 1
    active_lvl = lvls.lvls[lvl_no]
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
    #score
    draw_scor_table()

#yeniden başlat
def restart():
    if rocket_.planet != active_lvl[0]:
        print("restart")
        rocket_.planet = active_lvl[0]
        rocket_.angle = 0
        rocket_vector = (1,1)
        rocket_.rocket_direction = 0
        rocket_.scored_planets = []
        
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
    rocket_.scor_count()
    is_dead()
    pygame.display.flip()
    FPSCLOCK.tick(FPS)
