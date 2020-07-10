import json

import click

from src.mysql import command, query


@click.command()
@click.option("--args", type=str, help="json args")
def cli(sql, args=None):

    if args:
        args_dict = json.loads(args)
    else:
        args_dict = {}

    if sql.upper.startswith("SELECT") or sql.upper.startswith("SHOW"):
        result = query(sql, args_dict)
    else:
        result = command(sql, args_dict)
    click.echo(json.dumps(result))


def main():
    stdin_text = click.get_text_stream("stdin")
    sql = stdin_text.read()
    stdin_text.close()
    cli(sql)


if __name__ == "__main__":
    main()
