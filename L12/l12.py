from pycat.core import Window, Sprite, Label, Point
from enum import Enum, auto
from math import pi, sqrt, cos
from pycat.math import radian_to_degree, get_distance

w=Window()

class PlayButton(Sprite):
    def on_create(self):
        self.scale=100
        self.x=150
        self.y=150
        self.color=(0, 255, 0)

    def on_left_click(self):
        time_label.switch_state()
        

class ResetButton(Sprite):
    def on_create(self):
        self.scale=100
        self.x=350
        self.y=150
        self.color=(255, 0, 0)
        
    def on_left_click(self):
        time_label.reset()


class TimeLabel(Label):

    class State(Enum):
        PLAY=auto()
        STOP=auto()

    def on_create(self):
        self.time=0
        self.text='0'
        self.font_size=100
        self.state=self.State.STOP

    def switch_state(self):
        if self.state is self.State.PLAY:
            self.state=self.State.STOP
        else:
            self.state=self.State.PLAY

    def reset(self):
        self.state=self.State.STOP
        self.time=0
        self.text='0'

    def on_update(self, dt: float):
        if self.state is self.State.STOP:
            pass
        elif self.state is self.State.PLAY:
            self.time+=dt
            self.text=str(round(self.time, 2))



w.create_sprite(PlayButton)
w.create_sprite(ResetButton)
time_label=w.create_label(TimeLabel)



class Pendulum(Sprite):

    def on_create(self):
        self.is_visible=False
        self.a0=pi/4
        self.angle=pi/4
        self.anchor=w.create_circle(x=w.width/2, y=w.height, radius=20)
        self.pendulum=w.create_circle(x=w.width/2, y=50, radius=50)
        self.line=w.create_line(self.pendulum.x, self.pendulum.y, self.anchor.x, self.anchor.y)
        a, b, c, d=self.line.position
        self.distance=get_distance(Point(a, b), Point(c, d))
        self.w=sqrt(9.8/self.distance)

    def draw_pendulum(self):
        x, y=self.anchor.position
        self.position=Point(x, y)
        self.rotation=radian_to_degree(self.angle)-90
        self.move_forward(self.distance)
        self.pendulum.position=self.position.as_tuple()
        self.line.x=self.position.x
        self.line.y=self.position.y
        self.time=0


    def on_update(self, dt):
        self.time+=dt
        self.angle=self.a0*cos(self.w*self.time)
        self.draw_pendulum()
        


p=w.create_sprite(Pendulum)
p.draw_pendulum()
w.run()