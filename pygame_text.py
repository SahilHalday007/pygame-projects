import pygame

pygame.init()

width, height = 1028, 720

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My awesome game")

fps = 30
clock = pygame.time.Clock()

start = True

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    window.fill((255, 255, 255))
    font = pygame.font.Font("../Resources/Marcellus-Regular.ttf", 50)
    text = font.render("My Awesome Game", True, (50, 50, 50))

    window.blit(text, (350, 300))
    pygame.display.update()

    clock.tick(fps)