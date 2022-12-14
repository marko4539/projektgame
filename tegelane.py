import time
import pygame, sys
clock = pygame.time.Clock()
FPS=30
class Tegelane():
    def __init__(self, image, pos, text_input, font, color):
        self.image=image
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.color=color
        self.text_input = text_input
        self.text= self.font.render(self.text_input, True, self.color)
        self.täringjäänud=0
        if self.image is None:
            self.image=self.text
        self.rect = self.image.get_rect(midbottom=(self.x_pos, self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos, self.y_pos-60))
    
    def update(self, screen):
        self.rect = self.image.get_rect(midbottom=(self.x_pos, self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos, self.y_pos-60))
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    def täringlisa(self,väärtus):
        self.täringjäänud+= väärtus
#     def liikumine(self, uuspos, screen):
#         pos=(self.x_pos,self.y_pos)
#         posvektor=(uuspos[0]-pos[0],uuspos[1]-pos[1])
#         for i in range(10):
#             self.x_pos+=posvektor[0]/10
#             self.y_pos+=posvektor[1]/10
#             self.update(screen)
#         self.täringjäänud-=1
        
    