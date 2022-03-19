from random import randint
from pycat.core import Window, Sprite

w=Window(is_sharp_pixel_scaling=True, width=1480)

ROWS=10
COLS=27
CELL_SIZE=50
X0=100
Y0=w.height-100

heatmap=[]
val=0
for i in range(ROWS):
    row=[]
    for j in range(COLS):
        row.append(val)
        val+=1
    heatmap.append(row)

class Cell(Sprite):
    def on_create(self):
        # self.scale=CELL_SIZE-1
        # self.label=w.create_label()
        # self.label.font_size=6
        # self.label.color=(0,0,0)
        pass

    def on_left_click(self):
        print(self.image)
        

    def setup(self, i: int, j: int):
        val=heatmap[i][j]
        self.x=X0+j*CELL_SIZE
        self.y=Y0-i*CELL_SIZE
        # self.label.text=str(val)
        # self.label.x=self.x-self.label.content_width/2
        # self.label.y=self.y+self.label.content_height/2
        file_name='tiles/tile_'
        num=''
        if val<10:
            num='00'+str(val)+'.png'
        elif val<100:
            num='0'+str(val)+'.png'
        else:
            num=str(val)+'.png'

        file_name+=num
        self.image=file_name
        self.scale_to_width(CELL_SIZE-1)

for i in range(ROWS):
    for j in range(COLS):
        c=w.create_sprite(Cell)
        c.setup(i, j)

w.run()