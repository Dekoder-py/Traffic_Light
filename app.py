import pygame
from itertools import cycle
from random import randint

lights = [
    ('green', 5000),
    ('orange', 1000),
    ('red', 7000)
]
colors = cycle(lights)

pygame.init()
screen = pygame.display.set_mode((1000,800))
screen.fill("#1e1e2e")
pygame.display.set_caption("Traffic Light")

def red_off():
    pygame.draw.circle(screen, "#f38ba8", (500,600), 60, 0)

def red_on():
    pygame.draw.circle(screen, "red", (500,600), 60, 0)

def orange_off():
    pygame.draw.circle(screen, "#fab387", (500,400), 60, 0)

def orange_on():
    pygame.draw.circle(screen, "orange", (500,400), 60, 0)

def green_off():
    pygame.draw.circle(screen, "#a6e3a1", (500,200), 60, 0)

def green_on():
    pygame.draw.circle(screen, "green", (500,200), 60, 0)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    c,s = next(colors)
    s = randint(500,s)
    if c == "red":
        red_on()
        orange_off()
        green_off()
    elif c == "orange":
        red_off()
        orange_on()
        green_off()
    elif c == "green":
        red_off()
        orange_off()
        green_on()

    pygame.display.flip()
    pygame.time.wait(s)
