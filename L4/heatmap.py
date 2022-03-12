from random import randint
from pycat.core import Window, Sprite

w=Window()

ROWS=20
COLS=50
CELL_SIZE=20
X0=100
Y0=w.height-100

heatmap=[]

for i in range(ROWS):
    row=[]
    for j in range(COLS):
        row.append(randint(0, 255))
    heatmap.append(row)

class Cell(Sprite):
    def on_create(self):
        self.scale=CELL_SIZE-1
        self.label=w.create_label()
        self.label.font_size=6
        self.label.color=(0,0,0)



    def setup(self, i: int, j: int):
        val=heatmap[i][j]
        self.color=(255, 255-val, 255-val)
        self.x=X0+j*CELL_SIZE
        self.y=Y0-i*CELL_SIZE
        self.label.text=str(val)
        self.label.x=self.x-self.label.content_width/2
        self.label.y=self.y+self.label.content_height/2

for i in range(ROWS):
    for j in range(COLS):
        c=w.create_sprite(Cell)
        c.setup(i, j)

w.run()