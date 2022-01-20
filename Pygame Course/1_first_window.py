import pygame
pygame.init() #? acceses the functions of the library

screen = pygame.display.set_mode((800, 600)) #? make the screen and give width, height
#! after comma we add it to be able to resize

#? GAME LOOP
running = True #! the window closes so for that this code
while running:
    for event in pygame.event.get(): #! for things happening in the game window
        if event.type == pygame.QUIT: #! if X is pressed then close it
            running = False #! so its made false hence window closed






