import os
import tushare
import pandas as pd
import sqlite3
from dateutil import parser
from tradingtrainer.utils import money
import datetime


def get_db_path():
    return os.path.join(os.path.dirname(__file__), '../../db/daily.db')


def get_dates():
    print("=== get_dates ===")
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT date FROM dce_daily;")
    dates = cursor.fetchall()
    cursor.close()
    conn.close()

    dates = list(map(lambda d: parser.parse(d[0]).strftime("%Y-%m-%d"), dates))

    return dates


def import_dce_daily(date):
    print("=== import_dce_daily {0} ===".format(date))

    df: pd.DataFrame = tushare.get_dce_daily(date)

    # dff = df[df.apply(lambda x: x['symbol'] == 'J1805', axis=1)]
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    if df is not None:
        for index, row in df.iterrows():
            cursor.execute(
                """INSERT INTO 
                    dce_daily(symbol, date, open, high, low, close, 
                    volume, open_interest, turnover, settle, pre_settle, is_no_data) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                (
                    row["symbol"],
                    parser.parse(row["date"]),
                    money.to_integer(row["open"]),
                    money.to_integer(row["high"]),
                    money.to_integer(row["low"]),
                    money.to_integer(row["close"]),
                    row["volume"],
                    row["open_interest"],
                    row["turnover"],
                    row["settle"],
                    row["pre_settle"],
                    0,
                ))
    else:
        cursor.execute(
            """INSERT INTO 
                dce_daily(date, is_no_data) 
                VALUES (?, ?);""",
            (
                parser.parse(date),
                1,
            ))
        print("no data on {0}".format(date))

    cursor.close()
    conn.commit()
    conn.close()


def import_daily():
    print("=== main ===")

    dates: list = get_dates()

    for i in range(200, 300):
        date = datetime.date.today() - datetime.timedelta(days=i)
        date = date.strftime("%Y-%m-%d")

        if date not in dates:
            import_dce_daily(date)
