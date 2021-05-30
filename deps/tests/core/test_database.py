import pytest

from core import database


def test_execute_db_command_empty():
    with pytest.raises(database.DataBaseException) as excinfo:
        database.execute_db_command('')
    assert "can't execute an empty query" in str(excinfo.value)


def test_execute_db_command_incorrect():
    statement = "SELECTCTX * FROM documents;"
    with pytest.raises(database.DataBaseException) as excinfo:
        database.execute_db_command(statement)
    assert 'syntax error at or near "SELECTCTX"' in str(excinfo.value)


def test_execute_db_command_empty_connection(prepare_connection_for_execute_command):
    statement = "SELECT * FROM documents;"
    with pytest.raises(AttributeError) as excinfo:
        database.execute_db_command(statement)
    assert "'NoneType' object has no attribute 'execute'" in str(excinfo.value)
