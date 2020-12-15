import pygame
import random
pygame.init()


sw = 800
sh = 600
bg = pygame.image.load("bg2.png")
win = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Pong")

vel = 10
p1Score = 0
p2Score = 0

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 100
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])

class Ball(object):
    def __init__(self):
        self.radius = 5
        self.x = sw//2
        self.y = sh//2
        self.color = (255, 255, 255)
        xd = random.choice([-1,1])
        yd = random.choice([-1, 1])
        self.xv = 5 * xd
        self.yv = 5 * yd

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def hit(self):
        self.xv *= -1

    def resetPong(self):
        self.x = sw // 2
        self.y = sh // 2
        xd = random.choice([-1, 1])
        yd = random.choice([-1, 1])
        self.xv = 5 * xd
        self.yv = 5 * yd
        player1.y = sh//2 - player1.h//2
        player2.y = sh // 2 - player2.h // 2
        redrawGameWindow()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


def redrawGameWindow():
    win.blit(bg, (0,0))
    font = pygame.font.SysFont('comicsans', 50)
    player1.draw(win)
    player2.draw(win)
    ball.draw(win)
    score1Text = font.render(str(p1Score), 1, (195, 195, 195))
    score2Text = font.render(str(p2Score), 1, (195, 195, 195))
    win.blit(score1Text, (10, 10))
    win.blit(score2Text, (sw - 10 - score2Text.get_width(), 10))

    pygame.display.update()



player1 = Player(10, sh//2 - 50)
player2 = Player(sw - 30, sh//2 - 50)
ball = Ball()

run = True
while run:
    clock.tick(100)

    ball.move()

    if ball.y < 0 or ball.y + ball.radius > sh:
        ball.yv *=-1

    if ball.x - ball.radius <= player1.x + player1.w and ball.x - ball.radius >= player1.x:
        if (ball.y - ball.radius >= player1.y and ball.y -ball.radius <= player1.y + player1.h) or (ball.y + ball.radius >= player1.y and ball.y + ball.radius <= player1.y + player1.h):
            ball.hit()
            ball.x = player1.x + player1.w + ball.radius

    if ball.x + ball.radius >= player2.x  and ball.x + ball.radius <= player2.x + player2.x:
        if (ball.y - ball.radius >= player2.y and ball.y -ball.radius <= player2.y + player2.h) or (ball.y + ball.radius >= player2.y and ball.y + ball.radius <= player2.y + player2.h):
            ball.hit()
            ball.x = player2.x - ball.radius

    if ball.x < 0 - ball.radius:
        p2Score += 1
        # ball = Ball()
        ball.resetPong()
    if ball.x > sw:
        p1Score += 1
        #ball = Ball()
        ball.resetPong()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if player2.y - vel < 0:
            player2.y = 0
        else:
            player2.y -= vel

    if keys[pygame.K_w]:
        if player1.y - vel < 0:
            player1.y = 0
        else:
            player1.y -= vel

    if keys[pygame.K_DOWN]:
        if player2.y + player2.h + vel > sh:
            player2.y = sh - player2.h
        else:
            player2.y += vel

    if keys[pygame.K_s]:
        if player1.y + player1.h + vel > sh:
            player1.y = sh - player1.h
        else:
            player1.y += vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()