from stockselector.models.base import Base
from stockselector.database.config import engine
from stockselector.models.h_data import HData
from stockselector.models.stock_basic import StockBasic


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
