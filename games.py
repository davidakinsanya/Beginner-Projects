import pygame
import time
import random

pygame.init()

width = 800
height = 600 # size of the game frame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0) 

dark_red = (150,0,0)
dark_green = (0,150,0) # colours used for the game

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('*skrrt*')
clock = pygame.time.Clock() # game ish

image = pygame.image.load('skrr.png') # car image
car_width = 135
pause = True
score = []


def dodge(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: " + str(count), True, red) # blocks dodge count function
    display.blit(text,(10,10))
    

def blocks(blockx,blocky,blockw,blockh,color):
    pygame.draw.rect(display, color, [blockx, blocky, blockw, blockh]) # blocks function

def car(x,y):
    display.blit(image,(x,y)) 

def text_objects(text, font):
    TextSurface = font.render(text, True, red)
    return TextSurface, TextSurface.get_rect()

def message_display(text):
    
    large  = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, large)
    TextRect.center = ((width/2),(height/2))
    display.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()

def crash():
    message_display("u done fucked up boi.") # crash message
    
def quit1():
    pygame.quit()
    quit()
       
def button(action = None): # the main green button function

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if 352+100 > mouse[0] > 250 and 250+50 > mouse[1] > 250:
            
        pygame.draw.rect(display,green,(352,250,100,50)) # if the mouse is on the button, light it up
        
        if click[0] == 1 and action != None:
            action() # if its clicked, run the action function
               
    else:    
        pygame.draw.rect(display,dark_green,(352,250,100,50)) # if the mouse isn't on the button leave it a dark green colour

def unpause():
    global pause
    pause = False


def paused(): # pause function
    
    global pause
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(black)
        large  = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects("*paused*", large)
        TextRect.center = ((width/2),(height/3))
        display.blit(TextSurf, TextRect)
        
        button(unpause) # when the button is pressed, run the unpause function
        pygame.display.update()
        clock.tick(60)

            
def intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(black)
        large  = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects("*skrrt*", large)
        TextRect.center = ((width/2),(height/3))
        display.blit(TextSurf, TextRect)
        
        button(game_loop) # when the button is pressed, run the gameloop function
        pygame.display.update()
        clock.tick(60)

            
def game_loop():
    
    x = (width*0.4)
    y = (height*0.8) # variables for car movement
    
    changex = 0
    startx = random.randrange(55,width-250)
    starty = -600
    speed = 10
    width2 = 100
    height2 = 100
    count = 0 # variables for the falling blocks
    
    
    exit_game = False

    while not exit_game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    changex = -7
                     
                if event.key == pygame.K_RIGHT:
                    changex = 7
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
                     
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    changex = 0

 
        x += changex # this will make the car move according to the key presses
        display.fill(black)
        
        blocks(startx, starty, width2, height2, green)

        starty += speed
        car(x,y)
        dodge(count)
        
        if x > width - car_width or x < 0:
            score.append(count)
            print(score)
            print(" ")
            crash() 
            
        if starty > height:
            starty = 0 - height2
            startx = random.randrange(55,width-250)
            count += 1
            
        
        if y < starty+height2:
            pass

            if y < starty+height2 and x > startx and x < startx+width2 or x+car_width > startx and x+car_width < startx+width2:
                score.append(count)
                print(score)
                print(" ")
                crash() 
                
      
        pygame.display.update()
        clock.tick(85)
        
intro()
game_loop()  
pygame.quit()
quit()
