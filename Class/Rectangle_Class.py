from Polygon_Class import Polygon

class Rectangle(Polygon):
    def __init__(self):
        self.num_of_sides = 2
        k = self.input_sides()
        self.a = k[0]
        self.b = k[1]

    def rct_square(self, a, b):
        return f"Square = {a * b}"

rect = Rectangle()
print(rect.rct_square(rect.a, rect.b))

