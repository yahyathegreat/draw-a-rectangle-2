import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 225), pygame.rect(30, 30, 60, 60))
    pygame.display.flip()
import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))
GREEN = (0, 255, 0)
pygame.draw.circle(window, GREEN, (300, 300), 50)
pygame.draw.circle(window, GREEN, (100, 100), 550, 3)
pygame.display.update()
running =  True
while running:
    for event in pygame.get():
        if event.type == pygame.QUIT:
             running = False
pygame.QUIT