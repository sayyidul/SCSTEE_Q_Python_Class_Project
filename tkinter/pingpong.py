#import library
import tkinter
import time 
import random
import sys
from copy import copy

#====TAMPILAN=====
#create tampilan window
window = tkinter.Tk()
#atur ukuran window
window_dimensions = [850, 600]
#indeks 0 = x & indeks 1 = y
window.geometry(str(window_dimensions[0]) + "x" + str(window_dimensions[1]))
window.resizable(False, False)
#title
window.title("Ping Pong Game")
#menutup window ketika x atau close di tekan
window.protocol("WM_DELETE_WINDOW", sys.exit)
#frame rate window
frame_per_second = 60
#create game canvas
game_canvas = tkinter.Canvas(window, width=window_dimensions[0], height=window_dimensions[1], bd=0)
game_canvas.pack()

#==== GAME VARIABLE ====
#padle size
padle_size = [20, 120]
#mengatur posisi Y untuk kedua padle
initial_y_position = (window_dimensions[1] - padle_size[1]) / 2

#player variable
player_y_position = initial_y_position
player_y_velocity = 0
#computer variable
ai_y_position = initial_y_position
ai_y_velocity = 0

#ball variable
ball_diameter = 15
#rumus bola = (x -35 - x padle - angka y position / 2) , (y - ukuran bola / 2 ) (bagi ukuran window) 
initial_ball_position = [(window_dimensions[0] - 35 - padle_size[0]) 
                         - (int(window_dimensions[1] / 2 )), ((window_dimensions[1] - ball_diameter) / 2) 
                         - (int(window_dimensions[1] / 2))]
initial_ball_velocity = [10, 10]

ball_position = copy(initial_ball_position)
ball_velocity = copy(initial_ball_velocity)

#score variable
score = [0, 0]

#hapus global variable useless
del initial_y_position
#tampilan instruction
display_instructions = True
#optimasi posisi ball & player
optimal_position = False

#handle arrow key event
def onKeyDown(e):
    #deklarasikan global variable
    global player_y_velocity
    global ai_y_velocity
    global display_instructions

    # record variable kecepatan posisi player
    player_y_velocity_current = player_y_velocity
    ai_y_velocity_current = ai_y_velocity

    #bind perubahan arrow keys player 
    if(e.keysym == "w"):
        #start movement up when "W" press
        player_y_velocity = -10
    elif(e.keysym == "s"):
        #start movement down if s press
        player_y_velocity = 10
    
    #instuctoin gone if key press
    if(player_y_velocity_current != player_y_velocity or ai_y_velocity_current != ai_y_velocity):
        display_instructions = False

#handle arrow key  tidak di tekan
def onKeyUp(e):
    #deklarasi global variable
    global player_y_velocity
    global ai_y_velocity

    #bind arrow key jika velocity player berubah
    if(e.keysym == "w" or e.keysym == "s"):
        #stop movement either key
        player_y_velocity = 0


