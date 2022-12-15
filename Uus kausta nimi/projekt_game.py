import math
import time
import pygame, sys
import random
from nupp import Nupp
from tegelane import Tegelane
pygame.init()

(width, height) = (768, 768)
global screen
screen = pygame.display.set_mode((width, height))
screen.fill("black")
bg = pygame.image.load("taust.png")
menubg = pygame.image.load("menüü.png")
bdimg=pygame.image.load("bluedot.png")
ydimg=pygame.image.load("yellowdot.png")
rdimg=pygame.image.load("reddot.png")
tegelane1_pilt=pygame.image.load("tegelane1.png")
tegelane2_pilt=pygame.image.load("tegelane2.png")
bgscaled = pygame.transform.scale(bg, (768,768))
menubgscaled = pygame.transform.scale(menubg, (768,768))
clock = pygame.time.Clock()
FPS=45
game=True
global nimi1
nimi1="Marko"
global nimi2
nimi2="Rene"
def bdot(xy):
    bluedot=bdimg.get_rect(center=(xy[0],xy[1]))
    return bluedot
def ydot(xy):
    yeldot=ydimg.get_rect(center=(xy[0],xy[1]))
    return yeldot
def rdot(xy):
    reddot=rdimg.get_rect(center=(xy[0],xy[1]))
    return reddot
def Ending1():
    lõputekst= get_font(20).render(f"{nimi1} jõudis lõppu!", True, "#53493f")
    lõputekst4n=lõputekst.get_rect(center=(380, 300))
    screen.blit(lõputekst, lõputekst4n)
    lõputekst= get_font(20).render(f"{nimi2} eksmatrikuleeritakse", True, "#53493f")
    lõputekst4n=lõputekst.get_rect(center=(380, 400))
    screen.blit(lõputekst, lõputekst4n)

def Ending2():
    lõputekst= get_font(20).render(f"{nimi2} jõudis lõppu!", True, "#53493f")
    lõputekst4n=lõputekst.get_rect(center=(380, 300))
    screen.blit(lõputekst, lõputekst4n)
    lõputekst= get_font(20).render(f"{nimi1} eksmatrikuleeritakse", True, "#53493f")
    lõputekst4n=lõputekst.get_rect(center=(380, 400))
    screen.blit(lõputekst, lõputekst4n)
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
        

täringu_pildid = []
täringu_ani_pildid = []

for num in range(1, 7):
    täringu_pilt = pygame.image.load('täring/' + str(num) + '.png')
    täringu_pildid.append(täringu_pilt)

for num in range(1, 7):
    täringu_ani_pilt = pygame.image.load('animatsioon/a' + str(num) + '.png')
    täringu_ani_pildid.append(täringu_ani_pilt)

