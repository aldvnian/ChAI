class Button():
    def __init__(self, image, x, y, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos, self.y_pos = x, y
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.textRect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def apply(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def input(self, mouse):
        if mouse[0] in range(self.rect.left, self.rect.right):
            if mouse[1] in range(self.rect.top, self.rect.bottom):
                return True
        return False

    def hoveringColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)