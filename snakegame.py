# Snake with a rect.. and food with rect..
import pygame
import sys
import random
import time

from pygame import surface

fps = 15
fpsController = pygame.time.Clock()

pygame.init()

width = 600
height = 500

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((width,height))

bgcolor = pygame.Color('#f5ec42')
textcolor = pygame.Color('#000000')
snakecolor = pygame.Color('#f54242')
foodcolor = pygame.Color('#4299f5')

snake_pos = [[100,50],[90,50],[80,50]] # Dynamic variable...
snake_head = [100,50]

# random.choice()
# random.randint()

foodpos = [random.randrange(0,width,10), random.randrange(0,height,10)]

direction = 'RIGHT'  # Current Value.
change_to = direction  # Next Value.

def gameOver():
    my_font = pygame.font.SysFont('times new roman', 90)
    surface = my_font.render('YOU DIED!!',True,textcolor)
    rect = surface.get_rect()
    rect.midtop = (width/2,height/2)
    game_window.blit(surface,rect)
    pygame.display.update()
    show_score()
    time.sleep(5)
    pygame.quit()
    sys.exit()

score = 0

def show_score():
    score_font = pygame.font.SysFont('times new roman', 30,)
    surface = score_font.render("Score:" + str(score),True,textcolor)
    rect = surface.get_rect()
    rect.midtop = (50,15)
    game_window.blit(surface,rect)
    pygame.display.update()
    



while True:
    show_score()
    game_window.fill(bgcolor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    
    if direction == 'UP':
        snake_head[1] -= 10
    if direction == 'DOWN':
        snake_head[1] += 10
    if direction == 'LEFT':
        snake_head[0] -= 10
    if direction == 'RIGHT':
        snake_head[0] += 10

    pygame.draw.rect(game_window,foodcolor,[foodpos[0],foodpos[1],10,10])
    # Adding a new head in body..
    snake_pos.insert(0,list(snake_head))
    if snake_head[0] == foodpos[0] and snake_head[1] == foodpos[1]:
        score += 1
        foodpos = [random.randrange(0,width,10), random.randrange(0,height,10)]
    else:
        snake_pos.pop()

    for block in snake_pos:
        pygame.draw.rect(game_window,snakecolor,[block[0],block[1],10,10])

    if snake_head[0] < 0 or snake_head[0] > width:
        gameOver()
    if snake_head[1] < 0 or snake_head[1] > height:
        gameOver()

    for block in snake_pos[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            gameOver()
        

    fpsController.tick(fps)
    pygame.display.update()
