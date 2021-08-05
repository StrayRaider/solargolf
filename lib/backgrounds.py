import random

STARCOUNT = 100
STAR_RADIUS = (1,3)
STAR_COLOR = (50,255)

def get_stars(width,height):
    stars_list = []
    for i in range(0,STARCOUNT):
        #yıldızz konum oluştur
        x = random.randint(0,width)
        y = random.randint(0,height)
        #yarıçap
        radius = random.randint(*STAR_RADIUS)
        #renk
        color = random.randint(*STAR_COLOR)
        color = (color,color,color)
        stars_list.append([x,y,radius,color])
    
    return stars_list