#Example file showing a circle moving on screen
import pygame
import random
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    running = True
    gamescreen = 'menu'
    gamephasephase = 0
    satr = ''
    soton = ''
    inp = ''
    gamemap = list()
    refills = 0
    empty = set()
    protected = set()
    tempset = set()
    candies = ['r','o','y','g','b','p'] #for red, orange, yellow,green,blue and purple respetively
    held = False
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
                elif 180<=mousepos[0]<=540 and 160<=mousepos[1]<=240:
                    gamescreen = 'newgame'
        elif gamescreen == 'newgame':
            if mouse[0] == True:
                if 180<=mousepos[0]<=540 and 480<=mousepos[1]<=560:
                    if gamephasephase == 0 and held == False:
                        satr = int(inp)
                        inp =''
                        gamephasephase = 1
                    elif gamephasephase == 1 and not held:
                        soton = int(inp)
                        inp = ''
                        gamephasephase = 2
                    elif gamephasephase == 2 and not held:
                        empty = tempset
                        tempset = set()
                        inp = ''
                        gamephasephase = 3
                    elif gamephasephase == 3 and not held:
                        protected = tempset
                        tempset = set()
                        inp = ''
                        gamephasephase = 4
                    elif gamephasephase == 4 and not held:
                        if inp == '':
                            inp = '0'
                        refills = int(inp)
                        inp = ''
                        gamescreen = 'gameprep'
                        gamephasephase = 0
                elif 180<=mousepos[0]<=540 and 330<=mousepos[1]<=410 and (gamephasephase == 2 or gamephasephase == 3) and not held:
                    inp = inp.split(',')
                    inp[0] = int(inp[0])
                    inp[1] = int(inp[1])
                    if 0 < int(inp[0]) <= satr and 0 < int(inp[1]) <= soton:
                        tempset.add((inp[0]-1,inp[1]-1))
                    inp = ''
                held = True
            elif keys[pygame.K_0] or keys[pygame.K_KP0]:
                if not held:
                    inp += '0'
                held = True
            elif keys[pygame.K_1] or keys[pygame.K_KP1]:
                if not held:
                    inp += '1'
                held = True
            elif keys[pygame.K_2] or keys[pygame.K_KP2]:
                if not held:
                    inp += '2'
                held = True
            elif keys[pygame.K_3] or keys[pygame.K_KP3]:
                if not held:
                    inp += '3'
                held = True
            elif keys[pygame.K_4] or keys[pygame.K_KP4]:
                if not held:
                    inp += '4'
                held = True
            elif keys[pygame.K_5] or keys[pygame.K_KP5]:
                if not held:
                    inp += '5'
                held = True
            elif keys[pygame.K_6] or keys[pygame.K_KP6]:
                if not held:
                    inp += '6'
                held = True
            elif keys[pygame.K_7] or keys[pygame.K_KP7]:
                if not held:
                    inp += '7'
                held = True
            elif keys[pygame.K_8] or keys[pygame.K_KP8]:
                if not held:
                    inp += '8'
                held = True
            elif keys[pygame.K_9] or keys[pygame.K_KP9]:
                if not held:
                    inp += '9'
                held = True
            elif keys[pygame.K_COMMA]:
                if not held:
                    inp += ','
                held = True
            elif keys[pygame.K_BACKSPACE]:
                if not held and len(inp) > 0:
                    temp = ''
                    for letter in range(len(inp)-1):
                        temp += inp[letter]
                    inp = temp
                held = True
            else:
                held = False
        elif gamescreen == 'gameprep':
            for i in range(satr):
                gamemap.append(['generated' for j in range(soton)])
            for i in range(satr):
                for j in range(soton):
                    if (i,j) not in empty:
                        gamemap[i][j] = random.choice(candies)
                    else:
                        gamemap[i][j] = 'blocked'
            amodimult = 720/satr
            ofoghimult = 600/soton
            gamescreen = 'game'
        elif gamescreen == 'game':
            ...
        # fill the screen with a color to wipe away anything from last frame
        screen.fill('black')
        font1 = pygame.font.SysFont(None, 70)
        font2 = pygame.font.SysFont(None, 50)
        if gamescreen == 'menu':
            screen.blit(font1.render('Candy Pop!', True, "white"), (217, 50))
            #newgame
            pygame.draw.rect(screen,'white',(180,160,360,80),5)
            screen.blit(font1.render('New Game', True, "white"), (230, 177))
            #cont
            pygame.draw.rect(screen, 'grey', (180, 320, 360, 80), 5)
            screen.blit(font1.render('Continue', True, "white"), (245, 337))
            #exit
            pygame.draw.rect(screen, 'grey', (180, 480, 360, 80), 5)
            screen.blit(font1.render('Exit', True, "white"), (312, 497))
        elif gamescreen == 'newgame':
            if gamephasephase == 0:
                screen.blit(font1.render('How many rows?', True, "white"), (160, 150))
            elif gamephasephase == 1:
                screen.blit(font1.render('How many colomns?', True, "white"), (160, 150))
            elif gamephasephase == 2:
                screen.blit(font2.render('what spaces should be blocked ?', True, "white"), (80, 150))
                pygame.draw.rect(screen, 'grey', (180, 330, 360, 80), 5)
                screen.blit(font1.render('Add', True, "white"), (310, 347))
            elif gamephasephase == 3:
                screen.blit(font2.render('what spaces should be protected ?', True, "white"), (80, 150))
                pygame.draw.rect(screen, 'grey', (180, 330, 360, 80), 5)
                screen.blit(font1.render('Add', True, "white"), (310, 347))
            elif gamephasephase == 4:
                screen.blit(font1.render('how many fill-in candies ?', True, "white"), (60, 150))
            if gamephasephase == 0 or gamephasephase == 1 or gamephasephase == 4:
                screen.blit(font1.render(inp, True, "white"), (245, 200))
            elif gamephasephase == 2 or gamephasephase == 3:
                screen.blit(font1.render(f'({inp})', True, "white"), (245, 200))
            pygame.draw.rect(screen, 'grey', (180, 480, 360, 80), 5)
            screen.blit(font1.render('Confirm', True, "white"), (263, 497))
        elif gamescreen == 'game':
            if amodimult < ofoghimult :
                r = amodimult/2
            else:
                r = ofoghimult/2
            for i in range(satr):
                for j in range(soton):
                    if gamemap[i][j] == 'r':
                        color = 'red'
                    elif gamemap[i][j] == 'b':
                        color = 'blue'
                    elif gamemap[i][j] == 'y':
                        color = 'yellow'
                    elif gamemap[i][j] == 'p':
                        color = 'purple'
                    elif gamemap[i][j] == 'o':
                        color = 'orange'
                    elif gamemap[i][j] == 'g':
                        color = 'green'
                    else:
                        color = 'black'
                    pygame.draw.circle(screen,color,(120 + ((j+0.5)*ofoghimult),(i+0.5)*amodimult),r,500)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