keerlemis_heli = pygame.mixer.Sound('veeretamine.mp3')
keerlemis_lõpu_heli = pygame.mixer.Sound('veeretamine6.mp3')
pygame.mixer.music.load('muss.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

kas_keerleb = False
pildi_keerlemis_lugeja = 0
täring_num_pilt = täringu_pildid[0]
esimene=True

dotlist=[(170,370),(223,383),(242, 417),(275,445),(325,430),(365,410),(400,435),(400,470),
                 (370,500),(330,530),(322,580),(375,600),(395,645),(360,680),(350,720),(390,745),
                 (465,735),(485,690),(495,648),(500,605),(495,565),(490,522),(485,480),(490,440),
                 (495,395),(490,350),(520,310),(535,265),(475,240),(410,260),(345,280),(280,260),
                 (205,270),(170,230),(175,190),(230,175),(290,175),(350,175),(410,175),(440,145),
                 (385,125),(320,120),(255,120),(190,130),(170,90),(175,55),(210,30),(270,30),
                 (330,30),(390,28),(450,32),(510,30),(570,32),(600,60),(600,95),(600,130),
                 (600,165),(600,200),(600,240),(600,280),(600,320),(590,360),(587,405),(587,455),
                 (587,510),(587,560),(587,610),(587,655),(587,690),(587,720),(648,732),(670,650),
                 (650,550),(670,470),(650,380),(653,313),(670,247),(650,192),(650,55),
                 (700,25),(730,60),(725,115),(728,180),(730,245),(725,310),(730,375),(728,440),
                 (725,505),(730,565),(728,625),(725,680),(732,732)]
bluedotlist=[(170,370),(223,383),(325,430),(365,410),(400,470),(370,500),(375,600),(395,645),
                     (390,745),(495,648),(500,605),(495,565),(490,522),(490,440),
                     (495,395),(410,260),(345,280),(205,270),(170,230),(175,190),(230,175),(290,175),
                     (350,175),(410,175),(385,125),(320,120),(190,130),(170,90),(210,30),(270,30),(330,30),
                     (510,30),(600,60),(600,95),(587,405),(587,455),(587,510),(732,732)]
yeldotlist=[(242, 417),(330,530),(322,580),(360,680),(465,735),(485,690),(490,350),(520,310),(535,265),
                    (475,240),(255,120),(175,55),(390,28),(450,32),(570,32),(600,130),(600,200),(600,240),(600,280),
                    (600,320),(590,360),(587,560),(587,610),
                    (587,655),(648,732),(670,650),(650,550),(670,470),(650,380),(653,313),(670,247),(650,192),
                    (650,120),(650,55),(700,25)]
reddotlist=[(275,445),(400,435),(350,720),(485,480),(280,260),(440,145),(600,165),(587,690),(587,720),
                    (730,60),(725,115),(728,180),(730,245),(725,310),(730,375),(728,440),(725,505),(730,565),
                    (728,625),(725,680)]
end1 = False
end2 = False
def Eventbox(teg):
    eb = pygame.image.load("eventaken.png")
    event = True
    if teg == "teg1":
        if dotlist[uus1] is dotlist[-1]:
            global end1
            end1 = True
            
        elif vanapos1 in bluedotlist:
            event = False
        elif vanapos1 in yeldotlist:
            event = False
        elif vanapos1 in  reddotlist:
            event = False
    if teg == "teg2":
        if dotlist[uus2] is dotlist[-1]:
            global end2
            end2 = True
            
        elif vanapos2 in bluedotlist:
            event = False
        elif vanapos2 in yeldotlist:
            event = False
        elif vanapos2 in  reddotlist:
            event = False
    while event == True:
        p_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if p_back.checkinput(p_mouse_pos):
                    main_menu()
                    
        if end1 == True:
            screen.blit(eb, (70,160))
            Ending1()
        if end2 == True:
            screen.blit(eb, (70,160))
            Ending2()

        e_back=Nupp(image=None, pos=(65,740),
                       text_input="tagasi",
                        font=get_font(18),
                       base_color="#53493f",
                       hovering_color="White")
        for nupp in [e_back]:
            nupp.changecolor(p_mouse_pos)
            nupp.update(screen)
            
        pygame.display.update()
        clock.tick(FPS)

def play():
    global kas_keerleb
    global täring_num_pilt
    global pildi_keerlemis_lugeja
    pygame.display.set_caption('play')
    tväärtus=0
    tväärtused=[0]
    teg1=Tegelane(image=tegelane1_pilt, pos=dotlist[0], text_input=nimi1, font=get_font(12),color="blue")
    teg2=Tegelane(image=tegelane2_pilt, pos=dotlist[0], text_input=nimi2, font=get_font(12),color="red")
    vanapos1=dotlist[0]
    vanapos2=dotlist[0]
    liikumine1 = False
    liikumine2 = False
    while game:
        p_mouse_pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(bg, (0,0))
        for dotpos in bluedotlist:
            screen.blit(bdimg, bdot(dotpos))
        for dotpos in yeldotlist:
            screen.blit(ydimg, ydot(dotpos))
        for dotpos in reddotlist:
            screen.blit(rdimg, rdot(dotpos))
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
        if teg1.täringjäänud == 0 and teg2.täringjäänud == 0:
            if key[pygame.K_SPACE] and kas_keerleb is False and liikumine1 is False and liikumine2 is False:
                kas_keerleb = True
                keerlemis_heli.play()
                rand_num = random.randint(0, 5)
                täring_num_pilt = täringu_pildid[rand_num]
                tväärtus = rand_num + 1
                tväärtused.append(tväärtus)
                print(tväärtus)
                print(tväärtused)
                esimene=True
                screen.blit(täringu_ani_pildid[pildi_keerlemis_lugeja], (25,25))
                pildi_keerlemis_lugeja += 1
                #alustab keerlemist ja kalkuleerib täringu numbri
                if len(tväärtused) % 2 == 1:
                    teg1.täringlisa(tväärtus)
                if len(tväärtused) % 2 == 0:
                    teg2.täringlisa(tväärtus)
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
                if esimene and rand_num == 5:
                    keerlemis_lõpu_heli.play()
                    esimene=False
                #näitab täringu numbrit
        #print(teg1.täringjäänud)
        #print(teg2.täringjäänud)
        if teg1.täringjäänud > 0 and kas_keerleb is False:
            liikumine1 = True
            global uus1
            uus1=dotlist.index((vanapos1))+1
            pos1=vanapos1
            try:
                posvektor1=(dotlist[uus1][0]-pos1[0],dotlist[uus1][1]-pos1[1])
                teg1.x_pos+=posvektor1[0]/10
                teg1.y_pos+=posvektor1[1]/10
                teg1.update(screen)
            except:
                continue
            if round(teg1.x_pos) == dotlist[uus1][0] and round(teg1.y_pos) == dotlist[uus1][1]:
                liikumine1 = False
                if dotlist[uus1] is dotlist[-1]:
                    Eventbox("teg1")
                vanapos1=dotlist[uus1]
                teg1.täringjäänud-=1
#        if teg1.täringjäänud == 0:
#            if vanapos1 is not dotlist[0]:      
#                Eventbox(teg1)

        if teg2.täringjäänud > 0 and kas_keerleb is False:
            liikumine2 = True
            global uus2
            uus2=dotlist.index((vanapos2))+1
            pos2=vanapos2
            try:
                posvektor2=(dotlist[uus2][0]-pos2[0],dotlist[uus2][1]-pos2[1])
                teg2.x_pos+=posvektor2[0]/10
                teg2.y_pos+=posvektor2[1]/10
                teg2.update(screen)
            except:
                continue
            if round(teg2.x_pos) == dotlist[uus2][0] and round(teg2.y_pos) == dotlist[uus2][1]:
                liikumine2 = False
                if dotlist[uus2] is dotlist[-1]:
                    Eventbox("teg2")
                vanapos2=dotlist[uus2]
                teg2.täringjäänud-=1
                
#         if teg2.täringjäänud == 0:
#             if vanapos2 is not dotlist[0]:      
#                 Eventbox(teg2)

        teg1.update(screen)
        teg2.update(screen)
        pygame.display.update()
        clock.tick(FPS)



main_menu()
#play()