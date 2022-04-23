from pycat.core import Window, Color, Sprite, KeyCode
from random import choice
from pycat.base.event import KeyEvent

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
PEGS=6
GUESSES=20
SCALE=30

w=Window(draw_sprite_rects=True, width=SCALE*2*PEGS)
current_color=Color.RED

class RandomCode:

    def __init__(self):
        self.colors=[choice(COLORS) for _ in range(PEGS)]
        self.sprites=[w.create_sprite(scale=SCALE, color=c) for c in self.colors]
        for i in range(PEGS):
            s=self.sprites[i]
            s.x=s.width/2+i*(s.width+1)
            s.y=w.height-s.height/2
            s. is_visible=False

        
class ColorChooser:

    class Choice(Sprite):
        def on_left_click(self):
            global current_color
            current_color=self.color

    def __init__(self):
        self.sprites=[w.create_sprite(ColorChooser.Choice, scale=SCALE, color=c) for c in COLORS]
        for i in range(len(COLORS)):
            s=self.sprites[i]
            s.x=s.width/2+i*(s.width+1)
            s.y=s.height/2


class Guess:

    class GuessSprite(Sprite):

        def on_left_click(self):
            if self in current_guess.sprites:
                self.color=current_color

    guess_number=0

    def __init__(self, y: int):
        Guess.guess_number+=1
        self.y=y
        self.sprites=[w.create_sprite(Guess.GuessSprite, scale=SCALE, color=Color.BLACK) for _ in range(PEGS)]
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
        w.subscribe(on_key_press=self.on_key_press)

    def on_key_press(self, key_event: KeyEvent):
        if key_event.symbol == KeyCode.C:
            result=Result()
            if result.red_pegs==PEGS:
                print("You win")
            elif Guess.guess_number<GUESSES:
                global current_guess
                current_guess=Guess(current_guess.y+SCALE)
            else:
                print("You lose")


class Result:
    def __init__(self):
        self.red_pegs=0
        unmatched_guess_colors=[]
        unmatched_code_colors=[]
        for i in range(PEGS):
            if current_guess.colors[i]==code.colors[i]:
                self.red_pegs+=1
            else:
                unmatched_guess_colors.append(current_guess.colors[i])
                unmatched_code_colors.append(code.colors[i])
        for i in range(self.red_pegs):
            w.create_circle(x=(PEGS+1)*SCALE+i*SCALE/2, y=current_guess.y, radius=SCALE/8, color=Color.RED)



        white_pegs=0
        for color in unmatched_guess_colors:
            if color in unmatched_code_colors:
                white_pegs+=1
                unmatched_code_colors.remove(color)

        for i in range(white_pegs):
            w.create_circle(x=(PEGS+1)*SCALE+(i+self.red_pegs)*SCALE/2, y=current_guess.y, radius=SCALE/8, color=Color.WHITE)



code=RandomCode()
chooser=ColorChooser()
current_guess=Guess(100)
w.create_sprite(CheckButton)
print(code.colors)
w.run()