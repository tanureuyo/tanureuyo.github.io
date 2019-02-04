#This is a simple snake gaming made with pygame, install pygame to run
"""
#Along with the first sentdex tutorial, I used another one (https://www.youtube.com/watch?v=1hlaMPzAUZ0&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=12)
 to create the pause function
"""
import pygame as game
import time as t
import random as r
import tkinter as tk
from tkinter import messagebox
game.init()

clock = game.time.Clock()
white = (255,255,255)
black= (0,0,0)
red = (180,0,0)
bright_red = (255,0,0)
green = (0,180,0)
bright_green = (0,255,0)

display_width = 800
display_height = 800
block_size = 25
pause = True
#1. Defines sounds effects and music
death_sound = game.mixer.Sound("death.wav")
game.mixer.music.load("C418 - Stal.wav")

 

fps = 30
gameDisplay = game.display.set_mode((display_width,display_height))
game.display.set_caption('Snake')
gameCounter = game.display.set_mode((display_width,display_height))

font = game.font.SysFont(None, 25)
#2. Adds a grid to show the play area
def text_buttons(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = game.mouse.get_pos()
    click = game.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        game.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        game.draw.rect(gameDisplay, ic, (x,y,w,h))
    smallText = game.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_buttons(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        game.draw.line(surface, (0,0,0), (x,0),(x,w))
        game.draw.line(surface, (0,0,0), (0,y),(w,y))
def snake(block_size, snakelist): #draws the snake to the screen
    for XnY in snakelist:
        gameDisplay.fill(green, rect=[XnY[0], XnY[1], block_size, block_size])   
def message_to_screen(msg, color): #prints a message to th e screen
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/4, display_height/4], None)
#3. Counts the amount of apples the snake has collected
def appleCount(number, color):
    appleCount = font.render(number, True, color)
    gameCounter.blit(appleCount, [display_width/8, display_height/8])
#4. Title screen before game
def titleScreen():
    gameDisplay.fill(white)
    message_to_screen("Welcome to Fast Snake! Press C to play or Q to exit.", red)
    pauseAlert = font.render("Press P at any time to pause the game." , True, red)
    gameDisplay.blit(pauseAlert,[display_width/3, display_height/3])
    game.display.update()
    gameStart = False
    while not gameStart:
        for event in game.event.get():
            if event.type == game.KEYDOWN:
                if event.key == game.K_q:
                    game.quit()
                if event.key == game.K_c:
                    gameStart = True
                    gameLoop()
        
    for event in game.event.get():
        if event.type == game.QUIT:
            gameExit = True
#5. Creats a pause functionality
def paused():    
    while pause:
        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                quit()
        game.mixer.music.pause()
        gameDisplay.fill(white)
        largeText = game.font.SysFont("comicsansms", 115)
        textSurf, textRect = text_buttons("Paused", largeText)
        textRect.center =  ((display_width/2), (display_height/4))
        gameDisplay.blit(textSurf, textRect)
        
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        game.display.update()
        clock.tick(15)
def unpause():
    global pause
    pause = False
    game.mixer.music.unpause()
def quitgame():
    game.quit()
    quit()
#Main code block that runs the game
def gameLoop():
    global pause
    game.mixer.music.play(-1) #starts music in a loop
    message_to_screen("Welcome to Fast Snake! Press C to play or Q to exit.", red)
    game.display.update()
    t.sleep(10)
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    apples = 0

    snakeList = []
    snakeLength = 1
    #Places apple in a random position
    randAppleX = round(r.randrange(0, display_width-block_size)/block_size)*block_size
    randAppleY = round(r.randrange(0, display_height-block_size)/block_size)*block_size
    while not gameExit:
        if gameOver == True:
                game.mixer.Sound.play(death_sound)
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("GAME OVER. Press C to play again or Q to exit.", red)
            game.mixer.music.stop()
            game.display.update()

            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    if event.key == game.K_q:
                        gameExit = True
                        gameOver = False
                        
                    if event.key == game.K_c:
                        gameLoop()
       
                       
        for event in game.event.get():
            if event.type == game.QUIT:
                gameExit = True
                game.quit()
            #Logic that turns key presses into movement
            if  event.type == game.KEYDOWN:
                if event.key == game.K_LEFT or event.key == game.K_a:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == game.K_RIGHT or event.key == game.K_d:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == game.K_UP or event.key == game.K_w:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == game.K_DOWN or event.key == game.K_s:
                    lead_y_change = block_size
                    lead_x_change = 0
                if event.key == game.K_p:
                    pause = True
                    paused()
                   
                
            
        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            gameOver = True
            
        lead_x += lead_x_change
        lead_y += lead_y_change
       
        #Adds to snake length if apple run over
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(r.randrange(0, display_width-block_size)/block_size)*block_size
            randAppleY = round(r.randrange(0, display_height-block_size)/block_size)*block_size
            snakeLength += 1
            apples += 1
            appleCount('Apple  Count: ' +str(apples), red)
            game.display.update()
            t.sleep(.8)
            print('Apple Count: '+str(apples))
            

        gameDisplay.fill(white)
        gameDisplay.fill(red, rect=[randAppleX, randAppleY, block_size, block_size])
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        #Checks if snake has crossed itself
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                

        snakeList[:-1]
        
        snake(block_size, snakeList)
        drawGrid(display_width, 32, gameDisplay)
        game.display.update()
        clock.tick(fps)
                
            
   
    game.display.update()
    t.sleep(4)
    game.quit()

titleScreen()



