import math
import time
import pygame, sys
import random
from nupp import Nupp
pygame.init()

(width, height) = (768, 768)
screen = pygame.display.set_mode((width, height))
screen.fill("black")
bg = pygame.image.load("taust.png")
menubg = pygame.image.load("menüü.png")
bdimg=pygame.image.load("bluedot.png")
ydimg=pygame.image.load("yellowdot.png")
rdimg=pygame.image.load("reddot.png")
tegelane1_pilt=pygame.image.load("tegelane1.png")
bgscaled = pygame.transform.scale(bg, (768,768))
menubgscaled = pygame.transform.scale(menubg, (768,768))
clock = pygame.time.Clock()
FPS=30
game=True

def bdot(xy):
    bluedot=bdimg.get_rect(center=(xy[0],xy[1]))
    return bluedot
def ydot(xy):
    yeldot=ydimg.get_rect(center=(xy[0],xy[1]))
    return yeldot
def rdot(xy):
    reddot=rdimg.get_rect(center=(xy[0],xy[1]))
    return reddot

def get_font(size):
    return pygame.font.Font("font.ttf", size)
def tegelane1(xy):
  tegelane1=tegelane1_pilt.get_rect(bottom=(xy[0],xy[1]))
  return tegelane1
def liikumine():


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
        

täringu_pildid = []
täringu_ani_pildid = []

for num in range(1, 7):
    täringu_pilt = pygame.image.load('täring/' + str(num) + '.png')
    täringu_pildid.append(täringu_pilt)

for num in range(1, 7):
    täringu_ani_pilt = pygame.image.load('animatsioon/a' + str(num) + '.png')
    täringu_ani_pildid.append(täringu_ani_pilt)

kas_keerleb = False
pildi_keerlemis_lugeja = 0
täring_num_pilt = täringu_pildid[0]


def play():
    global kas_keerleb
    global täring_num_pilt
    global pildi_keerlemis_lugeja
    pygame.display.set_caption('play')
    while game:
        p_mouse_pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(bg, (0,0))
        print(p_mouse_pos)
        dotlist=[(170,370),(223,383),(242, 417),(275,445),(325,430),(365,410),(400,435),(400,470),
                 (370,500),(330,530),(322,580),(375,600),(395,645),(360,680),(350,720),(390,745),
                 (465,735),(485,690),(495,648),(500,605),(495,565),(490,522),(485,480),(490,440),
                 (495,395),(490,350),(520,310),(535,265),(475,240),(410,260),(345,280),(280,260),
                 (205,270),(170,230),(175,190),(230,175),(290,175),(350,175),(410,175),(440,145),
                 (385,125),(320,120),(255,120),(190,130),(170,90),(175,55),(210,30),(270,30),
                 (330,30),(390,28),(450,32),(510,30),(570,32),(600,60),(600,95),(600,130),
                 (600,165),(600,200),(600,240),(600,280),(600,320),(590,360),(587,405),(587,455),
                 (587,510),(587,560),(587,610),(587,655),(587,690),(587,720),(648,732),(670,650),
                 (650,550),(670,470),(650,380),(653,313),(670,247),(650,192),(650,120),(650,55),
                 (700,25),(730,60),(725,115),(728,180)]
        bluedotlist=[(),(),(),(),(),(),(),(),(),(),(),()]
        yeldotlist=[(),(),(),(),(),(),(),(),(),(),(),()]
        reddotlist=[(),(),(),(),(),(),(),(),(),(),(),()]
        for dotpos in dotlist:
            screen.blit(bdimg, bdot(dotpos))
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
        
        if key[pygame.K_SPACE] and kas_keerleb is False:
            kas_keerleb = True
            rand_num = random.randint(0, 5)
            täring_num_pilt = täringu_pildid[rand_num]
            screen.blit(täringu_ani_pildid[pildi_keerlemis_lugeja], (25,25))
            pildi_keerlemis_lugeja += 1
            #alustab keerlemist ja kalkuleerib täringu numbri
        else:
            if kas_keerleb:
                screen.blit(täringu_ani_pildid[pildi_keerlemis_lugeja], (25,25))
                pildi_keerlemis_lugeja += 1
                if pildi_keerlemis_lugeja >= 6:
                    kas_keerleb = False
                    pildi_keerlemis_lugeja = 0
                #näitab keerutamise animatsiioni
            else:
                screen.blit(täring_num_pilt,(25, 25))
                #näitab täringu numbrit
        
        pygame.display.update()
        clock.tick(FPS)



main_menu()
#play()