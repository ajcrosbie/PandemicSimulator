import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
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
    for i in range(15):
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
    getInfo = 0
    getInfoC = 10
    end = 10000
    ills = []
    safes = []
    deads = []
    immunes = []
    while v:
        getInfo = getInfo + 1
        for i in people:
            i.move()
        segment = segmentFinder(people, width, height)
        for i in range(len(segment)):
            for x in segment[i]:
                for g in segment[i]:
                    if transmitionArea(x, g):
                        if g.illness == 'immune' or x.illness == 'immune':
                            pass
                        elif g.illness == 'dead' or x.illness == 'dead':
                            pass
                        elif g.illness == 'ill' or x.illness == 'ill':
                            g.illness = 'ill'
                            x.illness = 'ill'
        if getInfo % getInfoC == 0:
            ill = 0
            safe = 0
            dead = 0
            immune = 0
            for i in people:
                if i.illness == 'ill':
                    ill = ill+1
                elif i.illness == 'safe':
                    safe = safe+1
                elif i.illness == 'dead':
                    dead = dead + 1
                elif i.illness == 'immune':
                    immune = immune + 1
            ills.append(ill)
            safes.append(safe)
            deads.append(dead)
            immunes.append(immune)
        redrawWin(people, win)
        try:
            if getInfo % end == 0 or ills[-1] == 0:
                v = False
        except:
            pass
    pygame.display.quit()
    v = []
    for i in range(getInfo//getInfoC):
        v.append(getInfoC*i)
    plt.plot(v, deads, 'g')
    plt.plot(v, ills, 'r')
    plt.plot(v, safes, 'y')
    plt.plot(v, immunes, 'b')
    plt.ylabel(f"people {len(people)}")
    plt.xlabel(f"frames")
    plt.show()


if __name__ == '__main__':
    main()
