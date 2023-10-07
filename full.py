from pygame import  *


window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Volleyball')
background = transform.scale(image.load('fon.jpg'), window_size)

window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Volleyball')
background2 = transform.scale(image.load('1.jpg'), window_size)

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image,x_size , y_size, x_cor, y_cor, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


font.init()  
form = font.SysFont('Arial', 50)

FPS = 60
clock = time.Clock()
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    if finish == False:
       window.blit(background2, (0,0))
       choise = form.render('Выберите персонажа:', True, [0, 0, 0])
       window.blit(choise, (150, 50))
       

    if finish == True:
       window.blit(background, (0,0))


    display.update()
    clock.tick(FPS)
