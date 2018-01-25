from tkinter import *
from expressions import Function


class Displayer(Canvas):
    def __init__(self, root,  x_min, x_max, y_min, y_max, x_scale=1, y_scale=1, canvas_size=500):
        super(Displayer, self).__init__(root, width=canvas_size, height=canvas_size, bg="white")
        self.canvas_size = canvas_size
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def add_axis(self):
        self.y_axis = self.create_line(self.canvas_size // 2, self.canvas_size, self.canvas_size // 2, 0,
                                       width=1, arrow=LAST)
        self.x_axis = self.create_line(0, self.canvas_size // 2, self.canvas_size, self.canvas_size // 2,
                                       width=1, arrow=LAST)

        # marking x_axis
        for i in range(self.canvas_size + 1):
            if i % (self.canvas_size / 10) == 0:
                k = -self.canvas_size // 2 + i
                self.create_line(k + self.canvas_size // 2, -2 + self.canvas_size // 2,
                                 k + self.canvas_size // 2, 2 + self.canvas_size // 2,
                                 width=0.25, fill='black')

                self.create_text(k + self.canvas_size // 2, -10 + self.canvas_size // 2,
                                 text=str(k * self.y_scale * (self.x_max - self.x_min) // (self.x_scale * self.canvas_size)), fill='black',
                                 font=('Helvectica', '10'))
        # marking y_axis
        for j in range(self.canvas_size + 1):
            if j % (self.canvas_size / 10) == 0:
                k = -self.canvas_size // 2 + j
                if k != 0:
                    self.create_line(-2 + self.canvas_size // 2, k + self.canvas_size // 2, 2 + self.canvas_size // 2, k + self.canvas_size // 2,
                                     width=0.25, fill='black')

                    self.create_text(15 + self.canvas_size // 2, k + self.canvas_size // 2,
                                     text=str(-k * (self.y_max - self.y_min) // self.canvas_size), fill='black',
                                     font=('Helvectica', '10'))

    def add_function(self, f, color="black"):
        previous_point = [0, 0]
        for x in range(-self.canvas_size // 2, self.canvas_size // 2 + 1):
            x = x * (self.x_max - self.x_min) / self.canvas_size
            point = [x * self.canvas_size // (self.x_max - self.x_min) + self.canvas_size // 2,
                     self.canvas_size // 2 - (f(x / self.x_scale) * self.y_scale) * self.canvas_size // (self.y_max - self.y_min)]
            self.create_line(previous_point, point, fill=color)
            previous_point = point

    def add_point(self, x, y, color="black"):
        self.create_oval(
            self.x_scale * x - 1,
            self.canvas_size - self.y_scale * y + 1,
            self.x_scale * x + 1,
            self.canvas_size - self.y_scale * y - 1,
            fill=color)

    def rescale(self, f, x_min, x_max, y_min, y_max):
        self.x_max = x_max
        self.x_min = x_min
        self.y_min = y_min
        self.y_max = y_max
        self.delete(ALL)
        self.add_axis()
        f = Function.parse(f)
        self.add_function(f.calculate)