import pygame, sys, os
from pygame import gfxdraw
from sglib import backgrounds, lvls, rocket, buttons, blackhole

max_lvl = 1

def read_write_maxlvl(r_or_w):
    global max_lvl
    home = os.path.expanduser("~")
    s_g_dir = os.path.join(home,".solargolf")
    s_g_conf = os.path.join(s_g_dir,"config")
    if not os.path.exists(s_g_dir):
        os.makedirs(s_g_dir)
    if r_or_w == "r":
        if os.path.exists(s_g_conf):
            f = open(s_g_conf,"r")
            readed = f.read()
            f.close()
            try:
                max_lvl = int(readed)
                if max_lvl > list(reversed(list(lvls.lvls)))[0]:
                    max_lvl = 1
            except:
                max_lvl = 1

    elif r_or_w == "w":
        f = open(s_g_conf, "w")
        f.write(str(max_lvl))
        f.close()

read_write_maxlvl("r")
WIDTH = 1280
HEIGHT = 720
FPS = 60
FPSCLOCK = pygame.time.Clock()

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
STARS = backgrounds.get_stars(WIDTH,HEIGHT)
lvl_no = max_lvl
active_lvl = lvls.lvls[lvl_no]
rocket_ = rocket.Rocket(active_lvl["planets"][0])
passive_p = pygame.image.load("./assets/icons/progres_1.png")
active_p = pygame.image.load("./assets/icons/progres_2.png")
button_list = [buttons.Button("./assets/buttons/restart_1.png", (1150,10),50),
               buttons.Button("./assets/buttons/close_1.png", (1210,10),50),
               buttons.Button("./assets/buttons/left_1.png", (1000,10),50),
               buttons.Button("./assets/buttons/right_1.png", (1060,10),50)]
connect_aud = pygame.mixer.Sound("./assets/musics/connect.wav")
disconnect_aud = pygame.mixer.Sound("./assets/musics/disconnect.wav")
music = pygame.mixer.music.load("./assets/musics/m_1.wav")
pygame.mixer.music.play(-1)

def update():
    #Roketi guncelleyelim
    rocket_.update_rocket()
    if not rocket_.planet:
        is_connect = rocket_.rocket_in_planet(active_lvl["planets"])
        if is_connect:
            connect_aud.play()
        c = rocket_.rocket_in_black_h(active_lvl["blackhole"])
        if c:
            restart()
        
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
    x,y = (920,15)
    for say_2 in range(0, len(rocket_.scored_planets)):
        SCREEN.blit(active_p, (x, y))
        x -= 45
    for say in range(0,int(len(active_lvl["planets"])) - len(rocket_.scored_planets)):
        SCREEN.blit(passive_p, (x, y))
        x -= 45



    if len(rocket_.scored_planets) / len(active_lvl["planets"]) == 1:
        print("lvl over")
        lvl_up()

def lvl_up(arrow = False):
    global active_lvl, lvl_no, max_lvl
    if arrow:
        if max_lvl > lvl_no:
            lvl_no += 1
            connect_aud.play()
    else:
        lvl_no += 1
        if max_lvl < lvl_no:
            max_lvl = lvl_no
        if lvl_no > (list(reversed(list(lvls.lvls)))[0]):
            lvl_no -= 1
    active_lvl = lvls.lvls[lvl_no]
    restart()

def lvl_down():
    global active_lvl, lvl_no
    lvl_no -= 1
    connect_aud.play()
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
    for planet in active_lvl["planets"]:
        planet.draw_planet(SCREEN)
        #planet.gravity_field(SCREEN)
    #kara delik
    for black_h in active_lvl["blackhole"]:
        black_h.draw_black_h(SCREEN)
        #black_h.gravity_field_b_h(SCREEN)
    #roket
    rocket_.draw_rocket(SCREEN)
    #draw button list
    for buton_ in button_list:
        buton_.draw_button(SCREEN)
    #score
    draw_scor_table()

#yeniden başlat
def restart():
    if rocket_.planet != active_lvl["planets"][0]:
        print("restart")
        rocket_.planet = active_lvl["planets"][0]
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
            read_write_maxlvl("w")
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_list[1].isoverlap(pygame.mouse.get_pos()):
                pygame.quit()
                read_write_maxlvl("w")
                sys.exit()
            elif button_list[0].isoverlap(pygame.mouse.get_pos()):
                connect_aud.play()
                restart()
            elif button_list[2].isoverlap(pygame.mouse.get_pos()):
                if lvl_no != 1:
                    lvl_down()
                else:
                    print("ilk levelden geri gidemezsiniz")
            elif button_list[3].isoverlap(pygame.mouse.get_pos()):
                if lvl_no != list(reversed(list(lvls.lvls)))[0]:
                    lvl_up(True)
                else:
                    print("bu son level")
            else:
                if rocket_.remove_planet():
                    disconnect_aud.play()

    update()
    draw()
    rocket_.scor_count()
    is_dead()
    pygame.display.flip()
    FPSCLOCK.tick(FPS)
