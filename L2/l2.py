from pycat.core import Window, Sprite
from pycat.base.event import MouseEvent
from enum import Enum, auto
w=Window(background_image='mountains_01.png')
SPEED_SCALE=0.05

class AlienState(Enum):
    WAIT_FOR_CLICK=auto()
    JUMPING=auto()

class Alien(Sprite):
    def on_create(self):
        self.image='alien.png'
        self.scale=0.3
        self.x_speed=0
        self.y_speed=10
        self.state=AlienState.WAIT_FOR_CLICK

    def should_stop_on_platform(self):
        p_list=self.get_touching_sprites_with_tag('platform')
        if p_list:
            p=p_list[0]
            prev_y=self.y-self.y_speed
            min_y=p.y+p.height/2+a.height/2
            if prev_y>min_y:
                return True
            else:
                return False
        else:
            return False

    def on_update(self, dt):
        if self.state is AlienState.JUMPING:
            self.x+=self.x_speed
            self.y+=self.y_speed
            self.y_speed-=0.5
            if self.should_stop_on_platform():
                self.state=AlienState.WAIT_FOR_CLICK
        elif self.state==AlienState.WAIT_FOR_CLICK:
            pass

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state is not AlienState.JUMPING:
            dp=mouse_event.position-self.position
            self.x_speed=SPEED_SCALE*dp.x
            self.y_speed=SPEED_SCALE*dp.y
            self.state=AlienState.JUMPING

class Platform(Sprite):
    def on_create(self):
        self.image='platform.png'
        self.scale=0.3
        self.add_tag('platform')

p=w.create_sprite(Platform, y=100, x=100)
w.create_sprite(Platform, y=100, x=300)
w.create_sprite(Platform, y=100, x=500)

a=w.create_sprite(Alien)
a.x=p.x
a.y=p.y+p.height/2+a.height/2


w.run()