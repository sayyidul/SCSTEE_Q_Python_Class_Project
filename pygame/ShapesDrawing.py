import pygame
pygame.init()

#Membuat Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working with shapes")

#warna screen
run = True
while run == True :
    screen.fill((255,255,255))

    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 150, 150),
                     width= 5, border_bottom_right_radius= 25,
                     border_top_left_radius= 25)
    pygame.draw.circle(screen, (0, 255, 0), (120, 300), 60, width=7)
    pygame.draw.ellipse(screen, (0, 0, 255), (220, 100, 150, 75))
    pygame.draw.arc(screen, (0, 255, 255), (220, 250, 150, 150), 0, 3.14, width=5)
    pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, (255, 0, 255), (400, 150), pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()