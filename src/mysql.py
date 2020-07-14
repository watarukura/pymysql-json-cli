import os
from typing import Any, Optional, Tuple, Union

import pymysql


def get_connection() -> pymysql.connections.Connection:
    connection = pymysql.connect(
        host=os.environ["HOST"],
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
        db=os.environ["DB"],
        port=int(os.environ["PORT"]),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    return connection


def query(sql: str, args={}) -> Optional[Union[Tuple[Any, ...]]]:
    """SELECT / SHOW SQL execute

    Args:
        sql (str): SQL
        args (dict, optional): argument. Defaults to {}.

    Returns:
        Optional[Union[Tuple[Any, ...]]]: query result
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()


def command(sql: str, args={}) -> dict:
    """INSERT / UPDATE / ... SQL execute

    Args:
        sql (str): SQL
        args (dict, optional): argumnt. Defaults to {}.

    Returns:
        dict: affected rows count
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(sql, args)
            conn.commit()
            return {"affected_rows": affected_rows}
    finally:
        conn.close()
