import pygame

pygame.init()

width, height = 1280, 720

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My awesome game")

fps = 30
clock = pygame.time.Clock()

# colors
c = {
    "lightGreen": (189, 209, 197),
     "lightOrange": (238, 204, 140),
     "lightPink": (232, 178, 152),
     "darkPink": (211, 162, 157),
     "darkGreen": (158, 171, 162),
     "darkGray": (128, 126, 126),
     "lightGray": (204, 204, 204),
     "darkBrown": (89, 61, 61),
     "white": (255, 255, 255),
     "black": (0, 0, 0)
}

# load images
imgBackground = pygame.image.load("Resources/Project - GUI/background.png").convert()
imgDesign = pygame.image.load("Resources/Project - GUI/design.png").convert_alpha()
imgIcon1 = pygame.image.load("Resources/Project - GUI/icon1.png").convert_alpha()
imgIcon2 = pygame.image.load("Resources/Project - GUI/icon2.png").convert_alpha()
imgIcon3 = pygame.image.load("Resources/Project - GUI/icon3.png").convert_alpha()
imgIcon4 = pygame.image.load("Resources/Project - GUI/icon4.png").convert_alpha()
imgIcon5 = pygame.image.load("Resources/Project - GUI/icon5.png").convert_alpha()
imgToggleOn = pygame.image.load("Resources/Project - GUI/toggleOn.png").convert()
imgToggleOff = pygame.image.load("Resources/Project - GUI/toggleOff.png").convert()
imgShadow = pygame.image.load("Resources/Project - GUI/shadow.png").convert_alpha()


# list of window pads
pads = [{"no": 1, "color": c["lightGreen"], "text": "Original", "icon": imgIcon2},
        {"no": 2, "color": c["lightOrange"], "text": "Grey Scale", "icon": imgIcon3},
        {"no": 3, "color": c["lightPink"], "text": "Edges", "icon": imgIcon4},
        {"no": 4, "color": c["darkPink"], "text": "Contours", "icon": imgIcon5}]


def drawWindowPad(pos, color, text, icon):
    xo, yo, w, h = pos

    # add shadow
    window.blit(imgShadow, (xo, yo+h-66))

    # header rectangle
    pygame.draw.rect(window, color, (xo, yo, w, 64),
                     border_top_left_radius=10, border_top_right_radius=10)
    # image area white
    pygame.draw.rect(window, c['white'], (xo, yo+64, w, h-87),
                     border_bottom_left_radius=10, border_bottom_right_radius=10)
    # icon
    window.blit(icon, (xo+20, yo+12))

    # text
    font = pygame.font.Font("Resources/Marcellus-Regular.ttf", 20)
    text = font.render("Original", True, c['darkBrown'])
    window.blit(text, (xo+82, yo+20))

def drawAll():
    w, h = 312, 301
    drawWindowPad((484, 57, w, h), pads[0]['color'], pads[0]['text'], pads[0]['icon'])
    window.blit(imgIcon1, (100, 100))

# main loop
start = True

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()


    window.blit(imgBackground, (0, 0))
    # imgDesign.set_alpha(50)
    # window.blit(imgDesign, (0, 0))
    drawAll()

    pygame.display.update()

    clock.tick(fps)
