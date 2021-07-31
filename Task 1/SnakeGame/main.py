import pygame
import sys
import random

from pygame import mixer

#Initializing 
pygame.init()

#Create Screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.jpg')

#Background song
mixer.music.load('background.wav')
mixer.music.play(-1)

# Snake Variables
snakeX = 370
snakeY = 480
snake_size = 30
snakeX_change = 0
snakeY_change = 0
snake_body = []
snake_length = 1


#Fruit
FruitX = random.randint(30,770)
FruitY = random.randint(30,570)
Fruit_size = 30


#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Game Over Text
over_font = pygame.font.Font('freesansbold.ttf',64)
game_over = False

#If distance is less than 30 than it will eat fruit
def isCollision(FruitX,FruitY,SnakeX,SnakeY):
    distanceX = abs(FruitX - SnakeX)
    distanceY = abs(FruitY - SnakeY)
    if distanceX < 30 and distanceY < 30:
        return True
    else :
        return False

#Displays Score
def show_score(x,y):
    score = font.render("Score :" + str(score_value),True, (0,255,0))
    screen.blit(score,(x,y))

#Displays Game Over 
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0,0,255))
    screen.blit(over_text, (200,250))

#Drawing Snake
def draw_snake(screen,snake_body,snake_size):
    for x,y in snake_body:
        pygame.draw.rect(screen,(0,0,0),[x,y,snake_size,snake_size])

running = True
while running:

    # Background color
    screen.fill((255,255,255))
    #background  image
    screen.blit(background,(0,0))
    if game_over:
        game_over_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running == False
                pygame.quit()
                sys.exit(0)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running == False
                pygame.quit()
                sys.exit(0)

            #if keystroke is pressed whether its left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snakeX_change = -0.8
                    snakeY_change = 0
                if event.key == pygame.K_RIGHT:
                    snakeX_change = 0.8
                    snakeY_change = 0
                if event.key == pygame.K_UP:
                    snakeY_change = -0.8
                    snakeX_change = 0
                if event.key == pygame.K_DOWN:
                    snakeY_change = 0.8
                    snakeX_change = 0

            #if snake crosses screen then game over
            if snakeX < 0 or snakeX > 800 or snakeY < 0 or snakeY > 600:
                snakeX = 0
                snakeY = 0
                game_over = True
                
        #Colllision
            collision = isCollision(FruitX,FruitY,snakeX,snakeY)
            if collision:
                score_value +=1
                snake_length += 5
                FruitX = random.randint(30,770)
                FruitY = random.randint(30,570)


    snakeX += snakeX_change
    snakeY += snakeY_change

    #Drawing Apple
    pygame.draw.rect(screen,(255,0,0),[FruitX,FruitY,Fruit_size,Fruit_size])

    #Snake head
    snake_head = []
    snake_head.append(snakeX)
    snake_head.append(snakeY)
    snake_body.append(snake_head)
    
    #if snake body bigger than score then delete first snake body ie last rectangle
    if len(snake_body) > snake_length:
        del snake_body[0]

    #if snake head touches body then game over, last index is head itself so check for all before that
    if snake_head in snake_body[:-1]:
        game_over = True
    draw_snake(screen,snake_body,snake_size)

    show_score(textX,textY)
    pygame.display.update()
    