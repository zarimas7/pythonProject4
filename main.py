import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_all_products(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products''')

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)

def select_products_by_price(conn, price_limit, quontity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price < ? and quontity > ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit,quontity_limit, ))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)

def update_product(conn, product):
    try:
        sql = '''
        UPDATE products SET price = ?, quontity = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)

def delete_product(conn, id):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_product(conn, product):
    try:
        sql = '''
        INSERT INTO products (product_title, price, quontity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


sql_create_product_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL, 
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quontity INTEGER (5) NOT NULL DEFAULT 0
)
'''



db_name = 'hw.db'
connection = create_connection(db_name)
if connection is not None:
    # create_table(connection, sql_create_product_table)
    # create_product(connection, ('butter', 105.50, 40))
    # select_all_products(connection)
    # select_products_by_price(connection, 100, 5)
    # update_product(connection, (30.50, 15, 2))
    delete_product(connection, 2)

    connection.close()
    print('Successfully')




