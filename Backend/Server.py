from flask import Flask,request,jsonify
from sql_connection import get_sql_connection
import products_dao
import uom_dao
import json
import insert_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route("/getProducts",methods=["GET"])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/getAllOrders",methods=["Get"])
def get_orders():
    orders = insert_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/insertOrder",methods=["POST"])
def insert_order():
    request_payload = json.loads(request.form["data"])
    order_id = insert_dao.insert_order(connection,request_payload)
    response = jsonify({
        "order_id":order_id
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/insertProduct",methods=["POST"])
def insert_products():
    print(request.form["data"])
    request_payload = json.loads(request.form["data"])
    product_id = products_dao.insert_new_product(connection,request_payload)
    print(request_payload)
    response = jsonify({
        "product_id" : product_id
    })
    print(response)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/deleteProduct",methods=["POST"])
def delete_product():
    try:
        return_id = products_dao.delete_product(connection,request.form["product_id"])
        response = jsonify({
            'product_id' : return_id
        })
        print(return_id)
        response.headers.add("Access-Control-Allow-Origin","*")
        return response
    except:
        return "An unexpected error occurred."

@app.route("/editProduct",methods=["POST"])
def Edit_Product():
    request_payload = json.loads(request.form["data"])
    return_id = products_dao.edit_product(connection,request_payload)
    response=jsonify({
        'product_id':return_id
    })
    print("Edit: \n",return_id)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/getUOM",methods=["GET"])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

if __name__ == "__main__":
    print("Running Flask For Grocery App")
    print(__name__)
    app.run()

