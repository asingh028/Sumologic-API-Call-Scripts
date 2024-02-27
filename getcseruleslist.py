import json
import csv
import requests
from requests.auth import HTTPBasicAuth

def flatten_json(json_obj, parent_key='', sep='_'):
    flat_dict = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_json(value, new_key, sep=sep))
        else:
            flat_dict[new_key] = value
    return flat_dict

def flatten_nested_json(json_data):
    flattened_data = []
    for obj in json_data:
        flattened_data.append(flatten_json(obj))
    return flattened_data

# Specify the API URL and Basic Authentication credentials- url used here is for Mumbai deployment
api_url = 'https://api.in.sumologic.com/api/sec/v1/rules?limit=1000'
username = 'accessid'
password = 'Accesskey'

# Make API request to download JSON data with Basic Authentication
response = requests.get(api_url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Flatten each JSON object in the list
    flat_data = flatten_nested_json(data['data']['objects'])

    # Extract column headers from the flattened dictionary
    headers = set(key for obj in flat_data for key in obj.keys())

    # Write data to CSV file
    csv_file_path = 'rulescsenew.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(flat_data)

    print(f"CSV file '{csv_file_path}' created successfully.")
else:
    print(f"Error making API request. Status code: {response.status_code}")
