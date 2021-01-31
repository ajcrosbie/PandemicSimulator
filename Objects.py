import random
import pygame


class person():
    def __init__(self, width, height, safety):
        self.width = width
        self.height = height
        x = random.randrange(width)
        y = random.randrange(height)
        self.pos = (x, y)
        self.illness = safety
        self.colour = (255, 255, 255)
        self.size = 4
        self.illnessc = random.randrange(500, 2000)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        xM = random.randint(-2, 2)
        x = self.pos[0] + xM
        yM = random.randint(-2, 2)
        y = self.pos[1] + yM
        if x > self.width:
            x = self.width
        elif x < 0:
            x = 0
        if y > self.height:
            y = self.height
        elif y < 0:
            y = 0
        self.pos = (x, y)
        if self.illness == 'ill':
            self.illnessc = self.illnessc-1
            self.colour = (255, 0, 0)
            if self.illnessc == 0:
                self.illness = 'immune'
        elif self.illness == 'immune':
            self.colour = (0, 0, 255)

    def draw(self, win):
        pygame.draw.circle(win, self.colour, self.pos, self.size)
