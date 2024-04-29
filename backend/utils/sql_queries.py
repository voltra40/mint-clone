CREATE_CATEGORY_TABLE = """
CREATE TABLE IF NOT EXISTS categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);
"""

CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    category_id INT,
    transaction_date DATE,
    post_date DATE,
    description TEXT,
    category TEXT,
    type TEXT,
    amount DECIMAL(10, 2),
    memo TEXT,
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE
);
"""
INSERT = "INSERT INTO transactions (category_id, transaction_date, post_date, description, category, type, amount, memo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

INSERT_CATEGORY_RETURN_ID = "INSERT INTO categories (name) VALUES (%s) RETURNING category_id;"
# INSERT_TRANSACTION = "INSERT INTO transactions (category_id, date, name, total) VALUES (%s, %s, %s, %s);"

SELECT_ALL = "SELECT * FROM transactions;"
SELECT_ALL_CATEGORIES = "SELECT * FROM categories;" 