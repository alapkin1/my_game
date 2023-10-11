from pygame import  *



window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Volleyball')
background = transform.scale(image.load('1.jpg'), window_size)

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
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.y_size = y_size
        self.x_size = y_size

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



font.init()  
form = font.SysFont('Arial', 50)

player1 = GameSprite('player1.jpg', 100, 100, 100, 250, 0, 0, 0)
player2 = GameSprite('player2.jpg', 100, 100, 300, 250, 0, 0, 0)
player3 = GameSprite('player4.png', 100, 100, 500, 250, 0, 0, 0)
player4 = GameSprite('player5.jpg', 100, 100, 500, 250, 0, 0, 0) 
players = sprite.Group() 

FPS = 60
clock = time.Clock()
udate = False
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if udate == False:
        window.blit(background2, (0,0))
        choise = form.render('Выберите персонажа:', True, [0, 0, 0])
        window.blit(choise, (100, 50))
        player1.reset() 
        player2.reset()
        player3.reset()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if player1.rect.collidepoint(x, y):
                players.add(player1)
                udate = True
            elif player2.rect.collidepoint(x, y):
                players.add(player2)
                udate = True
            elif player3.rect.collidepoint(x, y):
                players.add(player3)
                udate = True

    if udate == True:
        print(789)
        window.blit(background2, (0,0))
        choise = form.render('Выберите персонажа:', True, [0, 0, 0])
        window.blit(choise, (100, 50))
        player4.reset()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if player4.rect.collidepoint(x, y):
                players.add(player4)
                finish = True




                    
            
    if finish:
       window.blit(background, (0,0))
       players.draw(window)



    display.update()
    clock.tick(FPS)
