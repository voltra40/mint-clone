import pandas as pd
import json
import csv

file_path = 'Transactions.CSV'
df = pd.read_csv(file_path)

totals_dict = {}

df['Category'] = df['Category'].str.lower()
# Group the DataFrame by the 'Category' column
grouped = df.groupby('Category')

# print(df)

def getTotalByCategory(category_name):
  category_df = df[df['Category'] == category_name]
  total_spent = category_df['Amount'].sum()
  # print(f"Total spent: {total_spent}")
  return total_spent
  
def get_all_totals():
  totals_json = json.dumps(totals_dict)
  # print(totals_json)
  return totals_json

  
# # Open the CSV file
# with open(file_path, newline='') as csvfile:
#     datareader = csv.reader(csvfile)
#     data = [row for row in datareader]