def viableswap(gamemap,i,j):
    for one , two , three in [[-2,-1,0],[-1,0,1],[0,1,2]]:
        try:
            if (gamemap[i+one][j] == gamemap[i+two][j] and gamemap[i+one][j] == gamemap[i+three][j]):
                return 'i'
            elif (gamemap[i][j+one] == gamemap[i][j+two] and gamemap[i][j+one] == gamemap[i][j+three]):
                return 'j'
        except:
            pass
    return False
def popcandy(gamemap,i,j,returned,satr,soton):
    color = gamemap[i][j]
    explored = [[i,j]]
    if returned == 'i':
        higher = i
        lower = i
    elif returned == 'j':
        higher = j
        lower = j
    else:
        raise ValueError('unviable candy was given to popcandy')
    if returned == 'i':
        while higher != False and higher <satr-1:
            if gamemap[i+1][j] == color:
                higher = i+1
                explored.append([i+1,j])
            else:
                higher = False
        while lower != False  and 0 < lower:
            if gamemap[i-1][j] == color:
                lower = i-1
                explored.append([i-1,j])
            else:
                lower = False
    else:
        while higher != False and higher <soton-1:
            if gamemap[i][j+1] == color:
                higher = j+1
                explored.append([i,j+1])
            else:
                higher = False
        while lower != False  and 0 < lower:
            if gamemap[i][j-1] == color:
                lower = j-1
                explored.append([i,j-1])
            else:
                lower = False
    if returned == 'i':
        for one , two in [[-2,-1],[-1,1],[1,2]]:
            try:
                if gamemap[higher][j+one] == color and gamemap[higher][j+two] == color:
                    explored.append([higher,j+one])
                    explored.append([higher,j+two])
                    break
            except:
                pass
    elif returned == 'j':
        for one , two in [[-2,-1],[-1,1],[1,2]]:
            try:
                if gamemap[i+one][higher] == color and gamemap[i+two][higher] == color:
                    explored.append([i+one,higher])
                    explored.append([i+two,higher])
                    break
            except:
                pass
    for k,l in explored:
        gamemap[k][l] = 'poped'
    return gamemap
if __name__ == '__main__':
    main()