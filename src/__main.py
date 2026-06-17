import pygame


Running = True

pygame.init()

window = pygame.Window("GUNK!", (1920,1080), (0,0), fullscreen=True)
clock = pygame.Clock()

dt = 0

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Running = False
            break
        elif event.type == pygame.WINDOWLEAVE:
            print("나가지 마세요")
            window.show
    
    dt = clock.tick(60)/1000

pygame.quit()