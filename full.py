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
    def __init__(self, player_image,x_size , y_size, x_cor, y_cor, speed, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= 460:
            self.speed_y *= -1
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            self.speed_x *= -1
            self.speed_y *= 1

class Button():
    def __init__(self, x_cor, y_cor, x_size, y_size, image):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.x_size = x_size
        self.y_size = y_size
        self.image = transform.scale(image.load(image),(x_size, y_size))

    def showButton(self, display):
        if udate == True:
            py.draw.rect(display,(self.x_cor, self.y_cor,self.x_size, self.y_size, self.image))
    
    def focusCheck(self, mousepos, mouseclick):
        if(mousepos[0] >= self.x and mousepos[0] <= self.x + self.sx and mousepos[1] >= self.y and mousepos[1] <= self.y + self.sy):
            self.CurrentState = True
            return mouseclick[0]
        else:
            udate = False


font.init()  
form = font.SysFont('Arial', 50)

FPS = 60
clock = time.Clock()
udate = True
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
