from pygame import  *


window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Volleyball')
background = transform.scale(image.load('fon.jpg'), window_size)


class GameSprite(sprite.Sprite): 
    def __init__(self, player_image,x_size , y_size, x_cor, y_cor, speed_x, speed_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed = speed
        self.speed.x = speed_x
        self.speed.y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 300:
            self.rect.x += self.speed 
        if keys_pressed[K_w] and self.rect.y < 100:
            self.rect.y += self.speed 
        if keys_pressed[K_s] and self.rect.y > 600:
            self.rect.y += self.speed  

    def update2(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_a] and self.rect.x > 300:
            self.rect.x -= self.speed 
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed 
        if keys_pressed[K_w] and self.rect.y < 100:
            self.rect.y += self.speed 
        if keys_pressed[K_s] and self.rect.y > 600:
            self.rect.y += self.speed         

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed



FPS = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))


    display.update()
    clock.tick(FPS)
