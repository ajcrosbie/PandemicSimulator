import pygame
import random
import numpy as np
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
    for i in range(10):
        people.append(Objects.person(width, height, 'ill'))
    return people


def segmentFinder(people, width, height):
    q = [[], [], [], [], [], [], [], []]
    for i in people:
        if i.pos[0] < width//4 and i.pos[1] < height//2:
            q[0].append(i)
        elif i.pos[0] < width//4*2 and i.pos[1] < height//2:
            q[1].append(i)
        elif i.pos[0] < width//4*3 and i.pos[1] < height//2:
            q[2].append(i)
        elif i.pos[0] < width//4*4 and i.pos[1] < height//2:
            q[3].append(i)
        elif i.pos[0] < width//4 and i.pos[1] < height//1:
            q[4].append(i)
        elif i.pos[0] < width//4*2 and i.pos[1] < height//1:
            q[5].append(i)
        elif i.pos[0] < width//4*4 and i.pos[1] < height//1:
            q[6].append(i)
        elif i.pos[0] < width//4*4 and i.pos[1] < height//1:
            q[7].append(i)
    return q


def transmitionArea(A1, A2):
    g = (A1.size + A2.size)
    return np.linalg.norm(np.array([A1.pos[0], A1.pos[1]]) -
                          np.array([A2.pos[0], A2.pos[1]])) < g


def main():
    width = 750
    height = 375
    win = pygame.display.set_mode((width, height))
    people = populate(width, height)
    v = True
    while v:
        for i in people:
            i.move()
        segment = segmentFinder(people, width, height)
        for i in range(len(segment)):
            for x in segment[i]:
                for g in segment[i]:
                    if transmitionArea(x, g):
                        if g.illness == 'immune' or x.illness == 'immune':
                            pass
                        elif g.illness == 'ill' or x.illness == 'ill':
                            g.illness = 'ill'
                            x.illness = 'ill'
        redrawWin(people, win)


if __name__ == '__main__':
    main()
