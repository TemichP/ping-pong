from pygame import *
from time import time as timer
font.init()
from random import randint

rect=sprite.Group()

def section(player,pong):
    w=player.rect.bottom-player.rect.y
    if pong.rect.centery<=player.rect.y+w*2/9:
        return -40
    elif player.rect.y+w*2/9<pong.rect.centery<=player.rect.y+w*4/9:
        return -20
    elif player.rect.y+w*4/9<pong.rect.centery<=player.rect.y+w*5/9:
        return 0
    elif player.rect.y+w*5/9<pong.rect.centery<=player.rect.y+w*7/9:
        return 20
    elif player.rect.y+w*7/9<pong.rect.centery<=player.rect.y+w:
        return 40


    
def winna(point1, point2):
    if point1==11 and point2<=9:
        return 'win2'
    if point2==11 and point1<=9:
        return 'win1'
    elif point1>=10 and point2>=10:
        if point1==point2+2:
            return 'win2'
        if point2==point1+2:
            return 'win1'

def timers(t):
    if timer()-t<60:
        return '00:'+str(round(timer()-t))



    

class Sprite_game(sprite.Sprite):
    def __init__(self,play_image,speed,play_x,play_y,x,y):
        super().__init__()
        self.image=transform.scale(image.load(play_image),(x,y))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=play_x
        self.rect.y=play_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(Sprite_game):
    def __init__(self,play_image,speed,play_x,play_y,x,y,power):
        super().__init__(play_image,speed,play_x,play_y,x,y)
        self.power=power
    def update1(self):
        key_pres=key.get_pressed()
        if key_pres[K_w] and self.rect.y>=0:
            self.rect.y-=self.speed
        if key_pres[K_s] and self.rect.y<=410:
            self.rect.y+=self.speed
    def update2(self):
        key_pres=key.get_pressed()
        if key_pres[K_UP] and self.rect.y>=0:
            self.rect.y-=self.speed
        if key_pres[K_DOWN] and self.rect.y<=410:
            self.rect.y+=self.speed

class Button():
    def __init__(self,t_x,t_y,play_x,play_y,x,y,image_text):
        self.h=(play_x,play_y)
        self.image=Surface(self.h)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.imt=font.SysFont('Arial',40).render(image_text,True,(255,255,255))
        self.t_x=t_x
        self.t_y=t_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
        win.blit(self.imt,(self.t_x,self.t_y))
    def coord(self,x,y):
        return self.rect.collidepoint(x,y)

class Ball(Sprite_game):
    def __init__(self,play_image,play_x,play_y,x,y, speed_x, speed_y,k):
        super().__init__(play_image,speed_x,play_x,play_y,x,y)
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.k=k
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if sprite.collide_rect(ball,player1):
            degrees=section(player1,ball)
            if player1.power:
                self.speed_x=randint(7,10)
                self.speed_y=randint(-9,9) 
                player1.power=False
            elif degrees==-40:
                self.speed_x=3*self.k
                self.speed_y=-3
            elif degrees==-20:
                self.speed_x=3*self.k
                self.speed_y=-2
            elif degrees==20:
                self.speed_x=3*self.k
                self.speed_y=2
            elif degrees==40:
                self.speed_x=3*self.k
                self.speed_y=3
            elif degrees==0:
                self.speed_x=5*self.k
                self.speed_y=0
            if self.k<1.3:
                self.k+=0.01    
        if self.rect.y<=1:
            self.speed_y*=-1
            self.speed_x*=self.k
            if self.k<1.3:
                self.k+=0.01 
        if self.rect.y>=465:
            self.speed_y*=-1
            self.speed_x*=self.k
            if self.k<1.3:
                self.k+=0.01    
        if sprite.collide_rect(player2,ball):
            degrees=section(player2,ball)
            if player2.power:
                self.speed_x=randint(-10,-7)
                self.speed_y=randint(-9,9) 
                player2.power=False
            elif degrees==-40:
                self.speed_x=-3*self.k
                self.speed_y=-3
            elif degrees==-20:
                self.speed_x=-3*self.k
                self.speed_y=-2
            elif degrees==20:
                self.speed_x=-3*self.k
                self.speed_y=2
            elif degrees==40:
                self.speed_x=-3*self.k
                self.speed_y=3
            elif degrees==0:
                self.speed_x=-5*self.k
                self.speed_y=0
            if self.k<1.3:
                self.k+=0.01    


