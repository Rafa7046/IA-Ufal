import pygame

pygame.init()

size = width, height = 512,512

while 1:

    screen = pygame.display.set_mode(size)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [0, 64, 64, 128])