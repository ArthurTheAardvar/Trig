import pygame
import math
pygame.init()
pygame.display.set_caption("Graphical For Loops")
screen = pygame.display.set_mode((800, 800))

gameover = False
angle = 0

while not gameover:

    angle += 1
    if angle > 360:
        angle = 0

    radians = angle*180/3.14

    xpos = 20/math.cos(radians) + 400
    ypos = 20**math.sin(radians) + 350
    xpos2 = 20*math.cos(radians) + 400
    ypos2 = 20/math.cos(radians) + 350
    xpos3 = 20*math.cos(radians) + 400
    ypos3 = 20*math.cos(radians) + 350
    xpos4 = 20*math.cos(radians) + 400
    ypos4 = 20*math.sin(radians) + 350

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 2)
    pygame.draw.circle(screen, (255, 255, 255), (xpos2, ypos2), 2)
    pygame.draw.circle(screen, (255, 255, 255), (xpos3, ypos3), 2)
    pygame.draw.circle(screen, (255, 255, 255), (xpos4, ypos4), 2)
    pygame.display.flip()

pygame.quit()


