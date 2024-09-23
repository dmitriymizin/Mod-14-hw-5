import sqlite3

def initiate_db():
    connection = sqlite3.connect('db_products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def add_products(title, description, price):
    connection = sqlite3.connect('db_products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('db_products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    prods = cursor.fetchall()
    connection.close()
    return prods

def add_user(username, email, age):
    connection = sqlite3.connect('db_products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('db_products.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = check_user.fetchone()
    connection.close()
    return user is not None









