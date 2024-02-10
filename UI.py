import pygame

pygame.init()

timer = pygame.time.Clock()
fps = 60


class mainMenu:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 1000
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.screen.fill('light gray')
        self.font = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 20)
        self.bigFont = pygame.font.Font('Font/syn-nova/SYNNova-Normal.otf', 150)
        self.header1 = self.bigFont.render('Ch', True, (150, 150, 150))
        self.header2 = self.bigFont.render('AI', True, (255, 165, 0))
        self.header2Rect = self.header2.get_rect(midleft=(490, 200))
        self.header1Rect = self.header1.get_rect(midright=(490, 200))
        self.background = pygame.image.load('Images/background.jpg').convert_alpha()
        self.rect = pygame.Rect(315, 400, 310, 400)

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
            pygame.draw.rect(self.screen, (150, 150, 150), self.rect, 10)

            pygame.display.flip()
        pygame.quit()

p1 = mainMenu()
p1.run()
class button:
    def __init__(self, image, x, y, width, height, font, textInput, baseColour, hoveringColour):
        self.image = image
        self.x, self.y = x, y
        self.textInput = textInput
        self.baseColour = baseColour
        self.hoveringColour = hoveringColour
        self.font = font
        self.width = width
        self.height = height
        self.text = self.font.render(self.textInput, True, self.baseColour)