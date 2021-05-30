import datetime
from core.crud import DBOperator
from core.schemas import DocumentBase


def test_get_document_by_id(prepare_positive):
    actual = DBOperator.get_document_by_id(51)
    assert actual.id == 51
    assert actual.name == 'unique_test_document'
    assert actual.creation_date == datetime.datetime(2021, 5, 27, 21, 0, 21, 642682)
    assert actual.document_content == 'test_content'


def test_get_document_by_id_unexisting(prepare_negative):
    actual = DBOperator.get_document_by_id(51)
    assert actual is None


def test_create_document(prepare_positive):
    document = DocumentBase(id=51, name='unique_test_document',
                            creation_date=datetime.datetime(2021, 5, 27, 21, 0, 21, 642682),
                            document_content='test_content')
    actual = DBOperator.create_document(document)
    assert actual.id == 51
    assert actual.name == 'unique_test_document'
    assert actual.creation_date == datetime.datetime(2021, 5, 27, 21, 0, 21, 642682)
    assert actual.document_content == 'test_content'


def test_delete_document(prepare_positive):
    actual = DBOperator.delete_document(51)
    assert actual


def test_delete_document_unexisting(prepare_negative):
    actual = DBOperator.delete_document(1000)
    assert not actual
