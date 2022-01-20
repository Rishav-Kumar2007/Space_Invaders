import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(("Space Invadors"))
icon = pygame.image.load(r'F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo2.png')
pygame.display.set_icon(icon)
score = 0
bg = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\bg2.png")


#! Adding Player Image
player_img = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\arcade-game.png")
player_x_coord = 370
player_y_coord = 480
player_X_change = 0


#!-------Adding enemies-------
#!Adding multiple enemies:
alien_image = []
alien_x = []
alien_y = []
alien_x_change = []
alien_y_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    alien_image.append(pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\alien.png"))
    alien_x.append(random.randint(0, 736)) #! random locations of enemy
    alien_y.append(random.randint(50, 150))
    alien_x_change.append(2)
    alien_y_change.append(60)

#!----------------------------------------


bullet = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\bullet.png")
bullet_x =0 
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready" #? bullet isn't visible 



def player(x, y):
    screen.blit(player_img, (x, y))

def alien(x, y, i):
    screen.blit(alien_image[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+15, y+10))


def collision(bulletX, bulletY, enemyX, enemyY):
    distance = ((bulletX - enemyX)**2 + (bulletY - enemyY)**2)**0.5
    #print(distance)
    if distance < 27:
        return True
    return False


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
    for i in range(number_of_enemies):
        if alien_x[i] <=0:
            alien_x_change[i] = 2
            alien_y[i] += alien_y_change[i]
        elif alien_x[i] >= 736:
            alien_x_change[i] = -2
            alien_y[i] += alien_y_change[i]
        alien_x[i] += alien_x_change[i]
    #!------DO THINGS AFTER COLLISION---------
        collision_happened = collision(bulletX=bullet_x, bulletY=bullet_y, enemyX=alien_x[i], enemyY=alien_y[i])
        if collision_happened:
            bullet_y = 480 #? back to initial
            bullet_state = "ready"
            score += 1
            print(score)
            alien_x[i] = random.randint(0, 736) #! random locations of enemy
            alien_y[i] = random.randint(50, 150)
        alien(alien_x[i], alien_y[i], i)
#! ---------------------------------

#! bullet movement
    if bullet_y <= 0: #! when bullet reaches the end of screen..
        bullet_y = 480 #! then it goes back to space ship 
        bullet_state = "ready" #! we make it read to be shot again
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x_coord, player_y_coord)
    pygame.display.update()
