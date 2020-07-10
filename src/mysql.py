import os
from typing import Any, Optional, Tuple, Union

import pymysql


def get_connection() -> pymysql.connections.Connection:
    connection = pymysql.connect(
        host=os.environ["HOST"],
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
        db=os.environ["DB"],
        port=os.environ["PORT"],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    return connection


def query(sql: str, args={}) -> Optional[Union[Tuple[Any, ...]]]:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()


def command(sql: str, args={}) -> str:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            if args:
                affected_rows = cursor.execute(sql, args)
            else:
                affected_rows = cursor.execute(sql)
            conn.commit()
            return f"affected_rows: {affected_rows}"
    finally:
        conn.close()
