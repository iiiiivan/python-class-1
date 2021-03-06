from platform import platform
from pycat.core import Window, Sprite
from pycat.base.event import MouseEvent
from enum import Enum, auto
from typing import List
w=Window(background_image='mountains_01.png', draw_sprite_rects=False)
SPEED_SCALE=0.05

class AlienState(Enum):
    WAIT_FOR_CLICK=auto()
    JUMPING=auto()
    DIE=auto()
    RESET=auto()

class Alien(Sprite):
    SCALE=0.3
    def on_create(self):
        self.image='alien.png'
        self.scale=Alien.SCALE
        self.x_speed=0
        self.y_speed=10
        self.state=AlienState.WAIT_FOR_CLICK

    def should_stop_on_platform(self):
        p_list=self.get_touching_sprites_with_tag('hitbox')
        if p_list:
            p=p_list[0]
            prev_y=self.y-self.y_speed
            min_y=p.y+p.height/2+a.height/2
            if prev_y>min_y:
                self.y=min_y
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
            if self.is_touching_window_edge():
                self.state=AlienState.DIE
            if self.should_stop_on_platform():
                self.state=AlienState.WAIT_FOR_CLICK
        elif self.state is AlienState.WAIT_FOR_CLICK:
            pass
        elif self.state is AlienState.DIE:
            self.scale-=0.04
            if self.scale<0:
                a.x=p.x
                a.y=first_y
                self.state=AlienState.RESET
        elif self.state is AlienState.RESET:
            self.scale+=0.04
            if self.scale>Alien.SCALE:
                self.state=AlienState.WAIT_FOR_CLICK


    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state is AlienState.WAIT_FOR_CLICK:
            dp=mouse_event.position-self.position
            self.x_speed=SPEED_SCALE*dp.x
            self.y_speed=SPEED_SCALE*dp.y
            self.state=AlienState.JUMPING

class Platform(Sprite):
    def on_create(self):
        self.image='platform.png'
        self.scale=0.3
        self.add_tag('platform')
    def make_hitbox(self):
        self.hitbox=w.create_sprite(x=self.x, y=self.y)
        self.hitbox.width=0.8*self.width
        self.hitbox.height=0.8*self.height
        self.hitbox.layer=1
        self.hitbox.add_tag('hitbox')
        self.hitbox.opacity=0

fp=w.create_sprite(Platform, y=100, x=100)
w.create_sprite(Platform, y=100, x=300)
w.create_sprite(Platform, y=100, x=500)
platforms:List[Platform] = w.get_sprites_with_tag('platform')
for p in platforms:
    p.make_hitbox()

a=w.create_sprite(Alien)
a.x=fp.x
first_y=a.y=fp.hitbox.y+fp.hitbox.height/2+a.height/2


w.run()