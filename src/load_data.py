import pandas as pd

# Load CSV file
csv_data=pd.read_csv('../data/raw/students_coffee_crisis.csv')
print("CSV data :")
print(csv_data.head())

# Load JSON file
json_data=pd.read_json('../data/raw/students_coffee_crisis.json', orient='records')
print("JSON data :")
print(json_data.head())

# Load Excel file
excel_data=pd.read_excel('../data/raw/student_coffee_crisis.xlsx')
print("Excel data :")
print(excel_data.head())
