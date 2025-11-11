import cv2
import numpy as np
import pygame
import random as r
from cvzone.HandTrackingModule import HandDetector

# initialize and set pygame window
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

fps = 30
clock = pygame.time.Clock()

# set videocam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# load images
imgBalloon = pygame.image.load('../Resources/Project - Balloon Pop/Balloons/BalloonRed.png').convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 300

# variables
speed = 50

# create detector
detector = HandDetector(detectionCon=0.8, maxHands=1)


def reset_balloon():
    rectBalloon.x = r.randint(100, img.shape[0] - 100)
    rectBalloon.y = img.shape[0] + 50



# main loop
start = True

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic

    # OpenCV
    success, img = cap.read()
    hands, img = detector.findHands(img)

    rectBalloon.y -= speed # move the balloon up

    # check if balloon reached top
    if rectBalloon.y  < 0:
        reset_balloon()


    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))


    window.blit(imgBalloon, rectBalloon)


    # update display
    pygame.display.update()
    clock.tick(fps)



