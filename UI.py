import pygame
from Button import *
from Game import *

pygame.init()

timer = pygame.time.Clock()
fps = 60
smallFont = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 20)
font = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 30)
mediumFont = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 40)
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
        self.playButton = Button(475, 300, font, 'Play a match!', (255, 165, 0), (0, 128, 128), buttonImage)
        self.settingsButton = Button(475, 400, font, 'Settings', (255, 165, 0), (0, 128, 128), buttonImage)
        self.tutorialButton = Button(475, 500, font, 'Tutorial', (255, 165, 0), (0, 128, 128), buttonImage)

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

            self.playButton.hoveringColour(mouse)
            self.settingsButton.hoveringColour(mouse)
            self.tutorialButton.hoveringColour(mouse)

            pygame.display.flip()
        pygame.quit()


class settings:
    def __init__(self):
        self.screen = pygame.display.set_mode([1000, 700])
        self.screen.fill('dark gray')
        self.backButton = Button(500, 650, font, 'Back', (255, 165, 0), (255, 0, 0), buttonImage)
        self.text = font.render('The settings screen is still on development', True, 'black')


    def run(self):
        run = True
        while run:
            timer.tick(fps)
            mouse = pygame.mouse.get_pos()
            self.screen.blit(self.text, (215, 300))
            self.backButton.apply(self.screen)
            self.backButton.hoveringColour(mouse)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.backButton.input(mouse):
                        mainMenu(pygame.display.set_mode([1000, 700]))

            pygame.display.flip()
        pygame.quit()


class tutorial:
    def __init__(self):
        self.screen = pygame.display.set_mode([1000, 700])
        self.screen.fill('orange')
        self.text = mediumFont.render('How to play:', True, 'white')
        self.text2 = font.render('•To move a piece to the desired square,', True, 'black')
        self.text3 = font.render(' press on the piece and then press on the square', True, 'black')
        self.text4 = font.render('•The AI will place a move afterwards and the turn is', True, 'black')
        self.text5 = font.render('going to come back to you', True, 'black')
        self.text6 = font.render('•Castling, en passant and piece promotion are', True, 'black')
        self.text7 = font.render('special cases so be wary of them!', True, 'black')
        self.box = pygame.draw.rect(self.screen, 'black', pygame.Rect(45, 73, 230, 60), 4)
        self.backButton = Button(500, 650, font, 'Back', (255, 165, 0), (255, 0, 0), buttonImage)

    def run(self):
        run = True
        while run:
            timer.tick(fps)
            mouse = pygame.mouse.get_pos()

            self.screen.blit(self.text, (50, 75))
            self.screen.blit(self.text2, (50, 150))
            self.screen.blit(self.text3, (50, 225))
            self.screen.blit(self.text4, (50, 290))
            self.screen.blit(self.text5, (50, 365))
            self.screen.blit(self.text6, (50, 440))
            self.screen.blit(self.text7, (50, 510))
            self.backButton.apply(self.screen)
            self.backButton.hoveringColour(mouse)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.backButton.input(mouse):
                        mainMenu(pygame.display.set_mode([1000, 700]))
            pygame.display.flip()
        pygame.quit()
