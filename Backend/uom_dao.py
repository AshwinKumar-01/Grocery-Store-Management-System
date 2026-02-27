def get_uoms(connection):
    query = "SELECT * FROM UOM;"
    cursor = connection.cursor()
    cursor.execute(query)
    response = []
    for (uom_id,uom_name) in cursor:
        response.append({
            "uom_id" : uom_id,
            "uom_name" : uom_name
        })
    return response

if __name__ == "__main__":
    from sql_connection import get_sql_connection
    connection = get_sql_connection()
