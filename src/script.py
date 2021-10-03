import log
import pyautogui
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
    _strategy = None
    _logger = None

    def __init__(self):
        self._logger = log.MyLogger.__call__().get_logger()

    def get_field(self, field_name, fields):
        matching = [s for s in fields if field_name in s]
        return matching[0].replace(" ", "").split(":")

    def play(self, state, lastDraw, dealerMessage):
        if (
            state == State.PLAYED
            and dealerMessage == "Attendi finché non inizia il prossimo giro"
        ):
            return State.WAITING_TO_PLAY

        if (
            state == State.WAITING_TO_PLAY
            and dealerMessage == "Effettua Le Tue Puntate"
        ):
            if self._strategy.execute(lastDraw):
                return State.PLAYED
            else:
                return State.WAITING_TO_PLAY

    def run(self):
        state = State.WAITING_TO_PLAY

        while True:
            try:
                if not os.path.exists("/home/citi/Downloads/foo.txt"):
                    continue

                lines = []
                with open("/home/citi/Downloads/foo.txt") as f:
                    lines = f.readlines()

                if not lines:
                    continue

                print(lines)

                if not self._strategy:
                    topCol = self.get_field("TopColumn").split(",")
                    midCol = self.get_field("MidColumn").split(",")
                    botCol = self.get_field("BotColumn").split(",")
                    self._strategy = Strategy(topCol, midCol, botCol)

                state = self.play(
                    state, self.get_field("LastDraw"), self.get_field("Message")
                )

                os.remove("/home/citi/Downloads/foo.txt")

                time.sleep(1)
            except:
                self._logger.exception("message")


class Strategy:
    _topCol, _midCol, _botCol = []
    _xOffsets, _yOffsets = 0
    _dicColumnsNumbers = {}
    _logger = None

    def __init__(self, topCol, midCol, botCol):
        try:
            self._logger = log.MyLogger.__call__().get_logger()

            self._topCol = topCol
            self._midCol = midCol
            self._botCol = botCol
            self._xOffsets = 140
            self._yOffsets = 120

            self.init_dic()
        except:
            self._logger.exception("message")

    def init_dic(self):
        self.dicColumnsNumbers.fromkeys(range(36))
        for i in range(36):
            if i == 0:
                self.dicColumnsNumbers[i] = Column.NONE
            if i % 3 == 0:
                self.dicColumnsNumbers[i] = Column.TOP
            if i % 3 == 2:
                self.dicColumnsNumbers[i] = Column.MID
            if i % 3 == 1:
                self.dicColumnsNumbers[i] = Column.BOTTOM

    def execute(self, drawNumber):
        try:
            if self.dicColumnsNumbers[drawNumber] == Column.NONE:
                return True

            if self.dicColumnsNumbers[drawNumber] == Column.TOP:
                self.click_column(self.midCol, self.botCol)

            if self.dicColumnsNumbers[drawNumber] == Column.BOTTOM:
                self.click_column(self.midCol, self.topCol)
            if self.dicColumnsNumbers[drawNumber] == Column.MID:
                self.click_column(self.topCol, self.botCol)
        except:
            self._logger.exception("message")
            return False

    def click_column(self, col1, col2):
        pyautogui.click(col1[0] + self.xOffsets, col1[1] + self.yOffsets)
        pyautogui.click(col2[0] + self.xOffsets, col2[1] + self.yOffsets)

if __name__ == "__main__":
    Manager().start()
