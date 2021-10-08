from sqlalchemy.sql.expression import false
from entities.models.play import Play
from utilities import utilities


class PlayController:
    @staticmethod
    def save(play: Play, finalBalance):
        with utilities.get_session() as session, session.begin():
            play.final_balance = finalBalance
            session.add(play)

    @staticmethod
    def update(play: Play, props):
        with utilities.get_session() as session, session.begin():
            for key, value in props.items():
                setattr(play, key, value)

    @staticmethod
    def get_last():
        plays = []
        with utilities.get_session() as session, session.begin():
             plays = session.query(Play).order_by(Play.date_time.desc()).limit(1).all()
        
        return next(iter(plays or []), None)