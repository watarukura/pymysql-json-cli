import pytest
from click.testing import CliRunner

from src.main import cli


runner = CliRunner()


@pytest.mark.parametrize(
    "sql, expect",
    (
        (
            "SHOW DATABASES;\n",
            '[{"Database": "information_schema"}, {"Database": "test"}]\n',
        ),
    ),
)
def test_cli(sql: str, expect: str):
    result = runner.invoke(cli, args=[], input=sql)
    assert result.output == expect
