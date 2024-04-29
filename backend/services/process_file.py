import json
import csv
import os
import pandas as pd
from services.db_accessor import insert_data_into_db, auto_create_categories
from utils.helpers import get_all_unique_categories

cwd = os.getcwd()

def process_and_load_file(filename):
  # read csv
  data = pd.read_csv(cwd + "/uploads/" + filename)
  # remove rows where category is empty
  data = data.dropna(subset=['Category'])
  # # get unique categories from local file
  # unqiue_categories = get_all_unique_categories(data)
  
  # # populate categories table automatically
  # auto_create_categories(unqiue_categories)
  
  # insert all categories and transactions into db
  insert_data_into_db(data)
  