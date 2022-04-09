from pycat.core import Window, Sprite

w=Window()

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
            t.move_forward(length)
            t.rotation+=120



t=w.create_sprite(Turtle)
# t.position=w.center
for i in range(100, 900, 20):
    t.create_triangle(i)
    
# for i in range(36):
#     for _ in range(3):
#         t.move_forward(200)
#         t.rotation+=120
#     t.rotation+=10

w.run()