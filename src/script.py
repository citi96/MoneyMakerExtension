from entities.controllers.play_controller import PlayController
from entities.models.play import Play
from log import MyLogger
import time
from strategy import Strategy
from threading import Thread
from enum import Enum
from entities.models.parameter import Parameter
from entities.controllers.parameter_controller import ParameterController
from bs4 import BeautifulSoup
import pyautogui


class State(Enum):
    UNKNOWN = 0
    WAITING_TO_PLAY = 1
    PLAYED = 2


class Manager(Thread):
    _strategy = None
    _logger = None

    def __init__(self):
        super(Manager, self).__init__()
        self._logger = MyLogger.__call__().get_logger()

    def get_field(self, field, html):
        try:
            return html.find_all(class_=field)[0]
        except:
            self._logger.exception("message")
            return ""

    def get_scaled_coords(defaultCoords, defaultResolution):
        currentResolution = pyautogui.size()
        newCoords = [
            defaultCoords[0] / defaultResolution[0] * currentResolution[0],
            defaultCoords[1] / defaultResolution[0] * currentResolution[1],
        ]

        return newCoords

    def save_play(self, amountBet, currentBalance):
        playInfo = PlayController.get_last()
        if playInfo is not None:
            PlayController.update(playInfo, {"final_balance", currentBalance})

        PlayController.save(Play(currentBalance, amountBet), currentBalance)

    def play(self, state, lastDraw, dealerMessage, amountBet, currentBalance):
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
                self.save_play(amountBet, currentBalance)
                return State.PLAYED
            else:
                return State.WAITING_TO_PLAY

        return state

    def get_column_coords(self):
        defaultResolution = [
            ParameterController.get(
                Parameter.DEFAULT_RESOLUTION_X,
                Parameter.DEFAULT_RESOLUTION_Y,
            )
        ]

        colDefaultResolution = [
            ParameterController.get(Parameter.TOP_COLUMN_DEFAULT_COORD_X),
            ParameterController.get(Parameter.TOP_COLUMN_DEFAULT_COORD_Y),
        ]
        topCol = self.get_scaled_coords(
            colDefaultResolution, defaultResolution
        )

        colDefaultResolution = [
            ParameterController.get(
                Parameter.MIDDLE_COLUMN_DEFAULT_COORD_X
            ),
            ParameterController.get(
                Parameter.MIDDLE_COLUMN_DEFAULT_COORD_Y
            ),
        ]
        midCol = self.get_scaled_coords(
            colDefaultResolution, defaultResolution
        )

        colDefaultResolution = [
            ParameterController.get(
                Parameter.BOTTOM_COLUMN_DEFAULT_COORD_X
            ),
            ParameterController.get(
                Parameter.BOTTOM_COLUMN_DEFAULT_COORD_Y
            ),
        ]
        botCol = self.get_scaled_coords(
            colDefaultResolution, defaultResolution
        )

        return [topCol, midCol, botCol]

    def run(self):
        state = State.WAITING_TO_PLAY

        while True:
            try:
                # r = requests.get("file:///C:/Users/f.chiti/Desktop/MoneyMakerExtension/test.html")
                # soup = BeautifulSoup(r.text, "html.parser")
                soup = None
                with open(
                    "C:\\Users\\f.chiti\\Desktop\\MoneyMakerExtension\\test.html"
                ) as file:
                    soup = BeautifulSoup(file, "html.parser")

                if not self._strategy:
                    topCol, midCol, botCol = self.get_column_coords()
                    self._strategy = Strategy(topCol, midCol, botCol)

                self.play(
                    state,
                    self.get_field(
                        "roulette-history-item__value-text4i5PljD88Up2neJ6jtn4S", soup
                    ),
                    self.get_field("dealer-message-text", soup),
                    self.get_field("amount_bet", soup),
                    self.get_field("current_balance", soup),
                )
            except:
                self._logger.exception("message")
            finally:
                time.sleep(2)


if __name__ == "__main__":
    try:
        Manager().start()
    except:
        MyLogger.__call__().get_logger().exception("message")
