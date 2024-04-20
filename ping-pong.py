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

class Ball(Sprite_game):
    def update(self):
        speed_x=self.speed
        speed_y=self.speed
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(player2,ball):
            speed_x*=-1
        if ball.rect.y>=450:
            speed_y*=-1
        if ball.rect.x>=650:
            speed_x*=-1
        if ball.rect.y<=0:
            speed_y*=-1
        if ball.rect.x<=0:
            speed_x*=-1

win=display.set_mode((700,500))
display.set_caption('Пинг-понг')
background=transform.scale(image.load('фон.jpeg'),(700,500))
clock=time.Clock()
FPS=60
game=True
finish=True
player1=Player('левая ракетка.png',5,10,215,50,100)
player2=Player('правая ракетка.png',5,650,215,50,100)
ball=Ball('мяч.png',-2,300,200,50,50)
speed_x=ball.speed
speed_y=ball.speed
font2=font.SysFont('Arial',75)
lose1=font2.render('PLAYER 1 LOSE!',True,(255,0,0))
lose2=font2.render('PLAYER 2 LOSE!',True,(255,0,0))

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish!=False:
        win.blit(background,(0,0))
        player1.reset()
        player2.reset()
        ball.reset()
        player1.update1()
        player2.update2()

        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(player2,ball):
            speed_x*=-1
        if ball.rect.y>=450:
            speed_y*=-1
        if ball.rect.y<=0:
            speed_y*=-1

        if ball.rect.x<=0:
            win.blit(lose1,(50,220))
            finish=False
        if ball.rect.x>=650:
            win.blit(lose2,(50,220))
            finish=False


        clock.tick(FPS)
        display.update()         