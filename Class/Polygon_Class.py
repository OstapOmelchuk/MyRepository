class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides

    def input_sides(self):
        sides = []
        flag = False
        print("Enter the lengthof sides:")
        while not flag:
            print("The length of each side must be less than the sum of the others!")
            for x in range(self.num_of_sides):
                flag_2 = True
                while flag_2:
                    i = int(input(f"The side (> 0) #{x + 1} = "))
                    if i > 0:
                        flag_2 = False
                sides.append(i)
            if self.num_of_sides > 2:
                flag = self.sides_checker(sides)
            flag = True
        return sides

    def sides_checker(self, lst):
        k = 0
        for i in range(len(lst)):
            if sum(lst)-lst[i] <= lst[i]:
                k += 1
        if k > 0:
            return False
        return True