from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection,order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO grocery_store_management.orders(customer_name,total,datetime) VALUES (%s,%s,%s)")
    order_data = (order["customer_name"],order["grand_total"],datetime.now())
    cursor.execute(order_query,order_data)
    order_id = cursor.lastrowid
    print(order_id)
    order_details_query = ("INSERT INTO grocery_store_management.order_details(order_id,product_id,quantity,total_price) VALUES (%s,%s,%s,%s)")
    order_details_data = []
    print(order["order_details"])
    for order_detail_record in order["order_details"]:
        order_details_data.append([
            int(order_id),
            int(order_detail_record["product_id"]),
            float(order_detail_record["quantity"]),
            float(order_detail_record["total_price"])
        ])
    cursor.executemany(order_details_query,order_details_data)
    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT datetime,order_id,customer_name,total FROM grocery_store_management.orders;"
    cursor.execute(query)
    #connection.commit()
    response = []
    for datetime,order_id,customer_name,total in cursor:
        response.append({
            "datetime":datetime,
            "order_id":order_id,
            "customer_name":customer_name,
            "total":total
        })
    return response

if __name__ == "__main__":
    connection = get_sql_connection()
    order = {
        "customer_name":"Ironman",
        "grand_total": "150",
        "datetime":datetime.now(),
        "order_details":[
            {
                "product_id":16,
                "quantity":2,
                "total_price":40
            },
            {
                "product_id":17,
                "quantity":5,
                "total_price":450
            }
        ]

    }
    print(insert_order(connection,order))