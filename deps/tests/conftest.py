import datetime
import pytest
from unittest.mock import Mock
from sqlalchemy import delete, insert, select
from core.database import engine
from core.models import documents


@pytest.fixture
def create_mock_document():
    connection = engine.connect()
    connection.execute(insert(documents).values(name='unique_test_document', document_content='test_content'))
    res = connection.execute(select(documents.c.id).where(documents.c.name == 'unique_test_document'))
    connection.close()
    row = res.fetchone()
    id = row._mapping['id']
    yield id


@pytest.fixture
def create_and_delete_mock_document():
    connection = engine.connect()
    connection.execute(insert(documents).values(name='unique_test_document', document_content='test_content'))
    res = connection.execute(select(documents.c.id).where(documents.c.name == 'unique_test_document'))
    connection.close()
    row = res.fetchone()
    id = row._mapping['id']
    yield id
    connection = engine.connect()
    connection.execute(delete(documents).where(documents.c.name == 'unique_test_document'))
    connection.close()


@pytest.fixture
def delete_mock_document():
    yield None
    connection = engine.connect()
    connection.execute(delete(documents).where(documents.c.name == 'unique_test_document'))
    connection.close()


@pytest.fixture
def prepare_positive(mocker):
    mock_db_object = Mock()
    mock_db_object.fetchone.return_value = (51, 'unique_test_document',
                                            datetime.datetime(2021, 5, 27, 21, 0, 21, 642682), 'test_content')
    mocker.patch('core.crud.execute_db_command', return_value=mock_db_object)


@pytest.fixture
def prepare_negative(mocker):
    mock_db_object = Mock()
    mock_db_object.fetchone.return_value = None
    mocker.patch('core.crud.execute_db_command', return_value=mock_db_object)


@pytest.fixture
def prepare_connection_for_execute_command(mocker):
    mocker.patch('core.database.engine.connect', return_value=None)
