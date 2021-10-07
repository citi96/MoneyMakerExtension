import time
import pyautogui
import log
from enum import Enum

class Column(Enum):
    NONE = 0
    TOP = 1
    MID = 2
    BOTTOM = 3

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
            if self._dicColumnsNumbers[drawNumber] == Column.NONE:
                return True

            if self._dicColumnsNumbers[drawNumber] == Column.TOP:
                self.click_columns(self._midCol, self._botCol)
            if self._dicColumnsNumbers[drawNumber] == Column.BOTTOM:
                self.click_columns(self._midCol, self._topCol)
            if self._dicColumnsNumbers[drawNumber] == Column.MID:
                self.click_columns(self._topCol, self._botCol)

            return True
        except:
            self._logger.exception("message")
            return False

    def click_columns(self, col1, col2):
        self.click(col1[0] + self._xOffsets, col1[1] + self._yOffsets)
        self.click(col2[0] + self._xOffsets, col2[1] + self._yOffsets)

    def click(self, x, y, duration=0):
        pyautogui.moveTo(x,y, duration=duration)
        time.sleep(duration)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()    