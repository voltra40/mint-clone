import pandas as pd

file_path = 'Chase0470_Activity20240101_20240419_20240419.CSV'
df = pd.read_csv(file_path)

totals_dict = {}

df['Category'] = df['Category'].str.lower()
# Group the DataFrame by the 'Category' column
grouped = df.groupby('Category')

def getTotalByCategory(category_name):
  category_df = df[df['Category'] == category_name]
  total_spent = category_df['Amount'].sum()
  # print(f"Total spent: {total_spent}")
  return total_spent
  
for category_name, group_df in grouped:
    totals_dict[category_name] = getTotalByCategory(category_name)

def getAll():
  data_dict = df.to_dict(orient='records')  # Converts the DataFrame to a list of dictionaries
  print(f"data_dict: {data_dict}")
  return data_dict

def getAllTotals():
  print(totals_dict)
  return totals_dict
