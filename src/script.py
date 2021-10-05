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
        super(Manager, self).__init__()
        self._logger = log.MyLogger.__call__().get_logger()

    def get_field(self, field_name, fields):
        matching = [s for s in fields if field_name in s]
        return matching[0].split(":")[1].strip().replace("\n","")

    def play(self, state, lastDraw, dealerMessage):
        if (
            state == State.PLAYED
            and dealerMessage == "Attendi finché non inizia il prossimo giro"
        ):
            os.remove("/home/citi/Downloads/Info.txt")
            return State.WAITING_TO_PLAY

        if (
            state == State.WAITING_TO_PLAY
            and dealerMessage == "Effettua Le Tue Puntate"
        ):
            if self._strategy.execute(lastDraw):
                os.remove("/home/citi/Downloads/Info.txt")
                return State.PLAYED
            else:
                return State.WAITING_TO_PLAY

    def run(self):
        state = State.WAITING_TO_PLAY

        while True:
            try:
                if not os.path.exists("/home/citi/Downloads/Info.txt"):
                    continue

                lines = []
                with open("/home/citi/Downloads/Info.txt") as f:
                    lines = f.readlines()

                if not lines:
                    continue

                print(lines)

                if not self._strategy:
                    topCol = self.get_field("TopColumn", lines).split(",")
                    midCol = self.get_field("MidColumn", lines).split(",")
                    botCol = self.get_field("BotColumn", lines).split(",")
                    self._strategy = Strategy(topCol, midCol, botCol)

                state = self.play(
                    state, self.get_field("LastDraw", lines), self.get_field("Message", lines)
                )

                time.sleep(1)
            except:
                self._logger.exception("message")
                time.sleep(1)


class Strategy:
    _topCol = []
    _midCol = []
    _botCol = []
    _xOffsets = 0
    _yOffsets = 0
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
        self._dicColumnsNumbers.fromkeys(range(36))
        for i in range(36):
            if i == 0:
                self._dicColumnsNumbers[i] = Column.NONE
            if i % 3 == 0:
                self._dicColumnsNumbers[i] = Column.TOP
            if i % 3 == 2:
                self._dicColumnsNumbers[i] = Column.MID
            if i % 3 == 1:
                self._dicColumnsNumbers[i] = Column.BOTTOM

    def execute(self, drawNumber):
        try:
            drawNumber = int(drawNumber)

            if self._dicColumnsNumbers[drawNumber] == Column.NONE:
                return True

            if self._dicColumnsNumbers[drawNumber] == Column.TOP:
                self.click_column(self._midCol, self._botCol)

            if self._dicColumnsNumbers[drawNumber] == Column.BOTTOM:
                self.click_column(self._midCol, self._topCol)
            if self._dicColumnsNumbers[drawNumber] == Column.MID:
                self.click_column(self._topCol, self._botCol)

            return True
        except:
            self._logger.exception("message")
            return False

    def click_column(self, col1, col2):
        pyautogui.click(float(col1[0]) + self._xOffsets, float(col1[1]) + self._yOffsets)
        pyautogui.click(float(col2[0]) + self._xOffsets, float(col2[1]) + self._yOffsets)


if __name__ == "__main__":
    try:
        Manager().start()
    except:
        log.MyLogger.__call__().get_logger().exception("message")
