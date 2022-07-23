from turtle import position
from typing import List
from matplotlib.pyplot import text
from pycat.core import Window, Sprite, Scheduler, KeyCode, Label, Color
from random import randint
from enum import Enum, auto

from tables import Col

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
        self.x=0.8*w.width
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
        
        if self.is_touching_any_sprite_with_tag("weapon"):
            global enemy
            self.delete()
            enemy=None
                
                
class EnemyBullet(Sprite):

    def on_create(self):
        self.scale = 20
        self.position = enemy.position
        self.color=(255 ,0 ,0)

    def on_update(self, dt):
        self.x-=7
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player_life.life -= 1
            if player_life.life <=0:
                w.close()


class PlayerLife(Label):
    def on_create(self):
        self.font_size=20
        self.life=3
        self.layer=2
        self.font = "Blackadder ITC"
        self.color=Color(51, 204, 51)

    def on_update(self, dt: float):
        self.text="PlayerLives: "+str(self.life)


class Time(Label):
    def on_create(self):
        self.time = 0
        self.font_size = 20
        self.y = 40
        self.layer=2
        self.font = "Blackadder ITC"

    def on_update(self, dt):
        self.time += dt
        self.text = 'Time: ' + str(round(self.time, 1))

class HighScoreStart(Label):
    def on_create(self):
        self.font_size = 30
        self.font = "Blackadder ITC"
        # read from file the last high score
        self.score = 0
        with open("finalpproject/highscore.txt", "r") as f:
            self.score = float(f.readline())

        self.text = 'High Score: ' + str(self.score)
        self.y = w.height/2
        self.x=w.center.x-self.content_width/2
        self.layer=2
        self.color=Color.RED

class HighScore(Label):
    def on_create(self):
        self.font_size = 20
        self.font = "Blackadder ITC"
        self.score = 0
        with open("finalpproject/highscore.txt", "r") as f:
            self.score = float(f.readline())
        self.text = 'High Score: ' + str(self.score)
        self.y = 100
        self.layer=2
        self.color=Color.RED

    def on_update(self, dt):
        pass
        # check if the current time is more then the last high score
        if gui.time.time > self.score:
            with open("finalpproject/highscore.txt", "w") as f:
                f.write(str(round(gui.time.time,1)))


class LabelBackground(Sprite):
    def on_create(self):
        
        self.height = 150
        self.color = Color.BLACK
        
        self.y = w.height - self.height/2
        self.layer = 1
        self.opacity=125
        self.high=w.create_label(HighScore, y=450)
        self.time=w.create_label(Time, y=400)
        self.width = self.high.content_width 
        self.x = self.width/2


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


class Bird(Sprite):
    def on_create(self):
        self.image='bird.gif'
        self.x=50
        self.y=w.height/2
        self.scale=0.2
        self.y_speed=0
        self.has_weapon = False
    
    def on_left_click_anywhere(self):
        if self.has_weapon:
            self.has_weapon=False
            w.create_sprite(Weapon)

    def on_update(self, dt):
        self.y+=self.y_speed
        self.y_speed+=GRAVITY

        if w.is_key_down(KeyCode.SPACE):
            self.y_speed=4 

        if self.is_touching_any_sprite_with_tag('pipe') or self.y<0:
            endgame()
               


class WeaponIcon(Sprite):
    def on_create(self):
        self.image='bomb.png'
        self.scale=0.1

    def on_update(self, dt):
        self.x-=PIPE_SPEED
        if self.x<-self.width/2:
            self.delete()

    def on_left_click(self):
        global enemy
        self.delete()
        player.has_weapon=True
        if enemy is None :
            enemy = w.create_sprite(Enemy)


class Weapon(Sprite):
    def on_create(self):
        self.position=player.position
        self.image='bomb.png'
        self.scale=0.1
        self.x_speed=8
        self.y_speed=8
        self.layer=10
        self.hb=w.create_sprite(HitBox, position=self.position)
        

    def on_update(self, dt):
        self.x+=self.x_speed
        self.y+=self.y_speed
        self.y_speed-=0.2
        self.hb.position=self.position
        if self.x>w.width or self.y<0:
            self.delete()
            self.hb.delete()


class HitBox(Sprite):
    
    def on_create(self):
        self.opacity=255
        self.scale=2
        self.add_tag("weapon")
        

class GameOver(Label):
    def on_create(self):
        self.color=Color.WHITE
        self.font_size=100
        self.text="GAME OVER"
        self.x=w.width/2-self.content_width/2
        self.y=w.height/2+self.content_height/2
    def on_update(self, dt: float):
        pass



pipe_time = 3
is_play=True
def create_pipe(dt):
    global pipe_time, is_play

    if is_play:
        PAD=30
        gap_y=randint(PIPE_GAP//2+PAD, w.height-PIPE_GAP//2-PAD)
        p1=w.create_sprite(Pipe)
        p1.y=gap_y - PIPE_GAP/2 - p1.height/2

        p2=w.create_sprite(Pipe)
        p2.y=gap_y + PIPE_GAP/2 + p2.height/2
        p2.rotation=180

        if player and  not player.has_weapon and randint(1, 100)<=100:

            #add a weapon for bird
            b=w.create_sprite(WeaponIcon)
            b.x=p1.x
            b.y=gap_y

        

        Scheduler.wait(pipe_time, create_pipe)

    if pipe_time >= 1:
        pipe_time -= 0.1
    else:
        pipe_time = 1

gui=None
enemy=None
player_life=None
player=None

def start_game():
    global gui, player_life, player
    gui=w.create_sprite(LabelBackground)
    player_life=w.create_label(PlayerLife)
    player=w.create_sprite(Bird)
    
def endgame():
    w.delete_all_sprites()
    w.delete_all_labels()
    w.create_label(GameOver)
    global is_play
    is_play=False

class StartButton(Sprite):
    def on_create(self):
        self.image="Button3-b.png"
        self.scale=1
        self.x=450
        self.y=50
        self.layer=5
        self.score = w.create_label(HighScoreStart)

    def  on_update(self, dt):
        pass
    def on_left_click(self):
        self.delete()
        self.score.delete()
        start_game()



w.create_sprite(Background, x=0)
w.create_sprite(Background, x=w.width)
w.create_sprite(StartButton)

create_pipe(0)
w.run() 