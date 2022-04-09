from pycat.core import Sprite
from typing import List


class Turtle(Sprite):
    def on_create(self):
        return super().on_create()

    def move_forward(self, step_size: float):
        p=self.position
        super().move_forward(step_size)    
        q=self.position
        self.window.create_line(p.x, p.y, q.x, q.y)


class Rect:
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self, t: Turtle):
        t.x=self.x
        t.y=self.y
        t.rotation=0
        t.move_forward(self.width)
        t.rotation+=90
        t.move_forward(self.height)
        t.rotation+=90
        t.move_forward(self.width)
        t.rotation+=90
        t.move_forward(self.height)


class Grid:
    def __init__(self, x, y, width, height, rows, cols):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.rows=rows
        self.cols=cols
        self.make_cells()

    def make_cells(self):    
        self.cells: List[List[Rect]]=[]
        cell_height=self.height/self.rows
        cell_width=self.width/self.cols
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                x=self.x+j*cell_width
                y=self.y+i*cell_height
                row.append(Rect(x,y,cell_width,cell_height))
            self.cells.append(row)

    def draw(self, t:Turtle):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(t)