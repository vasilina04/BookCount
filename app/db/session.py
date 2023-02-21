import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import config
from app.core.config import settings
from app.db.base_class import Base


def connect_sqlalc():
    try:
        sqlite_connection = sqlite3.connect('books.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

    print('\nПопытка подключения к базе данных...\n')
    database_url = "sqlite:///./books.db"
    settings.SQLALCHEMY_DATABASE_URI = database_url
    engine = create_engine(config.settings.SQLALCHEMY_DATABASE_URI, echo=True)
    return engine


engine = connect_sqlalc()
SessionLocal = sessionmaker(autocommit=False, expire_on_commit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)
