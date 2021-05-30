from fastapi.testclient import TestClient
from sqlalchemy import select

from main import app
from core.database import engine
from core.models import documents


client = TestClient(app)


def test_add_document(delete_mock_document):
    response = client.post(
        "/documents/add_document/",
        json={"name": "unique_test_document", "document_content": "test_content"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "unique_test_document"
    assert data["document_content"] == "test_content"


def test_add_document_empty():
    response = client.post(
        "/documents/add_document/",
        json={"name": None, "document_content": None},
    )
    assert response.status_code == 422


def test_read_current_document(create_and_delete_mock_document):
    id = create_and_delete_mock_document
    response = client.get(f"/documents/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "unique_test_document"
    assert data["document_content"] == "test_content"


def test_read_current_document_unexisting():
    response = client.get("/documents/1000000000")
    assert response.status_code == 404


def test_read_current_document_incorrect_url():
    response = client.get("/documentsss/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_read_current_document_incorrect_data_url():
    response = client.get("/documents/a10")
    assert response.status_code == 422
    data = response.json()
    assert data['detail'][0]['msg'] == "value is not a valid integer"


def test_destroy_document(create_mock_document):
    id = create_mock_document
    response = client.delete(f'/documents/delete_document/{id}')
    assert response.status_code == 200
    connection = engine.connect()
    sure_res = connection.execute(select(documents.c.id).where(documents.c.name == 'unique_test_document'))
    row = sure_res.fetchone()
    assert row is None


def test_destroy_document_unexisting():
    response = client.delete('/documents/delete_document/1000000000')
    assert response.status_code == 404
    assert response.json() == {"message": "Document not found"}
