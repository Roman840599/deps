from fastapi import APIRouter, status

from core.crud import get_document_by_id, create_document, delete_document
from core.schemas import DocumentBase, DocumentFull


router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)


@router.get("/{document_id}", response_model=DocumentFull)
async def read_current_document(document_id: int):
    return get_document_by_id(document_id=document_id)


@router.post("/add_document/", response_model=DocumentFull)
def add_document(document: DocumentBase):
    return create_document(document=document)


@router.delete("/delete_document/{document_id}", status_code=status.HTTP_200_OK,)
def destroy_document(document_id: int):
    return delete_document(document_id=document_id)
