from contextlib import contextmanager

from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

from configs.db_config import connection_configs

engine = create_engine(connection_configs.get_connection_string())
metadata = MetaData()


class DataBaseException(Exception):
    pass


def db_errors_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as ex:
            raise DataBaseException(str(ex))
    return wrapper


@contextmanager
def connect_db():
    connection = engine.connect()
    yield connection
    connection.close()


@db_errors_catcher
def execute_db_command(statement):
    with connect_db() as conn:
        result = conn.execute(statement)
    return result
