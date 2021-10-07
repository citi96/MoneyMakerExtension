from entities.controllers.play_controller import PlayController
from entities.models.play import Play
import log
import time
import os
import strategy
from threading import Thread
from enum import Enum


class State(Enum):
    UNKNOWN = 0
    WAITING_TO_PLAY = 1
    PLAYED = 2


class Manager(Thread):
    _strategy = None
    _logger = None

    def __init__(self):
        super(Manager, self).__init__()
        self._logger = log.MyLogger.__call__().get_logger()

    def get_field(self, field_name, fields, type=str):
        matching = [s for s in fields if field_name in s]
        match = matching[0].split(":")[1].strip().replace("\n","")
        return type(match)

    def save_play(self, playInfo, amountBet, currentBalance):
        if playInfo:
            PlayController.save(playInfo, currentBalance)
        playInfo = Play(currentBalance, amountBet)
        

    def play(self, state, lastDraw, dealerMessage, amountBet, currentBalance, playInfo):
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
                self.save_play(playInfo, amountBet, currentBalance)
                return State.PLAYED
            else:
                return State.WAITING_TO_PLAY

        os.remove("/home/citi/Downloads/Info.txt")
        return state

    def run(self):
        state = State.WAITING_TO_PLAY
        playInfo = None

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
                    topCol = self.get_field("TopColumn", lines, float).split(",")
                    midCol = self.get_field("MidColumn", lines, float).split(",")
                    botCol = self.get_field("BotColumn", lines, float).split(",")
                    self._strategy = strategy.Strategy(topCol, midCol, botCol)

                state = self.play(
                    state, self.get_field("LastDraw", lines, int), self.get_field("Message", lines),
                    state, self.get_field("Bet", lines, float), self.get_field("Balance", lines, float),
                    playInfo
                )
            except:
                self._logger.exception("message")
            finally:
                time.sleep(1)


if __name__ == "__main__":
    try:
        Manager().start()
    except:
        log.MyLogger.__call__().get_logger().exception("message")
