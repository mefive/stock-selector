import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_db_path():
    return os.path.join(os.path.dirname(__file__), './data.db')


engine = create_engine('sqlite:///' + get_db_path(), echo=True)
session: Session = sessionmaker(bind=engine)()
