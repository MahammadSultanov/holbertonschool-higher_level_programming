from flask import Flask, render_template, request, jsonify
import json
import csv
from os import error
import sqlite3

app = Flask(__name__)

def read_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

def read_sql_data(db_path, query):
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    cursor.close()
    conn.close()

    result = [dict(zip(column_names, row)) for row in rows]

    return result

def filter_data_by_id(data, product_id):
    return [product for product in data if product['id'] == product_id]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
            items = data.get('items', [])
    except FileNotFoundError:
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error_message = None
    
    if source == 'json':
        data = read_json_data('products.json')
    elif source == 'csv':
        data = read_csv_data('products.csv')
    elif source == 'sql':
        query = "SELECT * FROM products"
        data, error_message = read_sql_data('products.db', query)
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)
    
    if not error_message and product_id:
        data = filter_data_by_id(data, int(product_id))
    if not data:
        error_message = "Product not found"
    
    return render_template('product_display.html', products=data, error=error_message)
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)