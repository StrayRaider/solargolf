import pygame

class Button():
    def __init__(self,img,SCREEN):
        self.img = img
        self.screen = SCREEN
        
    def buttondraw(self,x,y):
        self.screen.blit(self.img,(x,y))
        