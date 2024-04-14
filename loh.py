from pygame import *


window = display.set_mode((700, 500))
display.set_caption('loh krutoi')

background = transform.scale(image.load('akito pups.jpg'), (700,500))

clock = time.Clock()
FPS = 60 
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys(K_UP) and self.rect_y > 5:
            self.rect.y -= self.speed
        if keys(K_DOWN) and self.rect_y < 500 - 80:
            self.rect.y += self.speed  
    def update_l(self):
        keys = key.get_pressed()
        if keys(K_w) and self.rect_y > 5:
            self.rect.y -= self.speed
        if keys(K_s) and self.rect_y < 500 - 80:
            self.rect.y += self.speed  





racket1 = Player('platform2.png', 500, 200, 50, 150, 150)
racket2 = Player('platform.png', 40, 200, 50, 150, 150)



ball = GameSprite('mach.png',350, 250, 50, 150, 100)

speed_x = 3
speed_y = 3 

finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        ball.update()
        
        racket1.update_r()
        racket2.update_l() 
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1

        #if ball.rect.x < 0: 
           #finish = True
          # window.blit(lose1,(200, 500))
           #game_over = True 

        racket1.reset()
        racket2.reset()
        ball.reset()

    clock.tick(FPS)
    display.update()