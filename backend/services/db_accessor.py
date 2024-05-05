import os
import psycopg2
from dotenv import load_dotenv
from utils.helpers import convert_date_format
from flask import request

from utils.sql_queries import (
  CREATE_CATEGORY_TABLE,
  INSERT_CATEGORY_RETURN_ID,
  CREATE_TRANSACTIONS_TABLE,
  SELECT_ALL,
  SELECT_ALL_CATEGORIES,
  INSERT_TRANSACTION,
  SELECT_TRANSACTIONS_BY_CATEGORY
)

load_dotenv()
url = os.getenv("DATABASE_URL")

def get_database_connection():
  conn = psycopg2.connect(url)
  conn.autocommit = True
  return conn

# insert category, then insert transaction, creating a relationship
def insert_data_into_db(data):
  with get_database_connection().cursor() as cursor:
    cursor.execute(CREATE_CATEGORY_TABLE)
    cursor.execute(CREATE_TRANSACTIONS_TABLE)
    for index, row in data.iterrows():
      category_id = get_or_create_category(cursor, row)
      insert_transaction(cursor, category_id, row)

unique_categories = []
def get_or_create_category(cursor, row):
  category = row[3]
  print(f"category {category}")
  category_id = 0
  if category not in [item[1] for item in unique_categories]:
    print('not in')
    cursor.execute(INSERT_CATEGORY_RETURN_ID, (category,))
    category_id = cursor.fetchone()[0]
    unique_categories.append((category_id, category))
  else:
    category_id = [item[0] for item in unique_categories if item[1] == category][0]
  print(f"category_id {category_id}")
  return category_id

def insert_transaction(cursor, category_id, row):
  cursor.execute(
    INSERT_TRANSACTION,
    (category_id, convert_date_format(row[0]), convert_date_format(row[1]), row[2], row[3], row[4], row[5], row[6])
  )

def get_all_categories():
  with get_database_connection().cursor() as cursor:
    cursor.execute(SELECT_ALL_CATEGORIES)
    data = cursor.fetchall()
    return data

def get_all_transactions():
  with get_database_connection().cursor() as cursor:
    cursor.execute(SELECT_ALL)
    data = cursor.fetchall()
  return data

def add_new_category():
  try:
    try:
      data = request.get_json()
      category_name = data["name"]
    except Exception:
      category_name = "uncategorized"
    with get_database_connection().cursor() as cursor:
      cursor.execute(CREATE_CATEGORY_TABLE)
      cursor.execute(INSERT_CATEGORY_RETURN_ID, (category_name,))
      category_id = cursor.fetchone()[0]
    return {"id": category_id, "message": f"Category: {category_name} created."}, 201
  except Exception as e:
    return {"error": str(e)}, 500
  
def get_transactions_by_category():
  try:
    category_name = request.args.get("category")
    print(f"category name: {category_name}")
    print(f"category name type: {type(category_name)}")
    with get_database_connection().cursor() as cursor:
      cursor.execute(SELECT_TRANSACTIONS_BY_CATEGORY, (category_name,))
      data = cursor.fetchall()
      return data
  except Exception as e:
    return {"error": str(e)}, 500
