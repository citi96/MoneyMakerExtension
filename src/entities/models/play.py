from datetime import datetime
from sqlalchemy import Column, Integer, Float
from sqlalchemy.sql.sqltypes import DateTime
from utilities import utilities

Base = utilities.get_base()


class Play(Base):
    __tablename__ = "plays"
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, default=datetime.now())
    initial_balance = Column(Float)
    bet = Column(Float)
    final_balance = Column(Float)

    def __init__(self, initial_balance, bet, final_balance=0):
        self.initial_balance = initial_balance
        self.bet = bet
        self.final_balance = final_balance


Base.metadata.create_all()
