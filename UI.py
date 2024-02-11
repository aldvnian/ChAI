import pygame
from Button import *

pygame.init()

timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 40)
bigFont = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 150)
getButtonImage = pygame.image.load('Images/playButton.png')
buttonImage = pygame.transform.scale(getButtonImage, (250, 75))


class mainMenu:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 1000
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('ChAI', 'ChAI')
        self.screen.fill('light gray')
        self.header1 = bigFont.render('Ch', True, (150, 150, 150))
        self.header2 = bigFont.render('AI', True, (255, 165, 0))
        self.header2Rect = self.header2.get_rect(midleft=(490, 200))
        self.header1Rect = self.header1.get_rect(midright=(490, 200))
        self.playButton = Button(buttonImage, 475, 500, 'Play a match!', font, (255, 165, 0), 	(0,128,128))
        self.settingsButton = Button(buttonImage, 475, 600, 'Settings', font, (255, 165, 0), (0,128,128))
        self.tutorialButton = Button(buttonImage, 475, 700, 'Tutorial', font, (255, 165, 0), (0,128,128))
        self.background = pygame.image.load('Images/background.jpg').convert_alpha()

    def run(self):
        run = True
        while run:
            timer.tick(fps)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.header1, self.header1Rect)
            self.screen.blit(self.header2, self.header2Rect)
            self.playButton.update(self.screen)
            self.settingsButton.update(self.screen)
            self.tutorialButton.update(self.screen)

            pygame.display.flip()
        pygame.quit()

p1 = mainMenu()
p1.run()