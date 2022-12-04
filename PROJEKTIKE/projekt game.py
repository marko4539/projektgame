import math
import time
import pygame, sys
from nupp import Nupp
pygame.init()

(width, height) = (768, 768)
screen = pygame.display.set_mode((width, height))
screen.fill("black")
bg = pygame.image.load("taust.png")
menubg = pygame.image.load("menüü.png")
bgscaled = pygame.transform.scale(bg, (768,768))
menubgscaled = pygame.transform.scale(menubg, (768,768))
clock = pygame.time.Clock()
FPS=30
game=True
def get_font(size):
    return pygame.font.Font("font.ttf", size)



def main_menu():
    pygame.display.set_caption('menu')
    screen.fill("black")
    while True:
        screen.blit(menubg, (0,0))
        m_mouse_pos = pygame.mouse.get_pos()
        mängunimi= get_font(30).render("Hauamäng", True, "#53493f")
        mängunimi4n=mängunimi.get_rect(center=(200, 200))
        screen.blit(mängunimi, mängunimi4n)
        mänginupp=Nupp(image=None, pos=(125,260),
                       text_input="mängi",
                       font=get_font(18),
                       base_color="#53493f",
                       hovering_color="White")
        äramänginupp=Nupp(image=None, pos=(160,290),
                       text_input="ära mängi",
                       font=get_font(18),
                       base_color="#53493f",
                       hovering_color="White")
        for nupp in [mänginupp, äramänginupp]:
            nupp.changecolor(m_mouse_pos)
            nupp.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mänginupp.checkinput(m_mouse_pos):
                    play()
                if äramänginupp.checkinput(m_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)
        
def play():
    pygame.display.set_caption('play')
    while game:
        p_mouse_pos = pygame.mouse.get_pos()
        screen.fill("black")
        screen.blit(bg, (0,0))
        p_back=Nupp(image=None, pos=(65,740),
                       text_input="tagasi",
                       font=get_font(18),
                       base_color="#53493f",
                       hovering_color="White")
        for nupp in [p_back]:
            nupp.changecolor(p_mouse_pos)
            nupp.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if p_back.checkinput(p_mouse_pos):
                    main_menu()
        pygame.display.update()
        clock.tick(FPS)



main_menu()
#play()