import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(("Space Invadors"))
icon = pygame.image.load(r'F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo2.png')
pygame.display.set_icon(icon)

#! Adding Player Image
player_img = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\arcade-game.png")
player_x_coord = 370
player_y_coord = 480

def player():
    screen.blit(player_img, (player_x_coord, player_y_coord)) #? blit is like drawiing image on screen
#! -----------------player image added----------------------------

running = True
while running:
    screen.fill((0, 0, 0)) #! this is on top so its drawn first
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    player() #! this is below so its drawn later on top of first
    pygame.display.update()
