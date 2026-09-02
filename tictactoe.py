import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TicTacToe")

#variable
line_width = 5
mark = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

#define colours
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#define font
font = pygame.font.SysFont(None, 40)

#create again rectangle
again_rect = Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 160, 50)

def draw_grid():
    background = (255, 255, 200)
    grid = (50,50,50,50)
    screen.fill(background)
    for x in range (1,3) :
        pygame.draw.line(screen, grid, (0, x * 100), (SCREEN_WIDTH, x * 100))
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, SCREEN_HEIGHT))

for x in range(3):
    row = [0] * 3
    mark.append(row)

def draw_mark():
    x_pos = 0
    for x in mark:
        y_pos = 0
        for y in x :
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 +85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 +15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos +=1
        x_pos +=1

def check_winner():
    global winner
    global game_over
    y_pos = 0

    for x in mark:
        # check the collumn
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True

        # check rows
        if mark[0][y_pos] + mark[1][y_pos] + mark[2][y_pos] == 3:
            winner = 1
            game_over = True
        if mark[0][y_pos] + mark[1][y_pos] + mark[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos *= 1

    # cross checking
    if mark[0][0] + mark [1][1] + mark [2][2] == 3 or mark [2][0] + mark [1][1] + mark [0][2] == 3:
        winner = 1
        game_over = True
    if mark[0][0] + mark [1][1] + mark [2][2] == 3 or mark [2][0] + mark [1][1] + mark [0][2] == -3:
        winner = 2
        game_over = True

def draw_winner(winner):
    win_text = "Player" + str(winner) + " Wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 50 ))
    screen.blit(win_img, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10))

    again_text = 'Play Again ? '
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (SCREEN_WIDTH // 2-80, SCREEN_HEIGHT // 2 + 10))

run = True
while run == True :
    draw_grid()
    draw_mark()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False :
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True :
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos [0]
                cell_y = pos [1]
                if mark[cell_x // 100][cell_y // 100] == 0 :
                    mark[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False :
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True :
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                mark = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    mark.append(row)

    pygame.display.update()
pygame.quit()


    

                    