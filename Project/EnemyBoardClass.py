import keyboard

class EnemyBoard:
    def __init__(self, canvas):
        self.canvas = canvas
        self.enemy_id = canvas.create_rectangle(0, 25, 70, 35, fill="green")
        self.canvas.move(self.enemy_id, 225, -20)
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)

    def turn_right(self, evnt):
        self.x = 10

    def turn_left(self, evnt):
        self.x = -10

    def move_enemy_board(self):
        self.canvas.move(self.enemy_id, self.x, 0)
        pos = self.canvas.coords(self.enemy_id)
        if pos[0] < 0:
            self.canvas.move(self.enemy_id, -pos[0], 0)
        elif pos[2] >= self.canvas_width:
            self.canvas.move(self.enemy_id, -(pos[2]-self.canvas_width), 0)
        self.x = 0
            
