from pycat.core import Window, Sprite, Point
from random import randint

w=Window()

def get_random_point(x1=0, x2=w.width, y1=0, y2=w.height):
    return Point(randint(x1, x2), randint(y1, y2))

class Turtle(Sprite):
    def on_create(self):
        return super().on_create()

    def move_forward(self, step_size: float):
        p=self.position
        super().move_forward(step_size)    
        q=self.position
        w.create_line(p.x, p.y, q.x, q.y)

    def create_triangle(self, length: float):
        for _ in range(3):
            self.move_forward(length)
            self.rotation+=120

class Brush(Turtle):
    def draw_regular_polygon(self, length, sides):
        for i in range(sides):
            self.move_forward(length)
            self.rotation+=360/sides
    
    
    

b=w.create_sprite(Brush)
b.x=w.center.x
for i in range(3, 20):
    b.draw_regular_polygon(300, i)
w.run()