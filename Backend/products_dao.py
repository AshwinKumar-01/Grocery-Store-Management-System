#DAO --> Data Access object
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM grocery_store_management.products;"
    query1 = "SELECT products.product_id,products.product_name,uom.uom_name,products.price_per_unit FROM products JOIN uom on products.uom_id = uom.uom_id"

    cursor.execute(query1)
    response = []
    for (product_id,product_name,uom_name,price_per_unit) in cursor:
        response.append(
            {
            "product_id":product_id,
            "product_name":product_name,
            "uom_name":uom_name,
            "price_per_unit":price_per_unit
            }
        )
        print(product_id,product_name,uom_name,price_per_unit)
        print(response)

    #connection.close()
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO grocery_store_management.products(product_name,uom_id,price_per_unit) VALUES (%s,%s,%s)")
    data = (product["product_name"],product["uom_id"],product["price_per_unit"])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def edit_product(connection,product):
    cursor=connection.cursor()
    query = "UPDATE grocery_store_management.products SET product_name=%s,uom_id=%s,price_per_unit=%s WHERE product_id=%s"
    data = (product["product_name"],product["uom_id"],product["price_per_unit"],product["product_id"])
    cursor.execute(query,data)
    connection.commit()

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id=" + str(product_id)
    cursor.execute(query)
    connection.commit()

if __name__=="__main__":
    connection = get_sql_connection()
    product = {
        "product_name":"Potato",
        "uom_id":"2",
        "price_per_unit":"30"
    }
    print(insert_new_product(connection,product))
    print(get_all_products(connection))
    print(delete_product(connection,6))
