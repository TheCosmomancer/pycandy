#Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
gamescreen = 'menu'

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    mousepos = pygame.mouse.get_pos()
    if gamescreen == 'menu':
        if mouse[0] == True:
            if 180<=mousepos[0]<=540 and 480<=mousepos[1]<=560:
                running = False
            elif 180<=mousepos[0]<=540 and 320<=mousepos[1]<=400:
                gamescreen = 'newgame'

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('black')
    font1 = pygame.font.SysFont(None, 70)
    if gamescreen == 'menu':
        #newgame
        pygame.draw.rect(screen,'white',(180,160,360,80),5)
        screen.blit(font1.render('New Game', True, "white"), (230, 177))
        #cont
        pygame.draw.rect(screen, 'grey', (180, 320, 360, 80), 5)
        screen.blit(font1.render('Continue', True, "white"), (245, 337))
        #exit
        pygame.draw.rect(screen, 'grey', (180, 480, 360, 80), 5)
        screen.blit(font1.render('Exit', True, "white"), (312, 497))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
