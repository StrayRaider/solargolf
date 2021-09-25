import pygame
from pygame import gfxdraw
from sglib import settings

class Blackhole():
    def __init__(self,location,radius):
        self.scl_fac =  settings.scale_factor()[0]
        self.location = (int(location[0]* self.scl_fac), int(location[1]* self.scl_fac))
        self.radius = int(radius * self.scl_fac)
        self.orbit = radius*2
        self.g_field = radius*3
        self.img_loc = "./assets/blackholes/blackhole_1.png"
        self.black_h_img = pygame.image.load(self.img_loc)
        self.black_h_img = pygame.transform.scale(self.black_h_img, (self.orbit, self.orbit))
        
    def draw_black_h(self,SCREEN):
        color = (255,255,255)
        SCREEN.blit(self.black_h_img, (self.location[0]-self.radius, self.location[1]-self.radius))
        #gfxdraw.aacircle(SCREEN, *self.location, self.radius, color)

    def gravity_field_b_h(self,SCREEN):
        color = (255, 255, 255)
        gfxdraw.aacircle(SCREEN, *self.location, int(self.g_field), color)
    