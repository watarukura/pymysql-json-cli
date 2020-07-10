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
            "CREATE TABLE aaa(aaa varchar(8) primary key);",
            '"affected_rows: 0"\n',
        ),
        ("SHOW TABLES;", '[{"Tables_in_test": "aaa"}]\n'),
        (
            "SHOW COLUMNS FROM aaa;",
            '[{"Field": "aaa", "Type": "varchar(8)", "Null": "NO", "Key": "PRI", "Default": null, "Extra": ""}]\n',
        ),
    ),
)
def test_cli(sql: str, expect: str):
    result = runner.invoke(cli, args=[], input=sql)
    assert result.output == expect
