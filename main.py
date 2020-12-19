# Programmer: Luca Rubino
# Program: Le_Game
# Date: 01/21/17
import pygame, sys, time, random
from pygame.constants import *
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
width = 800
height = 500
screen = pygame.display.set_mode((width, height))
screenrect = screen.get_rect()
pygame.display.set_caption('JUMP GAME')

PHASE1 = 750
PHASE2 = 1200
PHASE3 = 1500
Red = Color(255, 0, 0)
Blue = Color(0, 0, 255)
Green = Color(0, 255, 0)
White = Color(255, 255, 255)
Orange = Color(255, 165, 0)
Black = Color(0, 0, 0)
LightBlue = Color(51, 255, 255)
LightGreen = Color(51, 255, 51)
Pink = Color(255, 51, 255)
Yellow = Color(255, 255, 0)
DarkBlue = Color(0, 0, 153)

Phase2BarColor = Black
Phase3BarColor = Black
Phase2BackgroundColor = White

rainbow = [Red, Blue, Green, Orange, LightBlue, LightGreen, Pink, Yellow, DarkBlue]
score = 0
players = 1
score2 = 0

highscore = 0
psizex = 25
psizey = 25
psizex2 = 25
psizey2 = 25
ObH = 500
Ob = []
x = [1000, 1250, 1500, 1750, 2000, 2250]
movex = [5, 5, 5, 5, 5, 5]
Oby = [random.randint(300, 350), random.randint(300, 350), random.randint(300, 350), random.randint(300, 350),
       random.randint(300, 350), random.randint(300, 350), ]
keys = pygame.key.get_pressed()

cirx, ciry = 0, 0
vel_x, vel_y = 0, 1
acc_x, acc_y = 0, 0.2
xw = 50
cirx2, ciry2 = 10, 10
vel_x2, vel_y2 = 0, 1
acc_x2, acc_y2 = 0, 0.2

screen_rect = screen.get_rect()
P1GameOver = False
P2GameOver = False
Scoreboard = False
run = False
Intro = True
font = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Arial", 70)
font3 = pygame.font.SysFont("System Bold", 120)
fontsb = pygame.font.SysFont("Fixedsys Regular", 90)


# This function resets all variables so the game can start again
def resetGame():
    global score, score2, Phase2BarColor, Phase3BarColor, Phase2BackgroundColor, highscore, x, Oby, cirx, ciry, cirx2, ciry2, vel_x, vel_y, vel_x2, vel_y2, acc_x, acc_y, acc_x2, acc_y2, P1GameOver, P2GameOver, Scoreboard
    score = 0
    score2 = 0
    highscore = 0
    x = [1000, 1250, 1500, 1750, 2000, 2250]
    Oby = [random.randint(300, 350), random.randint(300, 350), random.randint(300, 350), random.randint(300, 350),
           random.randint(300, 350), random.randint(300, 350), ]

    cirx, ciry = 0, 0
    vel_x, vel_y = 0, 1
    acc_x, acc_y = 0, 0.2
    cirx2, ciry2 = 10, 10
    vel_x2, vel_y2 = 0, 1
    acc_x2, acc_y2 = 0, 0.2

    Phase2BarColor = Black
    Phase3BarColor = Black
    Phase2BackgroundColor = White

    P1GameOver = False
    P2GameOver = False
    Scoreboard = False


# Function to show instructions
def HowToPlay():
    htp = True
    image = pygame.image.load('Game Instructions.png')
    screen.blit(image, (0, 0))
    image1 = pygame.transform.scale(image, (width, height))
    screen.blit(image1, (0, 0))
    fpsClock.tick(30)
    pygame.display.flip()

    while htp:
        for event in pygame.event.get():
            if (event.type == QUIT):
                sys.exit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_ESCAPE]:
            htp = False


