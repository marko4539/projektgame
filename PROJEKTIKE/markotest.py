import math
import time
import pygame, sys
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
kas_keerleb = False
def get_font(size):
    return pygame.font.Font("font.ttf", size)
    
def main_menu():
    pygame.display.set_caption('menu')
    screen.fill("black")
    while True:
        screen.blit(menubg, (0,0))
        m_mouse_pos = pygame.mouse.get_pos()
        mängunimi= get_font(30).render("mainmenu", True, "#53493f")
        mängunimi4n=mängunimi.get_rect(center=(200, 200))
        screen.blit(mängunimi, mängunimi4n)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(FPS)

täringu_pildid=
täringu_ani_pildid=

def play():
    pygame.display.set_caption('play')
    while game:
        p_mouse_pos = pygame.mouse.get_pos()
        screen.fill("black")
        screen.blit(bg, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if p_back.checkForInput(p_mouse_pos):
                main_menu()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and kas_keerleb is False:
            pass
            #alustab keerlemist ja kalkuleerib täringu numbri
        else:
            if kas_keerleb:
                pass
                #näitab keerutamise animatsiioni
            else:
                pass
                #näitab täringu numbrit
            
        
        pygame.display.update()
        clock.tick(FPS)

main_menu()