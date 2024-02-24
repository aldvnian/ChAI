import pygame
from Button import *
from Game import *

pygame.init()

timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 40)
bigFont = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 150)
getButtonImage = pygame.image.load('Images/playButton.png')
buttonImage = pygame.transform.scale(getButtonImage, (250, 75))
pygame.display.set_caption('ChAI', 'ChAI')

class mainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.run = True
        self.fps = 60
        self.timer = pygame.time.Clock()
        self.screen.fill('light gray')
        self.header1 = bigFont.render('Ch', True, (150, 150, 150))
        self.header2 = bigFont.render('AI', True, (255, 165, 0))
        self.header2Rect = self.header2.get_rect(midleft=(490, 100))
        self.header1Rect = self.header1.get_rect(midright=(490, 100))
        self.background = pygame.image.load('Images/background.jpg').convert_alpha()
        self.playButton = Button(buttonImage, 475, 300, 'Play a match!', font, (255, 165, 0), (0, 128, 128))
        self.settingsButton = Button(buttonImage, 475, 400, 'Settings', font, (255, 165, 0), (0, 128, 128))
        self.tutorialButton = Button(buttonImage, 475, 500, 'Tutorial', font, (255, 165, 0), (0, 128, 128))

        while self.run:
            timer.tick(fps)
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.playButton.input(mouse):
                        Game.displayBoard()

                    elif self.settingsButton.input(mouse):
                        screen.fill('black')
                        p1 = settings()
                        p1.run()

                    elif self.tutorialButton.input(mouse):
                        screen.fill('black')
                        p1 = tutorial()
                        p1.run()

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.header1, self.header1Rect)
            self.screen.blit(self.header2, self.header2Rect)

            self.playButton.apply(self.screen)
            self.settingsButton.apply(self.screen)
            self.tutorialButton.apply(self.screen)

            self.playButton.hoveringColor(mouse)
            self.settingsButton.hoveringColor(mouse)
            self.tutorialButton.hoveringColor(mouse)

            pygame.display.flip()
        pygame.quit()

class settings:
    def __init__(self):
        self.screen = pygame.display.set_mode([1000, 700])
        self.screen.fill('dark gray')
        self.text = font.render('The settings screen is still on development!', True, 'white')

    def run(self):
        run = True
        while run:
            timer.tick(fps)
            self.screen.blit(self.text, (175, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.flip()
        pygame.quit()

class tutorial:
    def __init__(self):
        self.screen = pygame.display.set_mode([1000, 700])
        self.screen.fill('dark gray')
        self.text = font.render('The tutorial screen is still on development!', True, 'white')

    def run(self):
        run = True
        while run:
            timer.tick(fps)
            self.screen.blit(self.text, (175, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.flip()
        pygame.quit()
