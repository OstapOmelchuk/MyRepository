import random


class Ball:
    def __init__(self, canvas, color, my_brd, enemy_brd):
        self.counter = 0
        self.speed = 1
        self.canvas = canvas
        self.my_brd = my_brd
        self.enemy_brd = enemy_brd
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = 1
        self.game_over = False
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_my_brd(self, pos):
        brd_pos = self.canvas.coords(self.my_brd.my_id)
        if pos[2] >= brd_pos[0] and pos[0] <= brd_pos[2]:
            if pos[3] >= brd_pos[1] and pos[3] <= brd_pos[3]:
                self.counter += 1
                if self.counter % 2 == 0:
                    self.speed += 0.1
                return True
        return False

    def hit_enemy_brd(self, pos):
        brd_pos = self.canvas.coords(self.enemy_brd.enemy_id)
        if pos[2] >= brd_pos[0] and pos[0] <= brd_pos[2]:
            if pos[1] <= brd_pos[3] and pos[1] >= brd_pos[1]:
                self.counter += 1
                if self.counter % 2 == 0:
                    self.speed += 0.1
                return True
        return False

    def draw_ball(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.game_over = True
        if pos[3] >= self.canvas_height:
            self.game_over = True
        if self.hit_enemy_brd(pos) == True:
            self.y = self.speed
        if self.hit_my_brd(pos) == True:
            self.y = -self.speed
        if pos[0] <= 0:
            self.x = self.speed
        if pos[2] >= self.canvas_width:
            self.x = -self.speed
    