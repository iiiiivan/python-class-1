from pycat.core import Window, Sprite, Scheduler
from pycat.base.event import MouseEvent
from enum import Enum, auto
from typing import List
w=Window(enforce_window_limits=False, background_image='mountains_01.png', draw_sprite_rects=False)
SPEED_SCALE=0.05

class AlienState(Enum):
    WAIT_FOR_CLICK=auto()
    JUMPING=auto()
    DIE=auto()
    RESET=auto()
    MOVE=auto()
    FALL=auto()

class Alien(Sprite):
    SCALE=0.3
    def on_create(self):
        self.image='alien.png'
        self.scale=Alien.SCALE
        self.x_speed=0
        self.y_speed=10
        self.state=AlienState.WAIT_FOR_CLICK

    def should_stop_on_platform(self, tag):
        p_list=self.get_touching_sprites_with_tag(tag)
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
            if self.should_stop_on_platform('hitbox'):
                self.state=AlienState.WAIT_FOR_CLICK
            if self.should_stop_on_platform('moving'):
                self.state=AlienState.MOVE
        elif self.state is AlienState.WAIT_FOR_CLICK:
            pass
        elif self.state is AlienState.MOVE:
            if not self.is_touching_any_sprite_with_tag('movingplatform'):
                self.state=AlienState.JUMPING
                self.x_speed=0
                self.y_speed=0
        elif self.state is AlienState.DIE:
            self.scale-=0.04
            if self.scale<0:
                a.x=fp.x
                a.y=first_y
                self.state=AlienState.RESET
        elif self.state is AlienState.RESET:
            self.scale+=0.04
            if self.scale>Alien.SCALE:
                self.state=AlienState.WAIT_FOR_CLICK


    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state is AlienState.WAIT_FOR_CLICK or self.state is AlienState.MOVE:
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
        self.hitbox.opacity=200

class MovingPlatform(Platform):
    def on_create(self):
        self.add_tag('movingplatform')
        return super().on_create()
    def make_hitbox(self):
        super().make_hitbox()
        self.hitbox.remove_tag('hitbox')
        self.hitbox.add_tag('moving')
    def on_update(self, dt):
        self.x-=5
        self.hitbox.x=self.x
        if self.x<-self.width/2:
            self.delete()
            self.hitbox.delete()

fp=w.create_sprite(Platform, y=100, x=100)
w.create_sprite(Platform, y=100, x=300)
w.create_sprite(Platform, y=100, x=500)
w.create_sprite(MovingPlatform, y=200, x=1000)
platforms:List[Platform] = w.get_sprites_with_tag('platform')
for p in platforms:
    p.make_hitbox()

a=w.create_sprite(Alien)
a.x=fp.x
first_y=a.y=fp.hitbox.y+fp.hitbox.height/2+a.height/2

def create_platform():
    p=w.create_sprite(MovingPlatform, y=200, x=1300)
    p.make_hitbox()

Scheduler.update(create_platform, 1)

w.run()