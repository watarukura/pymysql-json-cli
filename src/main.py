import json
import re

import click

from src.mysql import command, query


@click.command()
@click.option(
    "--sqlfile", type=click.Path(exists=True, readable=True), help="sql file"
)
@click.option("--args", type=str, help="JSON for sql template")
@click.option("--dryrun", is_flag=True, help="dryrun mode")
def cli(sqlfile: str, args=None, dryrun=False):
    if sqlfile:
        with open(sqlfile, "r") as f:
            sql = f.read()
    else:
        stdin_text = click.get_text_stream("stdin")
        sql = stdin_text.read()
        stdin_text.close()

    if args:
        args_dict = json.loads(args)
    else:
        args_dict = {}

    if dryrun:
        sql_text = re.sub(
            r"%\((?P<arg>.+)\)s", r"{\g<arg>}", sql.replace("\n", "")
        ).format(**args_dict)
        result = {"dryrun": sql_text}
    elif sql.strip().upper().startswith(
        "SELECT"
    ) or sql.strip().upper().startswith("SHOW"):
        result = query(sql, args_dict)
    else:
        result = command(sql, args_dict)
    click.echo(json.dumps(result))


def main():
    cli()


if __name__ == "__main__":
    main()
