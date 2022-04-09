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
            self.move_forward(length)
            self.rotation+=120

class Brush(Turtle):
    def on_update(self, dt):
        self.point_toward_mouse_cursor()
        self.move_forward(5)
    
    

w.create_sprite(Brush)

w.run()