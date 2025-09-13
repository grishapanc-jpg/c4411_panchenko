import random
from tkinter.font import names


class Student:
    def __init__(self):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress +=0.12
        self.gladness -=3

    def to_sleep(self):
        print('Time to sleep')
        self.gladness +=3


    def to_chill(self):
        print('Rest time!')
        self.gladness += 5
        self.progress -= 0.1

    def to_chill(self):

        print('Cast out...')
        self.gladness += 5
        self.progress -= 0.1




