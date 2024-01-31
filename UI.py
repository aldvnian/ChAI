import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesandbold.ttf', 20)
bigFont = pygame.font.Font('freesandbold.ttf', 45)
timer = pygame.time.Clock()
fps = 60

run = True
while run:
    timer.tick(fps)
    screen.fill('light gray')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()