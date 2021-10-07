from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker

class utilities():
    _engine = None

    @staticmethod
    def get_session():        
        return sessionmaker(engine)

    @staticmethod
    def get_engine():
        if not utilities._engine:
            utilities._engine = engine.create_engine('sqlite:////tmp/teste.db', echo=True)
        return utilities._engine