import pygame
from pygame import gfxdraw

class Blackhole():
    def __init__(self,location,radius):
        self.location = location
        self.radius = radius
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
    