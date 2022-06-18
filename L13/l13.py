from random import randint
from turtle import position
from pycat.core import Window, Sprite
from enum import Enum

w=Window()

class State(Enum):
    WAIT, LEFT, RIGHT=range(3)

class Barrel(Sprite):
    def on_create(self):
        self.image='img/barrel1.png'
        self.scale=3
        self.time=0

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete()
        self.time+=dt
        if self.time>0.05:
            print(self.image)
            if self.image=='img/barrel1.png':
                self.image='img/barrel2.png'
            elif self.image=='img/barrel2.png':
                self.image='img/barrel3.png'
            elif self.image=='img/barrel3.png':
                self.image='img/barrel4.png'
            elif self.image=='img/barrel4.png':
                self.image='img/barrel1.png'
            self.time=0


class Ape(Sprite):
    T1=1
    T2=0.25
    def on_create(self):
        self.state=State.WAIT
        self.image='img/ape_waiting.png'
        self.x=w.center.x
        self.y=200
        self.scale=2
        self.t=0
        self.lr=0

    def throw_barrel(self):
        w.create_sprite(Barrel, position=self.position,rotation=randint(0, 360))

    def on_update(self, dt):
        self.t+=dt
        if self.state is State.WAIT:
            if self.t>Ape.T1:
                self.image='img/ape_angry2.png'
                self.state=State.LEFT
                self.t=0
        elif self.state is State.LEFT:
            if self.t>Ape.T2:
                self.image='img/ape_angry1.png'
                self.state=State.RIGHT
                self.t=0
                self.lr+=1
        elif self.state is State.RIGHT:
            if  self.lr==1 and self.t>Ape.T2:
                self.image='img/ape_angry2.png'
                self.state=State.LEFT
                self.t=0
            if self.lr==2 and self.t>Ape.T2:
                self.image='img/ape_waiting.png'
                self.state=State.WAIT
                self.t=0
                self.lr=0
                self.throw_barrel()
            
            






w.create_sprite(Ape)
w.run()