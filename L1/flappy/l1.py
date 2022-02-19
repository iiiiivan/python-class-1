from pycat.core import Window, Sprite, Scheduler, KeyCode
from random import randint

w = Window(background_image='background.png',
            width=900,
            height=504,
            enforce_window_limits=False)

PIPE_GAP=0.4*w.height


class Pipe(Sprite):
    def on_create(self):
        self.image='pipe.png'
        self.scale*=0.65
        self.x=w.width+self.width/2

    def on_update(self, dt):
        self.x-=5
        if self.x<-self.width/2:
            self.delete()

def create_pipe(dt):
    PAD=30
    gap_y=randint(PIPE_GAP//2+PAD, w.height-PIPE_GAP//2-PAD)
    p1=w.create_sprite(Pipe)
    p1.y=gap_y - PIPE_GAP/2 - p1.height/2

    p2=w.create_sprite(Pipe)
    p2.y=gap_y + PIPE_GAP/2 + p2.height/2
    p2.rotation=180

GRAVITY=-0.2

class Bird(Sprite):
    def on_create(self):
        self.image='bird.gif'
        self.x=50
        self.y=w.height/2
        self.scale=0.2
        self.y_speed=0

    def on_update(self, dt):
        self.y+=self.y_speed
        self.y_speed+=GRAVITY

        if w.is_key_down(KeyCode.SPACE):
            self.y_speed=2
  
Scheduler.update(create_pipe, 1.5)
create_pipe(0)
w.create_sprite(Bird)

w.run()