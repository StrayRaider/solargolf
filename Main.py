import pygame, sys, os
from pygame import gfxdraw
from sglib import backgrounds, lvls, rocket, buttons, blackhole, settings

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


pygame.init()
scl_fac = settings.scale_factor()[0]
screen_ratio = pygame.display.Info()
#comp_sizes = (screen_ratio.current_w, screen_ratio.current_h)
comp_sizes = (1280, 720)

if settings.scale_factor()[1] == "x": # x büyük olan ise : x 
    WIDTH = int(1280*scl_fac)
    HEIGHT = comp_sizes[1]

elif settings.scale_factor()[1] == "y":
    WIDTH = int(1280*scl_fac)
    HEIGHT = int(720*scl_fac)

elif settings.scale_factor()[1] == "xy":
    WIDTH = int(1280*scl_fac)
    HEIGHT = int(720*scl_fac)

print(WIDTH,HEIGHT)
FPS = 60
FPSCLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
STARS = backgrounds.get_stars(WIDTH, HEIGHT, scl_fac)
lvl_no = max_lvl
active_lvl = lvls.lvls[lvl_no]
rocket_ = rocket.Rocket(active_lvl["planets"][0], scl_fac)
#passive_p = pygame.image.load("./assets/icons/progres_1.png")
#active_p = pygame.image.load("./assets/icons/progres_2.png")
active_p = pygame.transform.scale(pygame.image.load("./assets/icons/progres_2.png"),(int(40*scl_fac),int(40*scl_fac)))
passive_p = pygame.transform.scale(pygame.image.load("./assets/icons/progres_1.png"),(int(40*scl_fac),int(40*scl_fac)))


button_list = [buttons.Button("./assets/buttons/restart_1.png", (1150 , 10), 50),
               buttons.Button("./assets/buttons/close_1.png", (1210 , 10), 50),
               buttons.Button("./assets/buttons/left_1.png", (1000 , 10), 50),
               buttons.Button("./assets/buttons/right_1.png", (1060 , 10), 50),
               buttons.Button("./assets/buttons/free.png", (940 , 10), 50)]#sayı

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
    x,y = (int(860*scl_fac),int(15*scl_fac))
    for say_2 in range(0, len(rocket_.scored_planets)):
        SCREEN.blit(active_p, (x, y))
        x -= int(45*scl_fac)
    for say in range(0,int(len(active_lvl["planets"])) - len(rocket_.scored_planets)):
        SCREEN.blit(passive_p, (x, y))
        x -= int(45*scl_fac)



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
    # SAYI YAZ
    font = pygame.font.Font('freesansbold.ttf', int(45*scl_fac))
    text = font.render(str(lvl_no), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (int(964*scl_fac),int(38*scl_fac))
    SCREEN.blit(text, textRect)

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
                    print("ilk levelden geri gidemezsiniz") # açık olan son levele yönlendirilebilir
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

