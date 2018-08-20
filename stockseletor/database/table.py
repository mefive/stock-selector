from stockseletor.models.base import Base
from stockseletor.database.config import engine
from stockseletor.models.h_data import HData
from stockseletor.models.stock_basic import StockBasic


def create_table():
    Base.metadata.create_all(
        bind=engine,
        tables=[
            HData.__table__,
            StockBasic.__table__
        ]
    )


if __name__ == '__main__':
    create_table()
