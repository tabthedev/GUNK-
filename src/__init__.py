import time
import pygame
from src.classes import customWindow

Running = True

clock = pygame.Clock()

window = customWindow.CustomWindow()

dt = 0

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Running = False
            break
        elif event.type == pygame.WINDOWLEAVE:
            print("나가지 마세요")

    window._screen.fill("purple")

    window.setPosition((512, 512))
    window.update()
    window2.update()

    dt = clock.tick(60)/1000

pygame.quit()