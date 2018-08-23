import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_db_path():
    return 'sqlite:///' + os.path.join(os.path.dirname(__file__), './data.db')

def get_my_sql_url():
    return 'mysql+mysqldb://mefive:123@localhost/stock?charset=utf8&use_unicode=1'



engine = create_engine(get_my_sql_url(), echo=True, convert_unicode=True)
session: Session = sessionmaker(bind=engine)()
