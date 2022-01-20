import pygame
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(("Space Invadors"))
icon = pygame.image.load(r'F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo2.png')
pygame.display.set_icon(icon)
bg = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\bg2.png")

#!Music____________
mixer.music.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\sounds\bgm2.mp3")
mixer.music.play(-1) #? -1 to play on loop
#!_________________


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

#! -----ADDING SCORE----
score = 0
font = pygame.font.Font(r'F:\RISHAV\Python38-32 codes\Pygame Course\fonts\CaviarDreams_BoldItalic.ttf', 32)
text_x = 10
text_y = 10

def show_score (x, y):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))
#! ---------------------

#!-----GAME OVER-----
go_text = "GAME OVER!"
font_go = pygame.font.Font(r'F:\RISHAV\Python38-32 codes\Pygame Course\fonts\PTC55F.ttf', 100)
go_text_y = 210
go_text_x = 100

def game_over(x, y):
    go = font_go.render(go_text, True, (255, 255, 255))
    screen.blit(go, (x, y))
#!-------------------

#?----CREDITS----
credit_text = "Made by Rishav using Python!"
credit_font = pygame.font.Font(r"F:\RISHAV\Python38-32 codes\Pygame Course\fonts\CaviarDreams_BoldItalic.ttf", 20)
credit_x = 250
credit_y = 350

def credit(x, y):
    credit = credit_font.render(credit_text, True, (255, 255, 255))
    screen.blit(credit, (x, y))
#?---------------
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
                    bullet_sound = mixer.Sound(r"F:\RISHAV\Python38-32 codes\Pygame Course\sounds\pew.mp3")
                    bullet_sound.play()
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

        #! Game Over:
        if alien_y[i] > 400:
            for j in range(number_of_enemies):
                alien_y[j] = 1000
            game_over(go_text_x, go_text_y)
            credit(credit_x, credit_y)
            break

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
            explosion_sound = mixer.Sound(r"F:\RISHAV\Python38-32 codes\Pygame Course\sounds\explode.wav")
            explosion_sound.play()
            bullet_y = 480 #? back to initial
            bullet_state = "ready"
            score += 1
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
    
    show_score(text_x, text_y)
    player(player_x_coord, player_y_coord)
    pygame.display.update()
