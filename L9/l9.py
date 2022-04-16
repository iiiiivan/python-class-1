from turtle import color
from pycat.core import Window, Color, Sprite
from random import choice

w=Window(draw_sprite_rects=True)
current_color=Color.RED

COLORS=[
    Color.RED,
    Color.GREEN,
    Color.BLUE,
    Color.YELLOW,
    Color.CYAN,
    Color.ORANGE,
    Color.BLACK,
    Color.WHITE
]
PEGS=4
GUESSES=10

class RandomCode:

    def __init__(self):
        self.colors=[choice(COLORS) for _ in range(PEGS)]
        self.sprites=[w.create_sprite(scale=50, color=c) for c in self.colors]
        for i in range(PEGS):
            s=self.sprites[i]
            s.x=s.width/2+i*(s.width+1)
            s.y=w.height-s.height/2

        
class ColorChooser:

    class Choice(Sprite):
        def on_left_click(self):
            global current_color
            current_color=self.color

    def __init__(self):
        self.sprites=[w.create_sprite(ColorChooser.Choice, scale=25, color=c) for c in COLORS]
        for i in range(len(COLORS)):
            s=self.sprites[i]
            s.x=s.width/2+i*(s.width+1)
            s.y=s.height/2


class Guess:

    class GuessSprite(Sprite):

        def on_left_click(self):
            if self in current_guess.sprites:
                self.color=current_color

    def __init__(self, y: int):
        self.y=y
        self.sprites=[w.create_sprite(Guess.GuessSprite, scale=50, color=Color.BLACK) for _ in range(PEGS)]
        for i in range(PEGS):
            s=self.sprites[i]
            s.x=s.width/2+i*(s.width+1)
            s.y=y

    @property
    def colors(self):
        return[sprite.color for sprite in self.sprites]
        
        
class CheckButton(Sprite):
    def on_create(self):
        self.x=100
        self.y=50
        self.width=100
        self.height=20
        lable=w.create_label(text="check", color=Color.BLACK, font_size=10)
        lable.x=self.x-lable.content_width/2
        lable.y=self.y+lable.content_height/2

    def on_left_click(self):
        global current_guess
        red_pegs=0
        for i in range(PEGS):
            if current_guess.colors[i]==code.colors[i]:
                red_pegs+=1
        print(red_pegs)
        current_guess=Guess(current_guess.y+50)

     


code=RandomCode()
chooser=ColorChooser()
current_guess=Guess(100)
w.create_sprite(CheckButton)
print(code.colors)
w.run()