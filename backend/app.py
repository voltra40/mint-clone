from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from services.db_accessor import get_all_categories, get_all_transactions, add_new_category, get_transactions_by_category
from services.process_file import process_and_load_file
from werkzeug.utils import secure_filename

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

@app.post("/api/add_new_category")
def category_api():
    return add_new_category()

@app.route('/api/transactions', methods=['GET'])
def transactions_by_category_api():
    transactions = get_transactions_by_category()
    return jsonify(transactions)
    
# get all unique categories

# @app.post("/api/transaction")
# def add_transaction():
#     data = request.get_json()
#     category_id = data["category"]
#     name = data["name"]
#     total = data["total"]
#     try:
#         date = datetime.strptime(data["date"], "%m-%d-%Y")
#     except KeyError:
#         date = datetime.now(timezone.utc)
        
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(CREATE_TRANSACTIONS_TABLE)
#             cursor.execute(INSERT_TRANSACTION, (category_id, date, name, total))

#     return {"message": "Transaction added successfully."}, 201

@app.route('/api/get_all_transactions', methods=['GET'])
def transactions_api():
    transactions = get_all_transactions()
    return jsonify(transactions)

@app.route('/api/get_all_categories', methods=['GET'])
def categories_api():
    categories = get_all_categories()
    return jsonify(categories)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        cwd = os.getcwd()
        filename = secure_filename(file.filename)
        file.save(os.path.join(cwd + "/uploads/" + filename))
        process_and_load_file(filename)
        return jsonify({'message': 'File processed successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

# get repeated purchases 

if __name__ == '__main__':
    app.run(debug=True)