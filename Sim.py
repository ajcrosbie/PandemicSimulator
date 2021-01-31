import pygame
import random
import Objects


def redrawWin(people, win):
    win.fill((0, 0, 0))
    for i in people:
        i.draw(win)
    pygame.display.update()


def populate(width, height):
    people = []
    for i in range(100):
        people.append(Objects.person(width, height, 'safe'))
    people.append(Objects.person(width, height, 'ill'))
    return people


def main():
    width = 1000
    height = 500
    win = pygame.display.set_mode((width, height))
    people = populate(width, height)
    v = True
    while v:
        for i in people:
            i.move()
        redrawWin(people, win)


if __name__ == '__main__':
    main()
