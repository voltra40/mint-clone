from flask import Flask, request, jsonify
from flask_cors import CORS
# import pandas as pd
from read import getAllTotals, getTotalByCategory, getAll
import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime, timezone

CREATE_CATEGORY_TABLE = """
CREATE TABLE IF NOT EXISTS category (
    id SERIAL PRIMARY KEY,
    name TEXT
);
"""

CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (
    category_id INTEGER,
    date TIMESTAMP,
    name TEXT,
    total DECIMAL(10, 2),
    FOREIGN KEY (category_id) REFERENCES category (id)
    ON DELETE CASCADE
);
"""

INSERT_CATEGORY_RETURN_ID = "INSERT INTO category (name) VALUES (%s) RETURNING id;"
INSERT_TRANSACTION = "INSERT INTO transactions (category_id, date, name, total) VALUES (%s, %s, %s, %s);"


load_dotenv()

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/total_spent', methods=['GET'])
def total_spent():
    category = request.args.get('category')
    if not category:
        return jsonify({"error": "Please specify a category"}), 400
    
    total = getTotalByCategory(category)
    return jsonify({"category": category, "total_spent": total})

@app.route('/api/all', methods=['GET'])
def get_all():
    return jsonify(getAll())

@app.route('/api/totals', methods=['GET'])
def get_totals():
    return getAllTotals()

@app.post("/api/category")
def create_category():
    data = request.get_json()
    category_name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_CATEGORY_TABLE)
            cursor.execute(INSERT_CATEGORY_RETURN_ID, (category_name,))
            category_id = cursor.fetchone()[0]
    return {"id": category_id, "message": f"Category {category_name} created."}, 201

@app.post("/api/transaction")
def add_transaction():
    data = request.get_json()
    category_id = data["category"]
    name = data["name"]
    total = data["total"]
    try:
        date = datetime.strptime(data["date"], "%m-%d-%Y")
    except KeyError:
        date = datetime.now(timezone.utc)
        
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TRANSACTIONS_TABLE)
            cursor.execute(INSERT_TRANSACTION, (category_id, date, name, total))

    return {"message": "Transaction added successfully."}, 201
    
# get repeated purchases 

if __name__ == '__main__':
    app.run(debug=True)