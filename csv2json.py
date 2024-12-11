import csv
import json
import sys
from pathlib import Path
import pandas as pd
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

def converter(input_dir, output_dir):
    
    listing_df = pd.read_csv(f'{input_dir}/listings_gz_small.csv')
    reviews_df = pd.read_csv(f'{input_dir}/reviews_gz_small.csv')
    calendar_df = pd.read_csv(f'{input_dir}/calendar_small.csv')
    
    listing_df["amenities"] = listing_df["amenities"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    listing_df["host_verifications"] = listing_df["host_verifications"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    
    listing_df["host"] = listing_df.apply(lambda row: { 
        "id": row["host_id"],
        "url": row["host_url"],
        "name": row["host_name"],
        "location": row["host_location"],
        "about": row["host_about"],
        "response_time": row["host_response_time"],
        "thumbail_url": row["host_thumbnail_url"],
        "picture_url": row["host_picture_url"],
        "neighbourhood": row["host_neighbourhood"],
        "response_rate": row["host_response_rate"],
        "is_superhost": row["host_is_superhost"],
        "has_profile_pic": row["host_has_profile_pic"],
        "identity_verified": row["host_identity_verified"],
        "listings_count": row["host_listings_count"],
        "total_listings_count": row["host_total_listings_count"],
        "calculated_listings_count": row["calculated_host_listings_count"],
        "calculated_listings_count_entire_homes": row["calculated_host_listings_count_entire_homes"],
        "calculated_listings_count_private_rooms": row["calculated_host_listings_count_private_rooms"],
        "calculated_listings_count_shared_rooms": row["calculated_host_listings_count_shared_rooms"],             
        "verification": row["host_verifications"]
    }, axis=1)
    
    listing_df["adress"] = listing_df.apply(lambda row: {
        
        "neighbourhood" : row["neighbourhood"],
        "neighbourhood_cleansed" : row["neighbourhood_cleansed"],
        "latitude" : row["latitude"],
        "longitude" : row["longitude"] 
    }, axis=1)
    
    listing_df["availability"] = listing_df.apply(lambda row: {
        "has_availability" : row["has_availability"],
        "availability_30" : row["availability_30"],
        "availability_60" : row["availability_60"],
        "availability_90" : row["availability_90"],
        "availability_365" : row["availability_365"] 
    }, axis=1)
    
    listing_df["reviews_info"] = listing_df.apply(lambda row: {
        "number" : row["number_of_reviews"],
        "number_ltm" : row["number_of_reviews_ltm"],
        "number_l30d" : row["number_of_reviews_l30d"],
        "first_review" : row["first_review"],
        "last_review" : row["last_review"],
        "reviews_per_month" : row["reviews_per_month"],
        "score_rating" : row["review_scores_rating"],
        "score_accuracy" : row["review_scores_accuracy"],
        "scores_cleanliness" : row["review_scores_cleanliness"],
        "scores_checkin" : row["review_scores_checkin"],
        "scores_communication" : row["review_scores_communication"],
        "scores_location" : row["review_scores_location"],
        "scores_value" : row["review_scores_value"],
           
    }, axis=1)
    
        
    
    column_names = ["host_id","host_url","host_name","host_location","host_about","host_response_time","host_thumbnail_url","host_picture_url","host_neighbourhood",
                    "host_response_rate", "host_is_superhost", "host_has_profile_pic", "host_identity_verified", "host_listings_count", "host_total_listings_count",
                    "host_verifications", "picture_url", "neighbourhood", "neighbourhood_cleansed", "latitude","longitude", "has_availability", "availability_30", 
                    "availability_60", "availability_90", "availability_365", "number_of_reviews", "number_of_reviews_ltm", "number_of_reviews_l30d", "first_review",
                    "last_review", "review_scores_rating", "review_scores_accuracy", "review_scores_cleanliness", "review_scores_checkin", "review_scores_communication",
                    "review_scores_location", "review_scores_value", "reviews_per_month","calculated_host_listings_count", "calculated_host_listings_count_entire_homes",
                    "calculated_host_listings_count_private_rooms","calculated_host_listings_count_shared_rooms" ]
    
    process_listing_df = listing_df.drop(column_names,axis=1)
    
    
    process_listing_df .to_json(f'{output_dir}/listings.json', orient='records', indent=4)
    reviews_df .to_json(f'{output_dir}/reviews.json', orient='records', indent=4)
    calendar_df.to_json(f'{output_dir}/calendar.json', orient='records', indent=4)
    
    print(f"csv en {input_dir} convertidos")   
    
    
    #print(f'{file} convertido a json')

def main():
    # Verifica que se han pasado suficientes argumentos
    if len(sys.argv) > 3:
        print("Usage: python booking.py <city> <room_tyepe> <start_date> <end_date>")
        sys.exit(1)
    
    if len(sys.argv) == 1:
        input_dir = './csv'
        output_dir = './json'
    else:
    
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] 

    converter(input_dir,output_dir)



if __name__ == "__main__":
    main()

