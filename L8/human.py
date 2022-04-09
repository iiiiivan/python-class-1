class Human:
    def __init__(self, age, name):
        self.age=age
        self.name=name

    def __str__(self):
        return "I'm"+self.name

    def talk(self):
        print("I'm", self.name)


h=Human(100, 'Ivan')
otherhuman=Human(99, 'Ian')

h.talk()
otherhuman.talk()