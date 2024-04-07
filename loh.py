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
    def update(self):

class Enemy(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
           self.rect.x += self.speed


platform = Enemy('platform.png', 200, 300, 300, 150, 60)


mach = Player('mach.png', 40, 380, 50, 150, 100)
# speed_x = 3
# speed_y = 3 




while game:
    for e in event.get():
        window.blit(background, (0,0))
        mach.reset()
        mach.update()
        platform.reset()
        platform.update
        if e.type == QUIT:
            game = False
        # if finish != True: 
        #     ball.rect.x += speed_x
        #     ball.rect.y += speed_y
            
    clock.tick(FPS)
    display.update()