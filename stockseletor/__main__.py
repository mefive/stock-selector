import argparse

from stockseletor.database.import_tool import import_daily

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', help='import data')

    args: argparse.Namespace = parser.parse_args()

    if args.i == 'daily':
        import_daily()
