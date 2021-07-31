import pygame
import sys

from pygame import mixer


#Initializing 
pygame.init()

#Create Screen
screen = pygame.display.set_mode((900,600))

#Background
background = pygame.image.load('background.jpg')

#Title and Icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Background song
mixer.music.load('background.wav')
mixer.music.play(-1)

#Game Over Text
over_font = pygame.font.Font('freesansbold.ttf',64)
game_over = False

#Player who has won initially it is 0 later itll be 1 for player1 and 2 for player2
winner = 0

#Drawing TicTacToe Board
def draw_board():
    screen.fill((255,255,255))
    screen.blit(background,(0,0))

    #Drawing Horizontal And Vertical Line on Board
    pygame.draw.line(screen,(80,200,120),(300,0),(300,600),10)
    pygame.draw.line(screen,(80,200,120),(600,0),(600,600),10)
    pygame.draw.line(screen,(80,200,120),(0,200),(900,200),10)
    pygame.draw.line(screen,(80,200,120),(0,400),(900,400),10)

#The playing grid each sublist is a coloum 
grid = [[0,0,0],[0,0,0],[0,0,0]]

#to conform mouse click
click = False

#Initially player1s chance then player2 chances(-1)
player = 1

#Drawing cross and cicle
def draw_fig():
    #in first coloum x = 0 and for second itll be 1
    x = 0
    for x_pos in grid:
        #in first row y= 0 and for second row itll be 1
        y = 0
        for y_pos in x_pos:
            #if in grid it is 1 draw cross and if -1 draw circle
            if y_pos == 1:
                pygame.draw.line(screen,(0,255,0),(x * 300 + 15, y * 200 + 15), (x * 300 + 285, y *200 + 185),6)
                pygame.draw.line(screen,(0,255,0),(x * 300 + 15, y * 200 + 185), (x * 300 + 285, y *200 + 15),6)

            if y_pos == -1:
                pygame.draw.circle(screen,(255,0,0),(x*300 + 150 ,y*200 + 100),75,6)
            y += 1
        x += 1

#checking for winner and tie
def winning_logic():
    global winner
    global game_over

    #Coloum check
    for x in grid:
        if sum(x) == 3 :
            winner = 1
            game_over = True
        if sum(x) == -3 :
            winner = 2
            game_over = True

    #ROW CHECK 
    y = 0
    for x in range(3):
        if grid[0][y] + grid[1][y] + grid[2][y] == 3:
                winner = 1
                game_over = True
        if grid[0][y] + grid[1][y] + grid[2][y] == -3:
                winner = 2
                game_over = True
        y += 1

    #Diagonal Check
    if grid[0][0] + grid[1][1] + grid[2][2] == 3 or grid[0][2] + grid[1][1] + grid[2][0] == 3:
        winner = 1
        game_over = True
    if grid[0][0] + grid[1][1] + grid[2][2] == -3 or grid[0][2] + grid[1][1] + grid[2][0] == -3:
        winner = 2
        game_over = True

    #Tie Check
    if game_over == False:
        tie = True
        for x in grid:
            for y in x:
                if y == 0:
                    tie = False
        if tie == True:
            winner = 0
            game_over = True


#Displaying game over and who won
def game_over_text():
    over_text = over_font.render("Player " + str(winner) + " is the Winner",True,(128,0,128))
    screen.blit(over_text, (150,250))



#Game loop
running = True
while running:
    
    draw_board()
    draw_fig()
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
            if event.type == pygame.MOUSEBUTTONDOWN and click == False:
                click = True
            if event.type == pygame.MOUSEBUTTONUP and click == True:
                click = False
                #This gets the coordinates of the mouse click
                x,y = pygame.mouse.get_pos()
                #If grid is = 0 ie that position is empty then assign to correct player
                if grid[x // 300][y // 200] == 0:
                    grid[x // 300][y // 200] = player
                    player *= -1
                    winning_logic()
        
    pygame.display.update()