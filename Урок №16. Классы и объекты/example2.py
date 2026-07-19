import math


class Cherepashka:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        distance_x = abs(x2 - self.x)
        distance_y = abs(y2 - self.y)

        return math.ceil(distance_x / self.s) + math.ceil(distance_y / self.s)


turtle = Cherepashka(0, 0, 2)

turtle.go_right()
turtle.go_up()

print(turtle.x, turtle.y)          # 2 2
print(turtle.count_moves(10, 6))   # 6