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
                industry=row['industry'],
                area=row['area'],
                pe=row['pe'],
                outstanding=row['outstanding'],
                totals=row['totals'],
                total_assets=row['totalAssets'],
                liquid_assets=row['liquidAssets'],
                fixed_assets=row['fixedAssets'],
                esp=row['esp'],
                bvps=row['bvps'],
                pb=row['pb'],
                time_to_market=row['timeToMarket'] if row['timeToMarket'] != 0 else None,
                undp=row['undp'],
                perundp=row['perundp'],
                rev=row['rev'],
                profit=row['profit'],
                npr=row['npr'],
            )

            session.add(stock_basic)

    session.commit()


if __name__ == '__main__':
    import_stock_basic()