win=display.set_mode((700,500))
display.set_caption('Пинг-понг')
background=transform.scale(image.load('фон.jpeg'),(700,500))
clock=time.Clock()
FPS=60
game=True
finish=True
b1=Button(250,120,260,60,230,110,'Продолжить')
b2=Button(300,280,160,60,280,270,'Выход')
b3=Button(260,200,250,60,240,190,'Перезапуск')
player1=Player('левая ракетка.png',5,10,215,20,100,False)
player2=Player('правая ракетка.png',5,650,215,20,100,False)
ball=Ball('мяч.png',300,200,35,35,2,2,1)
for i in range(4):
    rect.add(Sprite_game('куб.png',0,randint(100,550),randint(0,450),25,25))
speed_x=ball.speed
speed_y=ball.speed
font1=font.SysFont('Arial',25)
font2=font.SysFont('Arial',58)
lose_round1=font2.render('Player 1 lost the round',True,(255,0,0))
lose_round2=font2.render('Player 2 lost the round',True,(255,0,0))
lose_game1=font2.render('Player 1 lost the game',True,(255,0,0))
lose_game2=font2.render('Player 2 lost the game',True,(255,0,0))
l1=0
l2=0
rounds=3
rou1=0
rou2=0
tim1=timer()
n=0



while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
        if e.type==KEYDOWN:
            if e.key==K_ESCAPE:
                win.blit(background,(0,0))
                b1.reset()
                b2.reset()
                b3.reset()
                finish=False
                display.update()
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            x, y=e.pos
            if b1.coord(x,y):
                finish=True
            if b2.coord(x,y):
                game=False
            if b3.coord(x,y):
                l1=0
                l2=0
                finish=True
                ball.rect.x=300
                ball.rect.y=200
                player1.rect.y=215
                player2.rect.y=215
                ball.speed_x=2
                ball.speed_y=2
                ball.k=1
                tim1=timer()
                rou1=0
                rou2=0
                for i in range(4-len(rect)):
                    rect.add(Sprite_game('куб.png',0,randint(100,550),randint(0,450),25,25))
                


    if finish!=False:

        win.blit(background,(0,0))
        player1.reset()
        player2.reset()
        ball.reset()
        rect.draw(win)
        ball.update()
        player1.update1()
        player2.update2()

        if sprite.spritecollide(ball,rect,True):
            p=randint(1,2)
            if p==1:
                if ball.speed_x<0:
                    player2.power=True
                else:
                    player1.power=True
            '''if p==2:
                if ball.speed_x<0:
                    player2.y=120
                else:
                    player1.y=120'''




        if ball.rect.x<=0:
            l1+=1
            ball.rect.x=300
            ball.rect.y=200
            player1.rect.y=215
            player2.rect.y=215
            ball.speed_x=2
            ball.speed_y=2
            ball.k=1
            for i in range(4-len(rect)):
                rect.add(Sprite_game('куб.png',0,randint(100,550),randint(0,450),25,25))
        if ball.rect.x>=650:
            l2+=1
            ball.rect.x=300
            ball.rect.y=200
            player1.rect.y=215
            player2.rect.y=215
            ball.speed_x=2
            ball.speed_y=2
            ball.k=1
            for i in range(4-len(rect)):
                rect.add(Sprite_game('куб.png',0,randint(100,550),randint(0,450),25,25))

        ad=winna(l1,l2)
        if ad=='win1':
            #win.blit(lose_round2,(40,200))
            l1=0
            l2=0
            finish=True
            ball.rect.x=300
            ball.rect.y=200
            player1.rect.y=215
            player2.rect.y=215
            ball.speed_x=2
            ball.speed_y=2
            ball.k=1
            tim1=timer()
            if rou1<2:
                rou1+=1
            if rou1==2:
                win.blit(lose_game2,(40,200))
                finish=False

        elif ad=='win2':
            #win.blit(lose_round1,(40,200))
            l1=0
            l2=0
            finish=True
            ball.rect.x=300
            ball.rect.y=200
            player1.rect.y=215
            player2.rect.y=215
            ball.speed_x=2
            ball.speed_y=2
            ball.k=1
            tim1=timer()
            if rou2<2:
                rou2+=1
            if rou2==2:
                win.blit(lose_game1,(40,200))
                finish=False
        


        p1=font1.render('Счёт: '+str(l2)+'-'+str(l1),True,(255,255,255))
        p_g1=font1.render('Выиграл игр:'+str(rou1),True,(255,255,255))
        p_g2=font1.render('Выиграл игр:'+str(rou2),True,(255,255,255))
        tim=font1.render(timers(tim1),True,(255,255,255))

        win.blit(p1,(280,20))
        win.blit(p_g1,(10,20))
        win.blit(p_g2,(500,20))
        win.blit(tim,(320,60))        

        clock.tick(FPS)
        display.update()
