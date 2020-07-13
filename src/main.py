import json
import re

import click

from src.mysql import command, query


@click.command()
@click.option("--args", type=str, help="json args")
@click.option("--dryrun", is_flag=True, help="dryrun mode")
def cli(args=None, dryrun=False):
    stdin_text = click.get_text_stream("stdin")
    sql = stdin_text.read()
    stdin_text.close()

    if args:
        args_dict = json.loads(args)
    else:
        args_dict = {}

    if dryrun:
        result = re.sub(
            r"%\((?P<arg>.+)\)s", r"{\g<arg>}", sql.replace("\n", "")
        ).format(**args_dict)
    elif sql.upper().startswith("SELECT") or sql.upper().startswith("SHOW"):
        result = query(sql, args_dict)
    else:
        result = command(sql, args_dict)
    click.echo(json.dumps(result))


def main():
    cli()


if __name__ == "__main__":
    main()
