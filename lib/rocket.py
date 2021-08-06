import pygame, math, os

class Rocket():
    def __init__(self,planet):
        self.planet = planet
        self.vector = (1,1)
        self.angle = 0
        self.rotate_angle = 2
        self.rocket_direction = 0#0 saat tersi 1 saat yonu
        self.rocket_imgs = [pygame.image.load(os.path.join("assets","rockets","1.png")),
                            pygame.image.load(os.path.join("assets","rockets","2.png")),
                            pygame.image.load(os.path.join("assets","rockets","3.png"))]
        self.active_rocket_state = 0
        self.active_rocket = self.rocket_imgs[self.active_rocket_state]
        self.update_planet_location()

    def draw_rocket(self,SCREEN):
        SCREEN.blit(self.active_rocket,self.location)

    def update_rocket(self):
        if self.planet:
            if self.rocket_direction:
                self.angle -= self.rotate_angle
            else:
                self.angle += self.rotate_angle
            self.active_rocket = pygame.transform.rotate(self.rocket_imgs[self.active_rocket_state], self.angle)
            self.update_planet_location()
        else:
            self.location = (self.location[0]+self.vector[0],self.location[1]+self.vector[1])

    def update_planet_location(self):
        x = math.sin(math.radians(self.angle)) * self.planet.orbit
        y = math.cos(math.radians(self.angle)) * self.planet.orbit
        image_center = self.active_rocket.get_rect().center
        self.location = (self.planet.location[0]-x-image_center[0],
                         self.planet.location[1]-y-image_center[1])

    def remove_planet(self):
        if self.planet:
            self.planet = False
            x = math.cos(math.radians(self.angle)) * 2
            y = math.sin(math.radians(self.angle)) * 2
            if self.rocket_direction:
                self.vector = (x,-y)
            else:
                self.vector = (-x,y)

    def rocket_in_planet(self,planets):
        for planet in planets:
            image_center = self.active_rocket.get_rect().center
            image_center = (self.location[0]+image_center[0],self.location[1]+image_center[1])
            distance = math.sqrt((image_center[0]-planet.location[0])**2+(image_center[1]-planet.location[1])**2)
            if distance > planet.g_field:
                continue
            elif distance > planet.orbit:
                x = (planet.location[0]-image_center[0])*0.0001
                y = (planet.location[1]-image_center[1])*0.0001
                self.vector = (self.vector[0]+x,self.vector[1]+y)
            else:
                self.planet = planet
