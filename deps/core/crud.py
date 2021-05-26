import logging
from sys import exc_info

from fastapi import HTTPException, status
from sqlalchemy import select, insert, delete

from core.models import engine
from .models import documents
from .schemas import DocumentBase, DocumentFull


logger = logging.getLogger(__name__)


def get_document_by_id(document_id: int):
    global result
    try:
        result_document = None
        statement = select(documents).where(documents.c.id == document_id)
        connection = engine.connect()
        result = connection.execute(statement)
        connection.close()
        if result.rowcount == 1:
            for id, name, creation_date, document_content in result:
                result_document = DocumentFull(id=id, name=name, creation_date=creation_date,
                                               document_content=document_content)
            return result_document
    except Exception:
        logger.error(exc_info())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Something went wrong.'
        )
    finally:
        if result.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no such document in DB.'
            )


def create_document(document: DocumentBase):
    try:
        result_document = None
        statement = insert(documents).values(name=document.name, document_content=document.document_content).returning(
            documents.c.id, documents.c.name, documents.c.creation_date, documents.c.document_content)
        connection = engine.connect()
        result = connection.execute(statement)
        connection.close()
        for id, name, creation_date, document_content in result:
            result_document = DocumentFull(id=id, name=name, creation_date=creation_date,
                                           document_content=document_content)
            logger.info(f'Created new document, document.id={id}, document.name={name}.')
        return result_document
    except Exception:
        logger.error(exc_info())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Something went wrong.'
        )


def delete_document(document_id: int):
    global result
    try:
        statement = delete(documents).where(documents.c.id == document_id)
        connection = engine.connect()
        result = connection.execute(statement)
        connection.close()
        if result.rowcount != 0:
            logger.info(f'Document (document.id={document_id}) deleted.')
    except Exception:
        logger.error(exc_info())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Something went wrong.'
        )
    finally:
        if result.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no such document in DB.'
            )
