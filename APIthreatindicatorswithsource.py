import requests
import csv
import base64
import json

# Replace with your Sumo Logic access ID, access key, and environment (like 'au', 'us', etc.)
SUMO_ACCESS_ID = '<access ID>'
SUMO_ACCESS_KEY = '<access key>'
SUMO_ENVIRONMENT = 'api.us2.sumologic.com'  # Adjust for your environment- For reference- https://help.sumologic.com/docs/cse/administration/cse-apis/

# Base URLs for the APIs
sources_base_url = f"https://{SUMO_ENVIRONMENT}/api/sec/v1/threat-intel-sources"
indicators_base_url = f"https://{SUMO_ENVIRONMENT}/api/sec/v1/threat-intel-indicators"

# Encode the credentials for basic authentication
auth = base64.b64encode(f"{SUMO_ACCESS_ID}:{SUMO_ACCESS_KEY}".encode()).decode()

# Define the headers with authentication as a dictionary
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Basic {auth}'
}

# Function to get threat intel sources
def get_threat_intel_sources():
    response = requests.get(sources_base_url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {}).get('objects', [])
    else:
        print(f"Failed to retrieve sources: {response.status_code}")
        print(response.text)
        return []

# Function to get indicators for a specific source
def get_indicators_for_source(source_id):
    # Adjust parameters as needed; here, we're using a hypothetical 'sourceId' parameter
    params = {'sourceId': source_id}
    response = requests.get(indicators_base_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('data', {}).get('objects', [])
    else:
        print(f"Failed to retrieve indicators for source {source_id}: {response.status_code}")
        print(response.text)
        return []

# Fetch sources
sources = get_threat_intel_sources()

# Define the CSV file name
csv_file_name = 'threat_intel_sources_with_indicators.csv'

# Open the CSV file for writing
with open(csv_file_name, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header (column names)
    csv_writer.writerow([
        'source_id', 'source_name', 'source_description', 'source_sourceType',
        'indicator_id', 'indicator_value', 'indicator_active', 'indicator_expiration'
    ])

    # Process each source
    for source in sources:
        source_id = source.get('id', '')
        source_name = source.get('name', '')
        source_description = source.get('description', '')
        source_sourceType = source.get('sourceType', '')

        # Fetch indicators for the current source
        indicators = get_indicators_for_source(source_id)

        if indicators:
            # Write each indicator as a row in the CSV
            for indicator in indicators:
                row = [
                    source_id,
                    source_name,
                    source_description,
                    source_sourceType,
                    indicator.get('id', ''),
                    indicator.get('value', ''),
                    indicator.get('active', ''),
                    indicator.get('expiration', '')
                ]
                csv_writer.writerow(row)
        else:
            # If no indicators for the source, write a row with empty indicator fields
            row = [
                source_id,
                source_name,
                source_description,
                source_sourceType,
                '',  # indicator_id
                '',  # indicator_value
                '',  # indicator_active
                ''   # indicator_expiration
            ]
            csv_writer.writerow(row)

print(f"Threat intelligence sources with indicators exported successfully to {csv_file_name}.")
