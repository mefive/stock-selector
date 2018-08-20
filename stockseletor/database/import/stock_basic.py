import pandas as pd
import tushare

from stockseletor.database.config import session
from stockseletor.models.stock_basic import StockBasic
from stockseletor.utils import money


def import_stock_basic():
    df: pd.DataFrame = tushare.get_stock_basics(date='2018-08-17')

    if df is not None:
        for index, row in df.iterrows():
            stock_basic = StockBasic(
                code=index,
                name=row['name'],
                pe=money.to_integer(row['pe'])
            )

            session.add(stock_basic)

    session.commit()


if __name__ == '__main__':
    import_stock_basic()
