import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = """
        SELECT 
            products.product_id, 
            products.product_name, 
            products.unit_of_measure_id, 
            unit_of_measure.unit_of_measure_name, 
            products.price_per_unit 
        FROM 
            products 
        INNER JOIN 
            unit_of_measure ON products.unit_of_measure_id = unit_of_measure.unit_of_measure_id
    """

    cursor.execute(query)

    response = []

    for (product_id, product_name, unit_of_measure_id, unit_of_measure_name, price_per_unit) in cursor:
        response.append({
            "product_id": product_id,
            "product_name": product_name,
            "unit_of_measure_id": unit_of_measure_id,
            "unit_of_measure_name": unit_of_measure_name,
            "price_per_unit": price_per_unit
        })

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = """
        INSERT INTO `grocery_store`.`products`
            (`product_name`, `unit_of_measure_id`, `price_per_unit`)
        VALUES
            (%s, %s, %s)
    """
    data = (product['product_name'], product['unit_of_measure_id'], product['price_per_unit'])
    cursor.execute(query, data)

    connection.commit()

    return cursor.lastrowid
    
def delete_product(connection, product_id):
    cursor = connection.cursor()

    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))

    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 2))
