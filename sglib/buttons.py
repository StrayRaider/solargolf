import pygame

class Button():
    def __init__(self,img,but_loc,size):
        self.location = but_loc
        self.img = img
        self.size = size

    def draw_button(self,SCREEN):
        SCREEN.blit(self.img,self.location)
    #cursor ve button üst üste mi
    def isoverlap(self,mouse_loc):
        if mouse_loc[0] > self.location[0] and mouse_loc[0] < self.location[0] + self.size and mouse_loc[1] > self.location[1] and mouse_loc[1] < self.location[1] + self.size:
            pass