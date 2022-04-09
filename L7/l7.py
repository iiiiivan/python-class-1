from pycat.core import Window, Point
from random import randint

w=Window()

def create_triangle(p1:Point, p2:Point, p3:Point):
    w.create_line(p1.x, p1.y, p2.x, p2.y)
    w.create_line(p2.x, p2.y, p3.x, p3.y)
    w.create_line(p3.x, p3.y, p1.x, p1.y)

def get_random_point(x1=0, x2=w.width, y1=0, y2=w.height):
    return Point(randint(x1, x2), randint(y1, y2))

def create_barycenter(p1:Point, p2:Point, p3:Point):
    bc=(p1+p2+p3)/3
    w.create_circle(bc.x, bc.y, 5)

def create_random_triangle(is_create_barycenter=False):
    p1=get_random_point()
    p2=get_random_point()
    p3=get_random_point()
    create_triangle(p1, p2, p3)
    if is_create_barycenter:
        create_barycenter(p1, p2, p3)

for _ in range(5):
    create_random_triangle(True)

w.run()