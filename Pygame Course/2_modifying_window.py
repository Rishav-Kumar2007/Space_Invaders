import pygame
pygame.init()
screen = pygame.display.set_mode((900, 400))# width, height

#! Custom title and icon of  game window
pygame.display.set_caption("Space Invadors") #? title
icon = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo2.png")
pygame.display.set_icon(icon) #? icon from FLATICONS.COM (32px X 32px) 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#! anything inside that appears always goes in this loop
    screen.fill((255, 255, 255)) #! give RGB color code
    pygame.display.update() #!update changes