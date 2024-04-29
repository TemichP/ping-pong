from pygame import *
font.init()
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
    def __init__(self,play_image,play_x,play_y,x,y, speed_x, speed_y):
        super().__init__(play_image,speed_x,play_x,play_y,x,y)
        self.speed_x=speed_x
        self.speed_y=speed_y
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(player2,ball):
            self.speed_x*=-1
        if self.rect.y<=1:
            self.speed_y*=-1
        if self.rect.y>=450:
            self.speed_y*=-1



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
player1=Player('левая ракетка.png',5,10,215,20,100)
player2=Player('правая ракетка.png',5,650,215,20,100)
ball=Ball('мяч.png',300,200,50,50,2,2)
speed_x=ball.speed
speed_y=ball.speed
font1=font.SysFont('Arial',25)
font2=font.SysFont('Arial',70)
lose1=font2.render('PLAYER 1 LOSE!',True,(255,0,0))
lose2=font2.render('PLAYER 2 LOSE!',True,(255,0,0))
l1=0
l2=0

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


    if finish!=False:

        win.blit(background,(0,0))
        player1.reset()
        player2.reset()
        ball.reset()
        ball.update()
        player1.update1()
        player2.update2()

        if ball.rect.x<=0:
            l1+=1
            ball.rect.x=300
            ball.rect.y=200
            player1.rect.y=215
            player2.rect.y=215
            ball.speed_x=2
            ball.speed_y=2
        if ball.rect.x>=650:
            l2+=1
            ball.rect.x=300
            ball.rect.y=200
            player1.rect.y=215
            player2.rect.y=215
            ball.speed_x=2
            ball.speed_y=2

        if l1>=5:
            win.blit(lose1,(10,200))
            finish=False
        if l2>=5:
            win.blit(lose2,(10,200))
            finish=False


        p1=font1.render('Пропущено:'+str(l1),True,(255,255,255))
        p2=font1.render('Пропущено:'+str(l2),True,(255,255,255))
        win.blit(p1,(10,20))
        win.blit(p2,(535,20))


        clock.tick(FPS)
        display.update()
