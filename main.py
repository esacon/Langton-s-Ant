# Ant Icons made by Freepik from www.flaticon.com

import time
import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox

# Defining colours
# RGB (Red, Green, Blue)
white = (255, 255, 255)
gray = (84, 84, 84)
black = (0, 0, 0)
ant = (255, 255, 0)

# Game start values
pygame.init()
frames = 30
fps = 1.0 / frames  # Frames per second
width = 1024
height = width - 100

# Building the ant
antImage = pygame.image.load('ant_figure.png')

# Iteration parameters
n = -1
while n < 0:
    n = input('Digite el numero de iteraciones a realizar (Recomendado 12000): ')
    n = int(n)

running = True
iter = 1

# Resizing ant's size, so it could fit in a cell
scale = -1
while scale > 10 or scale <= 0:
    scale = input('Digite el tamanio de la grilla (Numero entre 1 y 10 -Recomendado 4-): ')
    scale = int(scale)

gap = scale * 3  # Define gap size for the grid
antImage = pygame.transform.scale(antImage, (gap, gap))
rows = width // gap  # Number of rows for the grid

# Defining the initial position of the ant and grid
initialX = -1
while initialX > width - 1 or initialX <= 0:
    initialX = input('Digite la posicion inicial para X (Numero entre 1 y 1023): ')
    initialX = int(initialX)

initialY = -1
while initialY > height - 1 or initialY <= 0:
    initialY = input('Digite la posicion inicial para Y (Numero entre 1 y 923): ')
    initialY = int(initialY)

# Setting window preferences
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption("La Hormiga de Langton")
icon = pygame.image.load('ant_icon.png')
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 36)

diffX = width // initialX
diffY = width // initialY
antX = rows // diffX
antY = rows // diffY
direction = 0

colored = [[False] * rows for i in range(rows)]  # Set all rows as white

# Defining positions
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))


def drawGrid(lineColor):
    xCoord = 0
    yCoord = 0
    for l in range(rows):
        xCoord = xCoord + gap
        yCoord = yCoord + gap

        # Define the start and end position for drawing lines
        pygame.draw.line(lineColor, gray, (xCoord, 0), (xCoord, width))
        pygame.draw.line(lineColor, gray, (0, yCoord), (width, yCoord))


def redrawWindow(background):
    background.fill(white)
    drawGrid(background)
    pygame.display.update()


def newDirection():
    global direction
    # Set a new direction for the ant
    if not colored[antX][antY]:
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4
    return direction


def movement():
    global antX, antY, direction
    # Verify whether the cell is colored or not
    if not colored[antX][antY]:
        colored[antX][antY] = True
        pygame.draw.rect(screen, gray, (antX * gap, antY * gap, gap, gap))
    else:
        colored[antX][antY] = False
        pygame.draw.rect(screen, white, (antX * gap, antY * gap, gap, gap))
    # Set next direction
    direction = newDirection()
    antX = (antX + dirs[direction][0]) % rows
    antY = (antY + dirs[direction][1]) % rows

    # Draw the current position of the ant
    pygame.draw.rect(screen, ant, (antX * gap, antY * gap, gap, gap))
    if direction == UP:
        antPos(moveAntLook(antImage, 0), antX * gap, antY * gap)
        posText = font.render("---ARRIBA---", True, black, white)
    if direction == LEFT:
        antPos(moveAntLook(antImage, 90), antX * gap, antY * gap)
        posText = font.render("IZQUIERDA", True, black, white)
    if direction == DOWN:
        antPos(moveAntLook(antImage, 180), antX * gap, antY * gap)
        posText = font.render("---ABAJO--- ", True, black, white)
    if direction == RIGHT:
        antPos(moveAntLook(antImage, -90), antX * gap, antY * gap)
        posText = font.render("-DERECHA-", True, black, white)

    screen.blit(posText, (width - 150, 10))


def antPos(image, x, y):
    screen.blit(image, (x, y))


def moveAntLook(ant, grad):
    return pygame.transform.rotate(ant, grad)


def endWindow():
    endWin = Tk()
    endWin.geometry("0x0")
    endWin.resizable(False, False)
    messagebox.showwarning("FINALIZADO", "CERRAR APLICACION")
    endWin.destroy()


redrawWindow(screen)
mixer.music.load('ants_sound.mp3')
mixer.music.play(-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # n = Numbers of iterations
    if iter <= n:
        iterText = font.render("Iteracion: {}".format(iter), True, black, white)
        screen.blit(iterText, (10, 10))
        # Move
        movement()
        pygame.display.update()
        iter += 1
        time.sleep(fps)
    else:
        pygame.mixer.music.stop()
        endWindow()
        running = False

