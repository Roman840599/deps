from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime
from .database import metadata


documents = Table('documents', metadata,
                  Column('id', Integer, primary_key=True, index=True),
                  Column('name', String, nullable=False, index=True),
                  Column('creation_date', DateTime, nullable=False, default=datetime.now),
                  Column('document_content', String)
                  )
