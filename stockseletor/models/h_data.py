from sqlalchemy import Column, Integer, String, Date, BigInteger
from stockseletor.models.base import Base


class HData(Base):
    __tablename__ = 'h_data'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    date = Column(Date)
    open = Column(Integer)
    high = Column(Integer)
    close = Column(Integer)
    volume = Column(BigInteger)
    amount = Column(BigInteger)

