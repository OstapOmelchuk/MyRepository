from tkinter import *
from BallClass import Ball
from BoardClass import Board
from EnemyBoardClass import EnemyBoard
from MenuClass import Menu
import random
import time
import keyboard

def start_game():
    tk = Tk()
    tk.resizable(0, 0)  
    tk.title("GAME")
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    brd = Board(canvas)
    enemy_brd = EnemyBoard(canvas)
    ball = Ball(canvas, "red", brd, enemy_brd)
    while 1:
        if ball.game_over == False:
            ball.draw_ball()
            brd.move_board()
            enemy_brd.move_enemy_board()
        else:
            canvas.destroy()
            tk.destroy() 
        # tk.update_idletasks()
        tk.update()
        time.sleep(0.01)


menu = Tk()
b1 = Button(menu, text = "Play Game", height=5, width = 20, command = start_game)
b2 = Button(menu, text = "Exit", height=5, width = 20, command = menu.destroy)
b1.pack()
b2.pack()
menu.mainloop()

