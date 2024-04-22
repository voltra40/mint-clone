from flask import Flask, request, jsonify
from flask_cors import CORS
# import pandas as pd
from read import getAllTotals, getTotalByCategory, getAll

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

if __name__ == '__main__':
    app.run(debug=True)