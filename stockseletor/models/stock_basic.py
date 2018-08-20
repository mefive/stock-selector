from sqlalchemy import Column, Integer, String, Date, BigInteger
from stockseletor.models.base import Base


class StockBasic(Base):
    __tablename__ = 'stock_basic'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)
    industry = Column(String)
    area = Column(String)
    pe = Column(String)
    outstanding = Column(Integer)
    totals = Column(Integer)
    totalAssets = Column(Integer)
    liquidAssets = Column(Integer)
    fixedAssets = Column(BigInteger)
    esp = Column(Integer)
    bvps = Column(Integer)
    pb = Column(Integer)
    timeToMarket = Column(Date)
    undp = Column(Integer)
    perundp = Column(Integer)
    rev = Column(Integer)
    profit = Column(Integer)
    npr = Column(Integer)
