import pygame

quit = False
pygame.init()
display = pygame.display.set_mode((640,480))
sprite_sheet = pygame.image.load('PlayerSprite.png').convert()

# by default, display the first sprite
image_number = 0

while quit == False:
    event = pygame.event.poll()
    no_more_events = True if event == pygame.NOEVENT else False

    # handle events (update game state)
    while no_more_events == False:
        if event.type == pygame.QUIT:
            quit = True
            break
        elif event.type == pygame.NOEVENT:
            no_more_events = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                image_number = 0
            elif event.key == pygame.K_RIGHT:
                image_number = 1

        event = pygame.event.poll()

    if quit == False:
        # redraw the screen
        display.fill(pygame.Color('white'))
        area = pygame.Rect(image_number * 100, 0, 100, 150)
        display.blit(sprite_sheet, (0,0), area)
        pygame.display.flip()
