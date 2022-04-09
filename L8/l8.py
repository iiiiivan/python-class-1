from pycat.core import Window
from pycat_turtle import Turtle, Grid
from typing import List

w = Window()
t=w.create_sprite(Turtle)


    
grid=Grid(0, 0, w.width/4, w.height/2, 20, 20)
grid.draw(t)
grid.x+=w.width/4
grid.height*=2
grid.make_cells()
grid.draw(t)
w.run()