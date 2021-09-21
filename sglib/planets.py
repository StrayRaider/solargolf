import random, pygame, os
from pygame import gfxdraw
from sglib import settings

class Planet():
    def __init__(self, location, radius):
        self.scl_fac =  settings.scale_factor()
        self.location = (int(location[0]* self.scl_fac), int(location[1]* self.scl_fac))
        self.radius = int(radius * self.scl_fac)
        self.orbit = self.radius*2
        self.g_field = self.radius*3
        planet_num = random.randint(1, 9)
        planet_img_loc = os.path.join(os.getcwd(),"assets","planets","{}.png".format(str(planet_num)))
        self.planet_img = pygame.image.load(planet_img_loc)
        self.planet_img = pygame.transform.scale(self.planet_img, (self.orbit, self.orbit))


    def draw_planet(self,SCREEN):
        color = (255,255,255)
        SCREEN.blit(self.planet_img, (self.location[0]-self.radius, self.location[1]-self.radius))
        gfxdraw.aacircle(SCREEN, *self.location, self.orbit, color)

    def gravity_field(self,SCREEN):
        color = (255, 255, 255)
        gfxdraw.aacircle(SCREEN, *self.location, int(self.g_field), color)