# This function pauses the game and lets the user resume or quit
def PauseGame():
    Pause = True
    while Pause:  # This is the pause menu
        for event in pygame.event.get():
            if (event.type == QUIT):
                sys.exit()

        screen.fill(White)
        Pausescreen = font.render("Player 1's score is " + str(score), 1, (Black))
        Pausescreen2 = font.render("Player 2's score is " + str(score2), 1, (Black))
        unpause = font.render("Press Q to continue" + " or Press E to quit", 1, (Black))
        Pausa = font3.render("PAUSE", 1, (Black))
        screen.blit(Pausescreen, (width / 3, height / 1.5))
        screen.blit(Pausescreen2, (width / 3, height / 1.3))
        screen.blit(unpause, (width / 4.3, height / 2))
        screen.blit(Pausa, (width / 3, height / 4))
        fpsClock.tick(30)
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            Pause = False
        elif keys[pygame.K_e]:
            sys.exit(0)


# Function to display Intro

def displayIntro(selection):
    dIntro = True
    while dIntro:
        screen.fill(White)
        Introfont = pygame.font.SysFont("Terminal", 75)
        P1option = pygame.font.SysFont("Terminal", 40)
        P2option = pygame.font.SysFont("Terminal", 40)
        Instructions = pygame.font.SysFont("Terminal", 30)
        Confirmation = Instructions.render("Press Enter to confirm", 1, Black)
        Option1 = P1option.render("W -> Single Player Game", 1, Black)
        Option2 = P2option.render("S -> Two Player Game", 1, Black)
        Option3 = Instructions.render("D -> How to Play", 1, Black)
        Option4 = Instructions.render("A -> QUIT", 1, Black)
        Intro = Introfont.render("WELCOME TO JUMP GAME", 1, Black)
        screen.blit(Confirmation, (width / 2.7, height / 1.2))
        screen.blit(Intro, (width / 10.5, height / 4.8))
        screen.blit(Option1, (width / 3, height / 1.9))
        screen.blit(Option2, (width / 3, height / 1.5))
        screen.blit(Option3, (width / 1.3, height / 1.2))
        screen.blit(Option4, (width / 10, height / 1.2))

        for event in pygame.event.get():
            if (event.type == QUIT):
                sys.exit()
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            selection = 1
        if keys[K_s]:
            selection = 2
        if keys[K_d]:
            selection = 3
        if keys[K_a]:
            selection = 4

        if selection == 1:
            pygame.draw.rect(screen, Black, Rect(width / 3.5, height / 1.9, 25, 25), 0)
        if selection == 2:
            pygame.draw.rect(screen, Black, Rect(width / 3.5, height / 1.5, 25, 25), 0)
        if selection == 3:
            pygame.draw.rect(screen, Black, Rect(width / 1.4, height / 1.2, 25, 25), 0)
        if selection == 4:
            pygame.draw.rect(screen, Black, Rect(width / 20, height / 1.2, 25, 25), 0)
        fpsClock.tick(30)
        pygame.display.flip()

        if keys[K_RETURN]:
            if selection == 3:
                HowToPlay()
            elif selection == 4:
                sys.exit()
            else:
                dIntro = False

    return (selection)


# This function displays scoreboard once the player(s) are dead
def displayScoreBoard():
    Scoreboard = True

    while Scoreboard:  # This enables the Scoreboard when both players are dead
        screen.fill(White)
        scoreboardtext = font.render("Scoreboard", 1, Black)
        screen.blit(scoreboardtext, (width / 2.6, height / 9))
        scoretext3 = font.render("Player 1's score was " + str(score), 1, Black)
        scoretext4 = font.render("Player 2's score was " + str(score2), 1, Black)
        scoreexit = font.render("Press R to Play Again            Press ESCAPE to quit", 1, Black)
        screen.blit(scoretext3, (width / 3.3, height / 3))
        screen.blit(scoretext4, (width / 3.3, height / 2))
        screen.blit(scoreexit, (width / 7, height / 1.5))
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == QUIT):
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            Scoreboard = False
        if keys[pygame.K_ESCAPE]:
            sys.exit()


# Main program starts below

players = displayIntro(players)
run = True

