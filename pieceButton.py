import pygame


class pieceButton:
    def __init__(self, coordinates, width, height):
        self.width = width
        self.height = height
        self.coordinates = coordinates
        self.buttonSurf = pygame.Surface((self.width, self.height))
        self.buttonSurfRect = self.buttonSurf.get_rect(bottomright=self.coordinates)

    def apply(self, screen):
        screen.blit(self.buttonSurf, self.buttonSurfRect)

    def input(self, mousePosition):
        if mousePosition[0] in range(self.buttonSurfRect.left, self.buttonSurfRect.right):
            if mousePosition[1] in range(self.buttonSurfRect.top, self.buttonSurfRect.bottom):
                return True
        return False
