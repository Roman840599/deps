from datetime import datetime
from pydantic import BaseModel


class DocumentBase(BaseModel):
    name: str
    document_content: str

    class Config:
        orm_mode = True


class DocumentFull(DocumentBase):
    id: int
    creation_date: datetime
