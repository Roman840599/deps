from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy import create_engine

from settings import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

documents = Table('documents', metadata,
                  Column('id', Integer, primary_key=True, index=True),
                  Column('name', String, nullable=False, index=True),
                  Column('creation_date', DateTime, nullable=False, default=datetime.now),
                  Column('document_content', String)
                  )
