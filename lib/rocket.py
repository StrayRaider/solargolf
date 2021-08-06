import pygame, math

class Rocket():
    def __init__(self,planet):
        self.planet = planet
        self.vector = (0,0)
        self.angle = 90
        self.rotate_angle = 2
        self.rocket_imgs = [pygame.image.load("./assets/rockets/1.png"),
                            pygame.image.load("./assets/rockets/2.png"),
                            pygame.image.load("./assets/rockets/3.png")]
        self.active_rocket_state = 0
        self.active_rocket = self.rocket_imgs[self.active_rocket_state]
        self.update_location()

    def draw_rocket(self,SCREEN):
        SCREEN.blit(self.active_rocket,self.location)

    def update_rocket(self):
        if self.planet:
            self.angle += self.rotate_angle
            self.active_rocket =  pygame.transform.rotate(self.rocket_imgs[self.active_rocket_state], self.angle)
            self.update_planet_location()

    def update_planet_location(self):
        x = math.sin(math.radians(self.angle)) * self.planet.orbit
        y = math.cos(math.radians(self.angle)) * self.planet.orbit
        image_center = self.active_rocket.get_rect().center
        self.location = (self.planet.location[0]-x-image_center[0],
                         self.planet.location[1]-y-image_center[1])
    
        