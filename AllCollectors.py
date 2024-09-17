import requests
import csv

# Replace these with your Sumo Logic access ID and access key
access_id = 'Accessid'
access_key = 'accesskey'

# Sumo Logic API endpoint for collectors
url = 'https://api.us2.sumologic.com/api/v1/collectors'

# Set initial offset and limit values
offset = 0
limit = 100  # Maximum number of collectors to fetch per request
all_collectors = []

# Loop through all collectors, handling pagination
while True:
    # Prepare API request with offset and limit parameters
    response = requests.get(
        url,
        params={'offset': offset, 'limit': limit},
        auth=(access_id, access_key),
        headers={'Content-Type': 'application/json'}
    )

    # Check if the request was successful
    if response.status_code == 200:
        collectors = response.json().get('collectors', [])
        
        # Append the current batch of collectors to the list
        all_collectors.extend(collectors)
        
        # If the number of collectors returned is less than the limit, we've retrieved all collectors
        if len(collectors) < limit:
            break
        
        # Update the offset to fetch the next batch of collectors
        offset += limit
    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Create a list of simplified collector information with health status
collector_data = []

for collector in all_collectors:
    # Extract relevant information
    collector_info = {
        'ID': collector.get('id'),
        'Name': collector.get('name'),
        'Type': collector.get('collectorType'),
        'Category': collector.get('category'),
        'Status': 'Healthy' if collector.get('alive') else 'Unhealthy',
        'Source Sync Mode': collector.get('sourceSyncMode'),
        'Last Seen Alive': collector.get('lastSeenAliveTime')
    }
    collector_data.append(collector_info)

# Define CSV file path
csv_file = 'collectors_with_status.csv'

# Write the data to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=collector_data[0].keys())
    
    # Write header
    writer.writeheader()
    
    # Write collector data
    writer.writerows(collector_data)

# Output confirmation
print(f"Collector data saved to {csv_file}")