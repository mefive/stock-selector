import pandas as pd
import tushare
from dateutil import parser
from dateutil.relativedelta import relativedelta

from stockseletor.database.config import session
from stockseletor.models.h_data import HData
from stockseletor.utils import money

index_codes = {
    '000001',
    '399001',
    '399006',
    '000016',
    '000300'
}


def import_index_h_data():
    start = parser.parse('2010-01-01')
    end = parser.parse('2010-12-31')

    while start != parser.parse('2012-01-01'):
        for code in index_codes:
            import_h_data(code, start, end)

        start = start + relativedelta(years=1)
        end = end + relativedelta(years=1)


def import_h_data(code, start, end):
    print('=== import h data ===')
    print('start: {:%Y-%m-%d} end: {:%Y-%m-%d}'.format(start, end))

    df: pd.DataFrame = tushare.get_h_data(
        code=code,
        start='{:%Y-%m-%d}'.format(start),
        end='{:%Y-%m-%d}'.format(end),
        index=True
    )

    if df is not None:
        for index, row in df.iterrows():
            h_data = HData(
                code=code,
                date=index,
                open=row['open'],
                close=row['close'],
                high=row['high'],
                volume=row['volume'],
                amount=row['amount']
            )

            session.add(h_data)

        session.commit()

    print('done')


if __name__ == '__main__':
    import_index_h_data()