#====== gamelopp (untuk membuat tampilan)====
def gameloop():
    #deklarasikan global variable
    global frame_per_second
    global game_canvas
    global window_dimensions
    global player_y_position
    global padle_size
    global ball_diameter
    global ball_position
    global ball_velocity
    global player_y_position
    global ai_y_velocity
    global ai_y_position
    global display_instructions
    global optimal_position

    #call gameloop to play in frame
    window.after(int(1000 / frame_per_second), gameloop)    

    #clear game canvas
    game_canvas.delete("all")
    #buat backround color
    game_canvas.create_rectangle(0, 0, window_dimensions[0], window_dimensions[1], fill="grey", outline="black")

    #display player padle (30 pxl jarak padle)
    game_canvas.create_rectangle(30, player_y_position, 30 + padle_size[0], player_y_position + padle_size[1], fill="blue", outline="yellow")
    #display ai padle
    game_canvas.create_rectangle(window_dimensions[0] - 30, ai_y_position, (window_dimensions[0] - 30) - padle_size[0],
                                  ai_y_position + padle_size[1], fill="green", outline="yellow")
    
    #display ball
    game_canvas.create_rectangle(ball_position[0], ball_position[1], 
                                 ball_position[0] + ball_diameter, ball_position[1] + ball_diameter, fill="black", outline="white")

    #display score
    game_canvas.create_text(window_dimensions[0] / 2, 35, anchor="center", font="Arial 28 bold", fill="black", 
                            text=str(score[0]) + "          " + str(score[1]))

    #display center saparator line
    game_canvas.create_line(window_dimensions[0] / 2, 0, (window_dimensions[0] / 2), window_dimensions[1], fill="black", dash=(5,10))

    #game instructions
    if(display_instructions):
        game_canvas.create_text(window_dimensions[0] / 2 - 30, window_dimensions[1]- 40, anchor="ne", font="Arial 16 bold", fill="black",
                                text="Move WASD")
        
    player_y_position += player_y_velocity
    ai_y_position += ai_y_velocity

    #update player posisiton
    player_y_position += player_y_velocity
    #update ai position
    ai_y_position += ai_y_velocity

    #player paddle supaya tidak lewat / coalision
    if(player_y_position + padle_size[1] > window_dimensions[1]):
        player_y_position = window_dimensions[1] - padle_size[1]
    elif(player_y_position < 0):
        player_y_position = 0

    #ai paddle supaya tidak lewat / coalision
    if(ai_y_position + padle_size[1] > window_dimensions[1]):
        ai_y_position = window_dimensions[1] - padle_size[1]
    elif(ai_y_position < 0):
        ai_y_position = 0

    # update ball posisi
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    #ball coalition
    #coalition bagian atas & bawah 
    if(ball_position[1] >= window_dimensions[1] - ball_diameter or ball_position[1] <=0):
        ball_velocity[1] = -ball_velocity[1]

    #coalition bagian kiri & kanan
    #kanan
    if(ball_position[0] <= 0):
        score[1] += 1 

        #reset ball
        ball_position = copy(initial_ball_position)
        ball_velocity = copy(initial_ball_velocity)

        #reset ball variable
        optimal_position = optimalPaddlePosition(ball_velocity, ball_position, ball_diameter, padle_size)
    #kiri
    if(ball_position[0] >= window_dimensions[0] - ball_diameter):
        score[0] += 1 

        #reset ball
        ball_position = copy(initial_ball_position)
        ball_velocity = copy(initial_ball_velocity)

        #reset ball variable
        optimal_position = optimalPaddlePosition(ball_velocity, ball_position, ball_diameter, padle_size)

    # paddle coalision supaya bisa mantul
    if(((ball_position[0] >= 35 and ball_position[0] <= 35 + padle_size[0]) and 
	 	(ball_position[1] + ball_diameter >= player_y_position and 
   		ball_position[1] <= player_y_position + padle_size[1]) and 
		ball_velocity[0] <= 0) or 
        ((ball_position[0] + ball_diameter <= window_dimensions[0] - 35 and 
		ball_position[0] + ball_diameter >= (window_dimensions[0] - 35) - padle_size[0]) and 
		(ball_position[1] + ball_diameter >= ai_y_position and ball_position[1] <= ai_y_position + padle_size[1]) and 
		ball_velocity[0] >= 0)):
        ball_velocity[0] = -ball_velocity[0]

        #update optimal posistion
        if(ball_velocity[0] <= 0):
            optimal_position = False
        else:
            optimal_position = optimalPaddlePosition(ball_velocity, ball_position, ball_diameter, padle_size)
    
    # inisialisasi gerak ai mengikuti ball
    if(ball_position[0] > window_dimensions[0] * 0.65):
        if(optimal_position != False and (ai_y_position < optimal_position and ai_y_position + padle_size[1] > optimal_position)):
            ai_y_velocity = 0
        elif(optimal_position != False):
            if(ai_y_position > optimal_position):
                ai_y_velocity = -10
            if(ai_y_position < optimal_position):
                ai_y_velocity = 10

def optimalPaddlePosition(local_ball_velocity, local_ball_position, local_ball_diameter, local_padle_size):
    #deklarasikan global variable
    global window_dimensions

    #reset arugumen untuk atur nilai ball & padle
    local_ball_velocity = copy(local_ball_velocity)
    local_ball_position = copy(local_ball_position)
    local_padle_size = copy(local_padle_size)

    #ball movement hingga menyentuh pinggir x 
    while(local_ball_position[0] < window_dimensions[0] - 35 - local_padle_size[0]):
		# update ball position
        local_ball_position[0] += local_ball_velocity[0]
        local_ball_position[1] += local_ball_velocity[1]

        #atur batasan atas & bawah posisi ai
        if(local_ball_position[1] >= window_dimensions[1] - local_ball_diameter or local_ball_position[1] <= 0):
            local_ball_velocity[1] = -local_ball_velocity[1]
    
    #update paddle position 
    local_optimal_position = local_ball_position[1]

    #return optimal posisi dengan posisi random
    return local_optimal_position


# connect fungsi key
window.bind("<KeyPress>", onKeyDown)
window.bind("<KeyRelease>", onKeyUp)

gameloop()
#tampilkan window
window.mainloop()