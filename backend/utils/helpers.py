from datetime import datetime, timezone

def convert_date_format(date_string):
    # convert MM/DD/YYYY to YYYY-MM-DD
    try:
      date_obj = datetime.strptime(date_string, '%m/%d/%Y')
    except Exception:
      date_obj = datetime.now(timezone.utc)
    return date_obj.strftime('%Y-%m-%d')
  
def get_all_unique_categories(data):
  unique_categories = data['Category'].unique().tolist()
  print(f"unique categories: {unique_categories}")
  return unique_categories
