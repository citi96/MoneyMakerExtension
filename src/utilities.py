from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class utilities:
    _engine = None
    _base = None

    @staticmethod
    def get_session():
        return sessionmaker(engine)

    @classmethod
    def get_engine(self):
        if not self._engine:
            self._engine = engine.create_engine("sqlite:///db\\db.db")
        return self._engine

    @classmethod
    def get_base(self):
        if self._base is None:
            self._base = declarative_base(bind=utilities.get_engine())
        return self._base