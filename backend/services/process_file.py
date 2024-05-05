import os
import pandas as pd
from services.db_accessor import insert_data_into_db

cwd = os.getcwd()

def process_and_load_file(filename):
  # read csv
  data = pd.read_csv(cwd + "/uploads/" + filename)
  
  # remove rows where category is empty
  data = data.dropna(subset=['Category'])
  
  # insert all categories and transactions into db
  insert_data_into_db(data)
  