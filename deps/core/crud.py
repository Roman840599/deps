import logging

from sqlalchemy import select, insert, delete

from .database import execute_db_command
from .models import documents
from .schemas import DocumentBase, DocumentFull


logger = logging.getLogger(__name__)


class DBOperator:

    @staticmethod
    def create_document(document: DocumentBase):
        result_document = None
        statement = insert(documents).values(name=document.name, document_content=document.document_content)\
            .returning(documents.c.id, documents.c.name, documents.c.creation_date, documents.c.document_content)
        db_object = execute_db_command(statement)
        document_tuple = db_object.fetchone()
        if document_tuple:
            id, name, creation_date, document_content = document_tuple
            result_document = DocumentFull(id=id, name=name, creation_date=creation_date,
                                           document_content=document_content)
            logger.info(f'DB insert operation performed successfully, document.id={id} deleted.')
        return result_document

    @staticmethod
    def get_document_by_id(document_id: int):
        result_document = None
        statement = select(documents).where(documents.c.id == document_id)
        db_object = execute_db_command(statement)
        document_tuple = db_object.fetchone()
        if document_tuple:
            id, name, creation_date, document_content = document_tuple
            result_document = DocumentFull(id=id, name=name, creation_date=creation_date,
                                           document_content=document_content)
        return result_document

    @staticmethod
    def delete_document(document_id: int):
        delete_result = False
        statement = delete(documents).where(documents.c.id == document_id).\
            returning(documents.c.id, documents.c.name, documents.c.creation_date, documents.c.document_content)
        db_object = execute_db_command(statement)
        document_tuple = db_object.fetchone()
        if document_tuple:
            delete_result = True
            logger.info(f'DB delete operation performed successfully, document.id={document_id} deleted.')
        return delete_result
