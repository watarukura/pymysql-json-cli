import pytest
from click.testing import CliRunner

from src.main import cli


runner = CliRunner()


@pytest.mark.parametrize(
    "sql, expect",
    (
        (
            "SHOW DATABASES;",
            '[{"Database": "information_schema"}, {"Database": "test"}]\n',
        ),
        (
            "CREATE TABLE test_table(test_column varchar(20) primary key);",
            '"affected_rows: 0"\n',
        ),
        ("SHOW TABLES;", '[{"Tables_in_test": "test_table"}]\n'),
        (
            "SHOW COLUMNS FROM test_table;",
            '[{"Field": "test_column", "Type": "varchar(20)", "Null": "NO", "Key": "PRI", "Default": null, "Extra": ""}]\n',
        ),
        (
            'INSERT INTO test_table(test_column) VALUES("test_value");',
            '"affected_rows: 1"\n',
        ),
        ("SELECT * FROM test_table;", '[{"test_column": "test_value"}]\n',),
    ),
)
def test_cli(sql: str, expect: str):
    result = runner.invoke(cli, args=[], input=sql)
    assert result.output == expect
