import mysql.connector as mc
import json


def inter_db(query, query_type: str):
    return_value = False
    connection = mc.connect(
        host='localhost',
        user='root',
        password='root',
        database='users'
    )
    cursor = connection.cursor()
    cursor.execute(query)

    if query_type == "commit":
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result
    if query_type == 'fetch_json':
        query_result = json.dumps(cursor.fetchall())
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
