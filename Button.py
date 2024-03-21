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

    #Method that applies the image and the text of the button to the screen
    def apply(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    #Method that takes input from the mouse
    def input(self, mouse):
        if mouse[0] in range(self.rect.left, self.rect.right):
            if mouse[1] in range(self.rect.top, self.rect.bottom):
                return True
        return False

    #Method that causes the colour to changes as the mouse hovers over the button
    def hoveringColour(self, mouse):
        if mouse[0] in range(self.rect.left, self.rect.right):
            if mouse[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.textInput, True, self.hoveringColor)
            else:
                self.text = self.font.render(self.textInput, True, self.baseColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)
