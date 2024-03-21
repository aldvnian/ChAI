class Button():
    def __init__(self, x, y, font, textInput, baseColor, hoveringColor, image):
        self.image = image
        self.xPos, self.yPos = x, y
        self.font = font
        self.baseColor, self.hoveringColor = baseColor, hoveringColor
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColor)
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
        self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))

    def apply(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def input(self, mouse):
        if mouse[0] in range(self.rect.left, self.rect.right):
            if mouse[1] in range(self.rect.top, self.rect.bottom):
                return True
        return False

    def hoveringColour(self, mouse):
        if mouse[0] in range(self.rect.left, self.rect.right):
            if mouse[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.textInput, True, self.hoveringColor)
            else:
                self.text = self.font.render(self.textInput, True, self.baseColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)
