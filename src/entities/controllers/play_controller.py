from sqlalchemy.sql.expression import false
from entities.models.play import Play
from utilities import utilities

class PlayController():
    @staticmethod
    def save(play: Play, finalBalance):
        with utilities.get_session() as session, session.begin():
            play.final_balance = finalBalance
            session.add(play)