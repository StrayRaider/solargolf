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
        self.rotate_rocket_imgs = []
        for rocket_img in self.rocket_imgs:
            self.rotate_rocket_imgs.append(pygame.transform.rotate(rocket_img, 180))
        self.active_rocket_state = 0
        self.active_rocket = self.rocket_imgs[self.active_rocket_state]
        self.update_planet_location()
        self.scored_planets = []

    def draw_rocket(self,SCREEN):
        SCREEN.blit(self.active_rocket,self.location)

    def update_rocket(self):
        if self.planet:
            if self.rocket_direction:
                self.angle -= self.rotate_angle
            else:
                self.angle += self.rotate_angle
            if self.rocket_direction:
                self.active_rocket = pygame.transform.rotate(self.rotate_rocket_imgs[self.active_rocket_state], self.angle)
            else:
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
                return False
            else:
                self.planet = planet
                self.scor_count()
                x = (planet.location[0] - image_center[0])
                y = (planet.location[1] - image_center[1])
                self.angle = self.coordinat_to_angle(x,y)

                x = self.vector[0]
                y = self.vector[1]
                rocket_angle = self.coordinat_to_angle(x,y)
                if rocket_angle > self.angle:
                    self.rocket_direction = 1
                else:
                    self.rocket_direction = 0
                return True

    def rocket_in_black_h(self,black_holes):
        for black_h in black_holes:
            image_center = self.active_rocket.get_rect().center
            image_center = (self.location[0]+image_center[0],self.location[1]+image_center[1])
            distance = math.sqrt((image_center[0]-black_h.location[0])**2+(image_center[1]-black_h.location[1])**2)
            if distance > black_h.g_field:
                continue
            elif distance > black_h.radius:
                x = (black_h.location[0]-image_center[0])*0.0001
                y = (black_h.location[1]-image_center[1])*0.0001
                self.vector = (self.vector[0]+x,self.vector[1]+y)

            else:
                print("dead")
                return True
            return False

    def coordinat_to_angle(self,x,y):
        if x > 0 and y > 0:
            add_angle = 0
        elif x > 0 and y < 0:
            add_angle = 270
        elif x < 0 and y > 0:
            add_angle = 90
        elif x < 0 and y < 0:
            add_angle = 180
        angle = math.atan(y/x)
        if angle < 0:
            add_angle += 90
        angle = 360 - angle
        return int(math.degrees(angle)+add_angle) % 360
        
    def scor_count(self):
        if self.planet not in self.scored_planets and self.planet:
            self.scored_planets.append(self.planet)

