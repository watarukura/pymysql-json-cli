import tempfile

import pytest
from click.testing import CliRunner

from src.main import cli


runner = CliRunner()


@pytest.mark.parametrize(
    "sql, expect",
    (
        (
            "CREATE TABLE test_table(test_column varchar(20) primary key);",
            '{"affected_rows": 0}\n',
        ),
        ("SHOW TABLES;", '[{"Tables_in_test": "test_table"}]\n'),
        (
            "SHOW COLUMNS FROM test_table;",
            '[{"Field": "test_column", "Type": "varchar(20)", "Null": "NO", "Key": "PRI", "Default": null, "Extra": ""}]\n',  # noqa
        ),
        (
            'INSERT INTO test_table(test_column) VALUES("test_value");',
            '{"affected_rows": 1}\n',
        ),
        ("SELECT * FROM test_table;", '[{"test_column": "test_value"}]\n',),
    ),
)
def test_cli(sql: str, expect: str):
    result = runner.invoke(cli, args=[], input=sql)
    assert result.output == expect


@pytest.mark.parametrize(
    "sql, args, expect",
    (
        (
            "INSERT INTO test_table(test_column) VALUES(%(value)s);",
            '{"value": "arg_value"}',
            '{"affected_rows": 1}\n',
        ),
        (
            "SELECT * FROM test_table;",
            None,
            '[{"test_column": "arg_value"}, {"test_column": "test_value"}]\n',
        ),
    ),
)
def test_cli_args(sql: str, args: str, expect: str):
    result = runner.invoke(cli, args=["--args", args], input=sql)
    assert result.output == expect


@pytest.mark.parametrize(
    "sql, args, expect",
    (
        (
            "INSERT INTO test_table(test_column) VALUES(%(value)s);",
            '{"value": "arg_value"}',
            '{"dryrun": "INSERT INTO test_table(test_column) VALUES(arg_value);"}\n',  # noqa
        ),
    ),
)
def test_cli_dryrun(sql: str, args: str, expect: str):
    result = runner.invoke(cli, args=["--args", args, "--dryrun"], input=sql)
    assert result.output == expect


@pytest.mark.parametrize(
    "sql, args, expect",
    (
        (
            "INSERT INTO test_table(test_column) VALUES(%(value)s);",
            '{"value": "file_value"}',
            '{"affected_rows": 1}\n',
        ),
    ),
)
def test_cli_sqlfile(sql: str, args: str, expect: str):
    sql_file = tempfile.NamedTemporaryFile()
    with open(sql_file.name, "w") as f:
        f.write(sql)
    result = runner.invoke(
        cli, args=["--sqlfile", sql_file.name, "--args", args]
    )
    assert result.output == expect
