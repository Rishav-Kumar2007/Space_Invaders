import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\ufo.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load(r"F:\RISHAV\Python38-32 codes\Pygame Course\Images\arcade-game.png")
player_X = 370
player_Y = 480
player_X_change = 0
player_Y_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False


        if events.type == pygame.KEYDOWN: #! checking if key is pressed or not
            print ("KEY IS PRESSED") #? if key is pressed then tell user
            if events.key == pygame.K_RIGHT: #! if right key is pressed then..
                player_X_change = 0.3 #? the change in x coordinate is +Ve so it moves right
            if events.key == pygame.K_LEFT: #! if left key is pressed then..
                player_X_change = -0.3 #? the change in x coordinate is -Ve so it moves left

            if events.key == pygame.K_UP: #! if UP key is pressed then..
                player_Y_change = -0.3 #? the change in Y coordinate is -Ve so it moves UP
            if events.key == pygame.K_DOWN: #! if DOWN key is pressed then..
                player_Y_change = 0.3 #? the change in Y coordinate is +Ve so it moves DOWN

        if events.type == pygame.KEYUP: #! checking if key is released or not
            print ("KEY IS RELEASED") #! if key is released then tell user
            if (events.key == pygame.K_RIGHT) or (events.key == pygame.K_LEFT) or (events.key == pygame.K_UP) or (events.key == pygame.K_DOWN): #! if any key is released then
                player_X_change = 0 #! there is no change in x coordinate
                player_Y_change = 0 #! there is no change in x coordinate

    player_X += player_X_change #? here we change maine coordinates sccording to key event
    player_Y += player_Y_change
    player(player_X, player_Y)
    pygame.display.update()

