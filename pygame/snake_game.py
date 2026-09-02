from tkinter import*
from random import randint
import random

#constant adalah variable yang tidak akan kita ubah
GAME_WIDTH = 550
GAME_HEIGHT = 550
SPEED = 100
SPACE_SIZE = 25
BODY_PARTS = 2
SNAKE_COLOR = "black"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "grey"

class Food:
    #membuat method
    def __init__(self):
        x = random.randrange(0, GAME_WIDTH // SPACE_SIZE-2) * SPACE_SIZE
        y = random.randrange(0, GAME_HEIGHT // SPACE_SIZE-2) * SPACE_SIZE

        #koordinat
        self.coordinates = [x, y]
        
        #draw food objek di canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class Snake:
    def __init__(self):
        #body size
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # list of koordinat
        for i in range (0, BODY_PARTS):
            # tambah list koordinat awal
            self.coordinates.append([0, 0])

        # draw square
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

def next_turn(snake, food):
    x,y = snake.coordinates[0]

    # direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y +=SPACE_SIZE
    elif direction == "left":
        x -=SPACE_SIZE
    elif direction == "right":
        x +=SPACE_SIZE

    # update koordinate
    snake.coordinates.insert(0, (x,y))
    # create new grafik of snake
    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
    # update list of sqaure
    snake.squares.insert(0, square)

    # kondisional score & delet food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score +=1
        label.config(text="SCORE:{}".format(score))
        # delete foof object
        canvas.delete("food")
        food = Food()

    else:
        # delete last body part snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    
def check_collisions(snake):
    x, y = snake.coordinates[0]

    #touch edge
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_WIDTH:
        return True

    #touch another body part 
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tags="gameover")

def restart_game():
    global snake, food, score, direction

    # Reset game variables to initial values
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    score = 0
    direction = 'down'
    label.config(text="SCORE:{}".format(score))
    next_turn(snake, food)



window = Tk() 
window.title("Snace Game")
window.resizable(False, False)

score = 0
direction = 'down'

#label score
label = Label(window, text="SCORE:{}".format(score), font=('consolas', 40))
label.pack()

#canvas
canvas = Canvas(window, bg= BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

#update window
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#adjust position our window
window.eval('tk::PlaceWindow . center')

# control tombol untuk snake
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

#restart 
restart_button = Button(window, text="Restart", command=restart_game, font=('consolas', 20))
restart_button.place(x=0, y=0)

#snake object
snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop() 