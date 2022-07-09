from typing import List
from pycat.core import Window, Sprite, Scheduler, KeyCode, Label, Color
from random import randint
from enum import Enum, auto

w = Window(width=900, height=504, enforce_window_limits=False) 

PIPE_GAP=0.4*w.height
GRAVITY=-0.2
PIPE_SPEED=5
FLAP_SPEED=4



class Background(Sprite):
    def on_create(self):
        self.image='background.png'
        self.y=w.height/2
        self.x=w.width/2
        self.x_speed=1
        self.layer = -1
    
    def on_update(self, dt):
        self.x-=1
        if self.x <= -w.width/2:
            self.x+=w.width*2

class Enemy(Sprite):

    class State(Enum):
        MOVE_UP = auto()
        MOVE_DOWN = auto()
    
    def on_create(self):
        self.image='bee.png'
        self.x=w.width/2
        self.y=w.height/2
        self.scale=0.3
        self.speed=3
        self.state=Enemy.State.MOVE_UP
        self.layer = 1
        self.time = 0

    def on_update(self, dt):
        if self.state is Enemy.State.MOVE_UP:
            self.y += self.speed
            if self.is_touching_window_edge():
                self.state = Enemy.State.MOVE_DOWN
        else:
            self.y -= self.speed
            if self.is_touching_window_edge():
                self.state = Enemy.State.MOVE_UP
        
        self.time += dt
        if self.time > 1:
            self.time = 0
            w.create_sprite(EnemyBullet)
                
                
class EnemyBullet(Sprite):

    def on_create(self):
        self.scale = 20
        self.position = enemy.position
        self.color=(255 ,0 ,0)

    def on_update(self, dt):
        self.x-=5
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player_life.life -= 1
            if player_life.life <=0:
                w.close()


class LabelBackground(Sprite):
    def on_create(self):
        self.width = 250
        self.height = 150
        self.color = Color.BLACK
        self.x = self.width/2
        self.y = w.height - self.height/2
        self.layer = 0


w.create_sprite(LabelBackground)


class Time(Label):
    def on_create(self):
        self.time = 0
        self.font_size = 15
        self.y = 40

    def on_update(self, dt):
        self.time += dt
        self.text = 'Time: ' + str(round(self.time, 1))


class HighScore(Label):
    def on_create(self):
        # read from file the last high score
        self.score = 0
        with open("finalpproject/highscore.txt", "r") as f:
            self.score = float(f.readline())

        self.text = 'High Score: ' + str(self.score)
        self.y = 100

    def on_update(self, dt):
        pass
        # check if the current time is more then the last high score
        # if time > self.score:
        #    write time to file
w.create_label(HighScore)
w.create_label(Time )
enemy = w.create_sprite(Enemy)
w.create_sprite(Background, x=0)
w.create_sprite(Background, x=w.width)

class Pipe(Sprite):
    def on_create(self):
        self.image='pipe.png'
        self.scale*=0.65
        self.x=w.width+self.width/2
        self.add_tag('pipe')


    def on_update(self, dt):
        self.x-=PIPE_SPEED
        if self.x<-self.width/2:
            self.delete()




class PlayerLife(Label):
    def on_create(self):
        self.font_size=15
        self.life=3

    def on_update(self, dt: float):
        self.text="PlayerLives: "+str(self.life)

player_life=w.create_label(PlayerLife)
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
            self.y_speed=4 

        if self.is_touching_any_sprite_with_tag('pipe'):
            # w.close()
            pass
        
        if self.y<0:
            # w.close()
            pass

class Bomb(Sprite):
    def on_create(self):
        self.image='bomb.png'
        self.scale=0.1
        self.pipes:List[Pipe]=[]

    def on_update(self, dt):
        self.x-=PIPE_SPEED

    def on_left_click(self):
        self.image='boom.png'
        for p in self.pipes:
            p.delete()
        
        if self.x<-self.width/2:
            self.delete()


pipe_time = 3
def create_pipe(dt):
    global pipe_time

    PAD=30
    gap_y=randint(PIPE_GAP//2+PAD, w.height-PIPE_GAP//2-PAD)
    p1=w.create_sprite(Pipe)
    p1.y=gap_y - PIPE_GAP/2 - p1.height/2

    p2=w.create_sprite(Pipe)
    p2.y=gap_y + PIPE_GAP/2 + p2.height/2
    p2.rotation=180

    if randint(1, 4)==1:
        b=w.create_sprite(Bomb)
        b.x=p1.x
        b.y=gap_y
        b.pipes=[p1, p2]

    Scheduler.wait(pipe_time, create_pipe)

    if pipe_time >= 1:
        pipe_time -= 0.1
    else:
        pipe_time = 1


create_pipe(0)
player=w.create_sprite(Bird)

w.run() 