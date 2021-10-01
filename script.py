#import pyautogui
import time
import os
from threading import Thread
from enum import Enum

class State(Enum):
    UNKNOWN = 0
    WAITING_TO_PLAY = 1
    PLAYED = 2

class Column(Enum):
    NONE = 0
    TOP = 1
    MID = 2
    BOTTOM = 3

class Manager(Thread):
    strategy

    def get_field(self, field_name, fields):
      matching = [s for s in fields if field_name in s]
      return matching[0].replace(" ", "").split(":")
  
    def play(self, state, lastDraw, dealerMessage):
        if state = PLAYED and dealerMessage = "La pallina sta girando":
            return WAITING_TO_PLAY
        
        if state = WAITING_TO_PLAY and dealerMessage = "Fate le vostre puntate":
            if self.strategy.execute(lastDraw):
                return PLAYED
            else
                return WAITING_TO_PLAY

    def run(self):
        state = WAITING_TO_PLAY

        while True:
            if not os.path.exists("/home/citi/Downloads/foo.txt"):
                continue

            lines = []
            with open('/home/citi/Downloads/foo.txt') as f:
                lines = f.readlines()
        
            if not lines:
                continue

            print(lines)
        
            if not self.strategy:
                topCol = get_field("TopColumn").split(',')
                midCol = get_field("MidColumn").split(',')
                botCol = get_field("BotColumn").split(',')
                self.strategy = Strategy(topCol, midCol, botCol)

            state = play(state, get_field("LastDraw"), get_field("Message"))
        
            os.remove("/home/citi/Downloads/foo.txt")

            time.sleep(1)

class Strategy():
    topCol, midCol, botCol = []

    def __init__(self, topCol, midCol, botCol):
        self.topCol = topCol
        self.midCol = midCol
        self.botCol = botCol      

    def execute(self, drawNumber):
            #pyautogui.click(1742, 1087, duration = 1) # x+=140 y+=120

if __name__ == "__main__":
    Manager().start()
