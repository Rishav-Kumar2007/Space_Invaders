import pygame
from pygame import event
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invadors")
icon = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load (r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\arcade-game.png")
player_X = 370
player_Y = 480


def player(x, y):
    screen.blit(player_img, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))


    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False


        #! Key stroke event detection
        if events.type ==  pygame.KEYDOWN:
            print("A KEYSTROKE HAS BEEN PRESSED")
            if events.key == pygame.K_LEFT:
                print("Left arrow is pressed")
            if events.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
        if events.type == pygame.KEYUP:
            print("A KEYSTROKE HAS BEEN RELEASED")
            if events.key == pygame.K_LEFT:
                print("Left arrow is released")
            if events.key == pygame.K_RIGHT:
                print("Right arrow is released")
        #! --------------------------


    player(player_X, player_Y)
    pygame.display.update()