while run:

    vel_x += acc_x
    vel_y += acc_y
    cirx += vel_x
    ciry += vel_y
    vel_x2 += acc_x2
    vel_y2 += acc_y2
    cirx2 += vel_x2
    ciry2 += vel_y2

    if ciry >= height - psizey:  # stay in screen Player 1
        ciry = height - psizey
        vel_y = 1
    if cirx <= 0:
        cirx = 0
    if cirx >= width - psizex:
        cirx = width - psizex
    if ciry <= psizey:
        ciry = psizey

    if ciry2 >= height - psizey:  # stay in screen Player 2
        ciry2 = height - psizey
        vel_y2 = 1
    if cirx2 <= 0:
        cirx2 = 0
    if cirx2 >= width - psizex:
        cirx2 = width - psizex
    if ciry2 <= psizey:
        ciry2 = psizey

    player = pygame.Rect(cirx, ciry, psizex, psizey)
    player2 = pygame.Rect(cirx2, ciry2, psizex2, psizey2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: ciry -= 10.3  # Player 1 controls
    if keys[pygame.K_a]: cirx -= 10
    if keys[pygame.K_s]: ciry += 10
    if keys[pygame.K_d]: cirx += 10

    if keys[pygame.K_UP]: ciry2 -= 10.3  # Player 2 controls
    if keys[pygame.K_LEFT]: cirx2 -= 10
    if keys[pygame.K_DOWN]: ciry2 += 10
    if keys[pygame.K_RIGHT]: cirx2 += 10
    if keys[pygame.K_ESCAPE]:
        PauseGame()
    screen.fill(Phase2BackgroundColor)

    if P1GameOver == False:
        pygame.draw.rect(screen, (Phase3BarColor), player)
    if P2GameOver == False and players == 2:
        pygame.draw.rect(screen, (Yellow), player2)

    supersaiyan = rainbow[(random.randint(0, 8))]

    scoretext = font.render("Player 1 Score is " + str(score), 1, Phase3BarColor)
    scoretext2 = font.render("Player 2 Score is " + str(score2), 1, Phase3BarColor)

    if players == 1:
        P2GameOver = True
        screen.blit(scoretext, (width / 8, height / 5))
    if players == 2:
        screen.blit(scoretext, (width / 8, height / 5))
        screen.blit(scoretext2, (width / 1.8, height / 5))

    if not P1GameOver:  # Controls the score
        score += 1
    if not P2GameOver and players == 2:
        score2 += 1

    # This section moves the obstacles and changes the colours based on score reached by the player(s)
    for a in range(len(x)):
        pygame.draw.rect(screen, Black, [x[a], Oby[a], xw, ObH - Oby[a]])
        if score >= PHASE1 or score2 >= PHASE1:  # This makes the obstacles and background change colour as you proceed further in the game
            Phase3BarColor += Color(5, 5, 5)
            Phase2BackgroundColor -= Color(5, 5, 5)
            Phase2BarColor += Color(1, 0, 0)
            pygame.draw.rect(screen, Phase2BarColor, [x[a], Oby[a], xw, ObH - Oby[a]])
            if Phase2BarColor == Red:
                Phase2BarColor += Color(0, 0, 0)
            if Phase2BackgroundColor == Black:
                Phase2BackgroundColor += Color(0, 0, 0)
            if Phase3BarColor == White:
                Phase3BarColor += Color(0, 0, 0)
        if score >= PHASE2 or score2 >= PHASE2:
            Red -= Color(1, 0, 0)
            Red += Color(0, 0, 1)
            pygame.draw.rect(screen, Red, [x[a], Oby[a], xw, ObH - Oby[a]])
            if Red == Blue:
                Red += Color(0, 0, 0)
        if score >= PHASE3 or score2 >= PHASE3:
            pygame.draw.rect(screen, supersaiyan, [x[a], Oby[a], xw, ObH - Oby[a]])
        if ciry + psizex >= Oby[a]:
            if (cirx + psizex > x[a]) and (cirx < x[a] + 50):
                P1GameOver = True
        if ciry2 + psizex2 >= Oby[a]:
            if (cirx2 + psizex2 > x[a]) and (cirx2 < x[a] + 50):
                P2GameOver = True
        x[a] -= movex[a]  # check to see if off screen
        if x[a] <= - xw:
            x[a] = width  # once off of screen move back

        if P1GameOver and P2GameOver == True:
            displayScoreBoard()

            players = displayIntro(players)
            resetGame()
            P1GameOver = False
            P2GameOver = False

    fpsClock.tick(30)
    pygame.display.flip()

sys.exit(0)



