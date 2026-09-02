import pygame

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working with rectangles")

soldier = pygame.image.load("avatar2.png").convert_alpha()
soldier = pygame.transform.scale(soldier, (200, 200))

rect_1 = pygame.Rect(200, 100, 150, 100)
rect_1.width = 500
rect_2 = soldier.get_rect()
rect_2.topleft = (200, 200)

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    screen.fill((255,255,255))

    screen.blit(soldier, rect_2)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect_2.x -= 5
    if key[pygame.K_d] == True:
        rect_2.x += 5
    if key[pygame.K_w] == True:
        rect_2.y -= 5
    if key[pygame.K_s] == True:
        rect_2.y += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()


