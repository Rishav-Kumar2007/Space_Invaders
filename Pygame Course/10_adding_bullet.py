import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(("Space Invadors"))
icon = pygame.image.load(r'F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo2.png')
pygame.display.set_icon(icon)

bg = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\bg2.png")


#! Adding Player Image
player_img = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\arcade-game.png")
player_x_coord = 370
player_y_coord = 480
player_X_change = 0

#! Adding Alien Image
alien_image = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\alien.png")
alien_x = random.randint(0, 736) #! random locations of enemy
alien_y = random.randint(50, 150)
alien_x_change = 2
alien_y_change = 60
#!------------------------------

#!---------ADDING BULLET---------
bullet = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\bullet.png")
bullet_x =0 
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready" #? bullet isn't visible 
#!-------------------------------


def player(x, y):
    screen.blit(player_img, (x, y))

def alien(x, y):
    screen.blit(alien_image, (x, y))

#! -------BULLET FUNCTION--------
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+15, y+10))
#!-----------------------------------

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                player_X_change = 3
            if events.key == pygame.K_LEFT:
                player_X_change = -3
            #! if space is pressed the bullet fired
            if events.key == pygame.K_SPACE:
                if bullet_state == "ready":#! when ready then only pressing space would work
                    bullet_x = player_x_coord #! bullet will move in the coordina of when it left the space ship and be there for rest of the time so that it doesn't follow the spcae ship
                    fire_bullet(bullet_x, bullet_y)

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT: #or events.key == pygame.K_UP or events.key == pygame.K_DOWN
                player_X_change = 0



#! addition of boundry for player
    if player_x_coord <=0:
        player_x_coord = 0
    elif player_x_coord >= 736:
        player_x_coord = 736
    player_x_coord += player_X_change

#! alien movement
    if alien_x <=0:
        alien_x_change = 2
        alien_y += alien_y_change
    elif alien_x >= 736:
        alien_x_change = -2
        alien_y += alien_y_change
    alien_x += alien_x_change
#! ---------------------------------

#! bullet movement
    if bullet_y <= 0: #! when bullet reaches the end of screen..
        bullet_y = 480 #! then it goes back to space ship 
        bullet_state = "ready" #! we make it read to be shot again
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change


    player(player_x_coord, player_y_coord)
    alien(alien_x, alien_y)
    pygame.display.update()
