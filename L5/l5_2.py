from random import randint
from pycat.core import Window, Sprite

w=Window(is_sharp_pixel_scaling=True, width=1480)

CELL_SIZE=50
X0=100
Y0=w.height-100

LEVEL_DICTIONARY={'g':'tiles/tile_026.png',
                  'w':'tiles/tile_012.png',
                  's':'tiles/tile_014.png',
                  'h':'tiles/tile_209.png'}

LEVEL=[
    'gggggggggg',
    'gggggggggg',
    'gggggsgggg',
    'gggggggggg',
    'gggwwsgggg',
    'gggggwgggg',
    'gggggggwgg',
    'ggggggwggg',
    'gggggwwggg',
    'gggwwwgggg',
]
wizard=(3,4,'h')




class Cell(Sprite):

    def on_left_click(self):
        print(self.image)
        

    def setup(self, i: int, j: int, c: str):
        self.x=X0+j*CELL_SIZE
        self.y=Y0-i*CELL_SIZE
        self.image=LEVEL_DICTIONARY[c]
        self.scale_to_width(CELL_SIZE-1)

for i in range(len(LEVEL)):
    for j in range(len(LEVEL[i])):
        c=w.create_sprite(Cell)
        c.setup(i, j, LEVEL[i][j])

s=w.create_sprite(Cell)
s.setup(*wizard)

w.run()