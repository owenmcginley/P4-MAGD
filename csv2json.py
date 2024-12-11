import csv
import json
import sys
from pathlib import Path
import ast


# json_columns = ['id', 'keywords']

"""Convert csv file into json file"""

# # Read CSV file and convert to list of dictionaries, one per row
# csv_file = 'listings_gz_small.csv'
# with open(f"{csv_file}", mode='r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     data = [row for row in reader]

# # Evaluate the json columns, which are quoted, to convert them into a dictionary or list of dictionaries
# # print(type(data[0]), data[0])
# for row in data:
#     for col in json_columns:
#         try:
#             # evaluate row[col] as dict or list of dicts
#             row[col] = ast.literal_eval(row[col])
#             # print(f"SETTING {col} TO {row[col]}")
#         except Exception as e:
#             pass  # ignore - not a good practice, in general

# # Write JSON output to file
# json_file = Path(csv_file).with_suffix('.json')
# with open(f"{json_file}", mode='w') as f:
#     json.dump(data, f)

# input_dir = input('Entra el directorio de los archivos csv: ')
# output_dir = input('Entra el directorio de los archivos json: ')

# if input_dir == '':
#     input_dir = 'csv'
# if output_dir == '':
#     output_dir = 'json'

def converter(csv_file, input_dir, output_dir):
    with open(f"{input_dir}/{csv_file}", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    keys = list(data[0].keys())
    for row in data:
        for col in keys:
            try:
                row[col] = ast.literal_eval(row[col])
            except Exception as e:
                pass  # ignore - not a good practice, in general

    json_file = Path(csv_file).with_suffix('.json')
    with open(f"{output_dir}/{json_file}", mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def main():
    # Verifica que se han pasado suficientes argumentos
    if len(sys.argv) > 3:
        print("Usage: python booking.py <city> <room_tyepe> <start_date> <end_date>")
        sys.exit(1)
    
    if len(sys.argv) == 1:
        input_dir = 'csv'
        output_dir = 'json'
    else:
    
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] 

    files = ['listings_gz_small.csv', 'reviews_gz_small.csv', 'calendar_small.csv']
    for file in files:
        converter(file,input_dir,output_dir)
        print(f'{file} convertido a json')



if __name__ == "__main__":
    main()

