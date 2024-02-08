import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill('light gray')
font = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 20)
bigFont = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 150)
timer = pygame.time.Clock()
fps = 60
header1 = bigFont.render('Ch', True, (150, 150, 150))
header2 = bigFont.render('AI', True, (255, 165, 0))
header2Rect = header2.get_rect(midleft=(490, 200))
header1Rect = header1.get_rect(midright=(490, 200))
background = pygame.image.load('Images/background.jpg').convert_alpha()
rect = pygame.Rect(315, 400, 310, 400)

run = True
while run:
    timer.tick(fps)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))
    screen.blit(header1, header1Rect)
    screen.blit(header2, header2Rect)
    pygame.draw.rect(screen, (150, 150, 150), rect, 10)

    pygame.display.flip()
pygame.quit()
