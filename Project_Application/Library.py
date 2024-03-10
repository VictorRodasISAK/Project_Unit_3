import sqlite3
from passlib.hash import sha256_crypt

hasher = sha256_crypt.using(rounds=30000)

def make_hash(text: str):
    return hasher.hash(text)

def check_hash(text: str, hashed: str):
    return hasher.verify(text, hashed)

class DatabaseWorker:
    def __init__(self, name):
        self.name_db = name
        self.connection = sqlite3.connect(self.name_db)
        self.cursor = self.connection.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, query):
        self.run_query(query)

    def search(self, query, multiple=False):
        results = self.cursor.execute(query)
        if multiple:
            return results.fetchall()
        return results.fetchone()


    def create_tables(self):
        #Users table
        query_users_table = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        given_name TEXT NOT NULL,
        password TEXT NOT NULL,
        schedule TEXT NOT NULL,
        email TEXT NOT NULL
        )"""

        query_materials_table = """CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material_name TEXT NOT NULL,
        material_price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        required_quantity INTEGER NOT NULL
        )"""

        query_customer_table = """CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uname TEXT NOT NULL,
        email TEXT NOT NULL
        )"""

        query_orders_table = """CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        material_id INTEGER NOT NULL,
        color TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        total_price REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
        FOREIGN KEY (material_id) REFERENCES materials(id)
        )"""

        query_purchases_table = """CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        total_price REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (material_id) REFERENCES materials(id)
        )"""

        # self.run_query(query_users_table)
        # self.run_query(query_materials_table)
        # self.run_query(query_customer_table)
        # self.run_query(query_orders_table)
        # self.run_query(query_purchases_table)


    def close(self):
        self.connection.close()