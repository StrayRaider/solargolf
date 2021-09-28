import pygame, random, math
from pygame import gfxdraw
#her eksen içi 2 drum var 1. si 0,0 ın solunda 3. sağında
#bunu random ile belirliycez 1 ise solda 2 ise sağda
#eğer soldaysa x için vector x pozitif sağdaydsa nrgstif ve vector büyüklükleri random belirlenicek

class Meteor():
    def __init__(self,scl_fac,comp_sizes):
        self.comp_sizes = comp_sizes
        self.scl_fac = scl_fac
        self.size = random.randint(2,5)
        self.size = int(self.size * self.scl_fac)
        self.orbit = self.size*2
        
    #meteor çiz
    def draw_met(self,SCREEN):
        color = (255,255,255)
        gfxdraw.aacircle(SCREEN, *self.location, self.orbit, color)
        pygame.draw.circle(SCREEN,color,self.location,self.orbit)
    def update_met(self):
        self.location = (int(self.location[0]+self.vector[0]),int(self.location[1]+self.vector[1]))

    def loc_and_vec(self):
        s_x_loc = random.randint(1,4) # 1 solda 2 sağda kalır
        s_y_loc = random.randint(1,2)
        self.size = random.randint(2,5)
        self.size = int(self.size * self.scl_fac)
        self.orbit = self.size*2
        print(s_x_loc)
    
        if s_x_loc == 1:
            x_loc = random.randint(5,10)
            x_vec = random.randint(2,4)
            y_loc = random.randint(5,self.comp_sizes[1])
        elif s_x_loc == 2:
            x_loc = random.randint(self.comp_sizes[0]-10 ,self.comp_sizes[0])
            x_vec = random.randint(-4,-2)
            y_loc = random.randint(5,self.comp_sizes[1])
        elif s_x_loc == 3:
            x_loc = random.randint(0, self.comp_sizes[0])
            x_vec = random.randint(2,4)
            y_loc = random.randint(5,10)
        elif s_x_loc == 4:
            x_loc = random.randint(0, self.comp_sizes[0])
            x_vec = random.randint(-4,-2)
            y_loc = random.randint(self.comp_sizes[1]-10 ,self.comp_sizes[1])

        if s_y_loc == 1:
            y_vec = random.randint(2,4)
        else:
            y_vec = random.randint(-4,-2)
        self.location = (int(x_loc*self.scl_fac) ,int(y_loc*self.scl_fac))
        self.vector = (int(x_vec*self.scl_fac) ,int(y_vec*self.scl_fac))
        
    def met_in_planet(self,planets):
        for planet in planets:
            image_center = self.location
            distance = (math.sqrt((image_center[0]-planet.location[0])**2+(image_center[1]-planet.location[1])**2))
            if distance > planet.g_field:
                continue
            elif distance > planet.orbit/2:
                x = (planet.location[0]-image_center[0])*0.0001 *self.scl_fac
                y = (planet.location[1]-image_center[1])*0.0001 *self.scl_fac
                self.vector = (self.vector[0]+x,self.vector[1]+y)
            else:
                return True #meteor yok edilir
            return False
            