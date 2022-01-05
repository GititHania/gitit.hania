from typing import NamedTuple
import mysql.connector as mc


def inter_db(query, query_type: str):
    return_value = False
    connection = mc.connect(
        host='localhost',
        user='root',
        passwprd='root',
        database='users'
    )
    cursor = connection.cursor(named_tuple=True)
    cursor.excute(query)

    if query_type == "commit":
        connection.commit()
        return_value=True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value=query_result

    connection.close()
    cursor.close()
    return return_value
