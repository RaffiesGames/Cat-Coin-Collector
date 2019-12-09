import pygame
import os
import time
import random

def msg(mess,size,status,color,x,y):
    myfont=pygame.font.Font('freesansbold.ttf',size)
    textsurface=myfont.render(mess,status,color)
    screen.blit(textsurface,(x,y))

pygame.init()

run=True

Black=(0,0,0)
White=(255,255,255)

x=40
y=40
score=0
coinx = random.randint(2,400)
coiny = random.randint(2,400)

myfont = pygame.font.Font('freesansbold.ttf', 20)
myfont2 = pygame.font.Font('freesansbold.ttf', 50)
catimg = pygame.image.load('Cat.png')
coinimg = pygame.image.load('Coin.jpg')
scorefont = pygame.font.SysFont('arial',15)

os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(30,30)
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
screen.blit(catimg,(1,1))
pygame.display.set_caption('Cat Walk Simulator 2018')
pygame.time.set_timer(pygame.USEREVENT,1000)
scorescreen=scorefont.render(str(score),True,Black)
col = False

while run:
    catrect = pygame.Rect((x,y),catimg.get_size())
    coinrect = pygame.Rect((coinx,coiny),coinimg.get_size())
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            scorescreen=scorefont.render(str(score),True,Black)
    col=catrect.colliderect(coinrect)
    print (col)
    if col == True: 
        coinx = random.randint(2,400) 
        coiny = random.randint(2,400)
        score = score + 1
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]:
        y=y-10
    if key[pygame.K_DOWN]:
        y=y+10
    if key[pygame.K_LEFT]:
        x=x-10                
    if key[pygame.K_RIGHT]:
        x=x+10
    if key[pygame.K_ESCAPE] or event.type==pygame.QUIT:
        msg('Thank you for playing',20,True,Black,110,230)
        pygame.display.update()
        time.sleep(3)
        run=False
        break
    if x<=-10 or x>=455 or y<=-10 or y>=425:
        msg('The Cat got hurt.',20, True, Black,120,220)
        msg('You Lose',20, True, Black,160,250)
        pygame.display.update()
        time.sleep(3)
        run=False
        break
    screen.fill(White)
    screen.blit(catimg,(x,y))
    screen.blit(coinimg,(coinx,coiny))
    screen.blit(scorescreen,(465,0))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
