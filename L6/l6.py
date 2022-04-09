from time import sleep
from pycat.core import Window, Sprite, Color
from typing import List
from random import randint

R=10
C=15
CELL_SIZE=100
X0=Y0=CELL_SIZE/2


w=Window(width=C*CELL_SIZE, height=R*CELL_SIZE)

class Cell(Sprite):

    def on_create(self):
        self.scale=CELL_SIZE-1
        
    def setup(self, i, j):
        self.x=X0+j*CELL_SIZE
        self.y=Y0+i*CELL_SIZE
        self.i=i
        self.j=j
    
    def toggle(self):
        if self.color==Color.RED:
            self.color=Color.WHITE
        else:
            self.color=Color.RED
    
    def on_left_click(self):
        toggle_neighbors(self.i, self.j)
        check_for_win()


grid: List[List[Cell]] = []
for i in range(R):
    r=[]
    for j in range(C):
        c=w.create_sprite(Cell)
        c.setup(i, j)
        r.append(c)
    grid.append(r)


def toggle_grid(i, j):
    if i<0:
        return
    elif i>R-1:
        return
    if j<0:
        return
    elif j>C-1:
        return
    grid[i][j].toggle()

def toggle_neighbors(i, j):
    toggle_grid(i-1, j)
    toggle_grid(i+1, j)
    toggle_grid(i, j-1)
    toggle_grid(i, j+1)

def check_for_win():
    for i in range(R):
        for j in range(C):
            if grid[i][j].color==Color.RED:
                return
    print("win")
    w.close()
            

for _ in range(5):
    i=randint(0, R-1)
    j=randint(0, C-1)
    toggle_neighbors(i, j)
    


w.run()

