from random import randint, choice
from enum import Enum, auto
from pycat.core import Window, Sprite, Scheduler, Label

w=Window()

def get_text_list(file_path: str):
    result = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            result.append(line.strip())
    return result

games = get_text_list('L10/games.txt')
languages = get_text_list('L10/languages.txt')
sports = get_text_list('L10/sports.txt')


class HighScore(Label):
    def on_create(self):
        with open('L10/high_score.txt', 'r') as file:
            self.high_score = int(file.readline())
        self.text = 'High Score: ' + str(self.high_score)
        self.x = w.center.x
        
high_score_label = w.create_label(HighScore)

class WordGroup(Enum):
    GAMES=auto()
    SPORTS=auto()
    LANGUAGES=auto()


class Word(Sprite):
    group=WordGroup.GAMES
    def on_create(self):
        self.scale=100
        self.y=w.height
        self.x=randint(0, w.width)
        self.label=w.create_label()
        self.text=choice(games+sports+languages)
        self.label.color=(255, 0, 0)
        self.update_lable_position()

    @property
    def text(self):
        return self.label.text

    @text.setter
    def text(self, s:str):
        self.label.text=s
        self.width=self.label.content_width
        self.height=self.label.content_height

    def update_lable_position(self):
        self.label.position = self.position
        self.label.x -=self.label.content_width/2
        self.label.y +=self.label.content_height/2

    def delete(self):
        super().delete()
        self.label.delete()

    def on_update(self, dt):
        self.y-=3
        self.update_lable_position()
        if self.y<4:
            self.delete()

    def on_left_click(self):
        if Word.group is WordGroup.GAMES and self.text in games:
            score_label.score += 1
            self.delete() 
        elif Word.group is WordGroup.SPORTS and self.text in sports:
            score_label.score += 1
            self.delete()
        elif Word.group is WordGroup.LANGUAGES and self.text in languages:
            score_label.score += 1
            self.delete()



def switch_group():
    Word.group=choice([Word.group.GAMES, Word.group.SPORTS, Word.group.LANGUAGES,])
    group_label.text=str(Word.group)


class Score(Label):
    def on_create(self):
        self.score=0
        self.y=50

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score=value
        self.text='score: ' + str(self.score)
        if value > high_score_label.high_score:
            
            high_score_label.high_score = value
            with open('L10/high_score.txt', 'w') as file:
                file.write(str(high_score_label.high_score))
            high_score_label.text = 'High Score: ' + str(high_score_label.high_score)


group_label=w.create_label(text=str(Word.group))    
score_label=w.create_label(Score)
Scheduler.update(lambda:w.create_sprite(Word), 0.5)
Scheduler.update(switch_group, 10)

w.run()