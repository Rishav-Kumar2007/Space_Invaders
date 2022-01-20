import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(("Space Invadors"))
icon = pygame.image.load(r'F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo2.png')
pygame.display.set_icon(icon)

#! Adding Player Image
player_img = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\arcade-game.png")
player_x_coord = 370
player_y_coord = 480
player_X_change = 0
# player_Y_change = 0

#! Adding Alien Image
alien_image = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\alien.png")
alien_x = random.randint(0, 736) #! random locations of enemy
alien_y = random.randint(50, 300)
alien_x_change = 0
alien_y_change = 0


def player(x, y):
    screen.blit(player_img, (x, y))

def alien(x, y):
    screen.blit(alien_image, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False


        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                player_X_change = 0.3
            if events.key == pygame.K_LEFT:
                player_X_change = -0.3
                '''
            if events.key == pygame.K_UP:
                player_Y_change = -0.3
            if events.key == pygame.K_DOWN:
                player_Y_change = 0.3
                '''

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT: #or events.key == pygame.K_UP or events.key == pygame.K_DOWN
                player_X_change = 0
                #player_Y_change = 0

#! addition of boundry
    if player_x_coord <=0:
        player_x_coord = 0
    elif player_x_coord >= 736:
        player_x_coord = 736
        '''
    elif player_y_coord <= 0:
        player_y_coord = 0
    elif player_y_coord >= 536:
        player_y_coord = 536
        '''


    player_x_coord += player_X_change
    # player_y_coord += player_Y_change
    player(player_x_coord, player_y_coord)
    alien(alien_x, alien_y)
    pygame.display.update()
