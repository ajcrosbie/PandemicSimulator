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

    def move(self):
        xM = random.randint(-2, 2)
        x = self.pos[0] + xM
        yM = random.randint(-2, 2)
        y = self.pos[1] + yM
        if x > self.height:
            x = self.height
        elif x < 0:
            x = 0
        if y > self.width:
            y = self.width
        elif y < 0:
            y = 0
        self.pos = (x, y)

    def draw(self, win):
        pygame.draw.circle(win, self.colour, self.pos, self.size)
