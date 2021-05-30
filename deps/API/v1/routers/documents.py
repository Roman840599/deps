from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.crud import DBOperator
from core.schemas import DocumentBase, DocumentFull


router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)


@router.get(
    "/{document_id}",
    response_model=DocumentFull,
    responses={
        200: {
            'description': 'Successful response',
            'content': {
                'application/json': {},
            },
        },
        404: {
            'description': 'Document not found',
        },
    },
)
async def read_current_document(document_id: int):

    """
    Return current document by it's document_id.
    In case document's absence in DB will return appropriate JSONResponse.
    """

    result = DBOperator.get_document_by_id(document_id)
    if result:
        return result
    else:
        return JSONResponse(status_code=404, content={"message": "Document not found"})


@router.post("/add_document/", response_model=DocumentFull)
def add_document(document: DocumentBase):

    """Create document using schema DocumentBase"""

    return DBOperator.create_document(document)


@router.delete(
    "/delete_document/{document_id}",
    responses={
            200: {
                'description': 'Successful response',
                'content': {
                    'application/json': {},
                },
            },
            404: {
                'description': 'Document not found',
            },
    }
)
def destroy_document(document_id: int):

    """Delete document by it's id and return JSONResponse."""

    result = DBOperator.delete_document(document_id)
    if result:
        return JSONResponse(status_code=200, content={"message": "Document deleted"})
    else:
        return JSONResponse(status_code=404, content={"message": "Document not found"})
