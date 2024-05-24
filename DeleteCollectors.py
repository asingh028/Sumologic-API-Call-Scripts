import csv
import requests

# Define the Sumo Logic API endpoint and access credentials
api_url = "https://api.sumologic.com/api/v1/collectors"
access_id = "YOUR_ACCESS_ID"
access_key = "YOUR_ACCESS_KEY"

# Function to get all collectors
def get_collectors():
    response = requests.get(api_url, auth=(access_id, access_key))
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

# Function to filter dead collectors
def filter_dead_collectors(collectors):
    dead_collectors = []
    for collector in collectors["collectors"]:
        if not collector["alive"]:
            dead_collectors.append(collector)
    return dead_collectors

# Function to delete a collector
def delete_collector(collector_id):
    delete_url = f"{api_url}/{collector_id}"
    response = requests.delete(delete_url, auth=(access_id, access_key))
    response.raise_for_status()  # Raise an exception for HTTP errors

# Fetch all collectors
collectors = get_collectors()

# Filter dead collectors
dead_collectors = filter_dead_collectors(collectors)

# Write dead collectors to a CSV file and delete them
with open("dead_collectors.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Collector ID", "Collector Name", "Category", "TimeZone", "Alive", "Collector Type"])
    for collector in dead_collectors:
        writer.writerow([
            collector["id"],
            collector["name"],
            collector.get("category", "N/A"),  # Provide default value if key is missing
            collector.get("timeZone", "N/A"),  # Provide default value if key is missing
            collector["alive"],
            collector["collectorType"]
        ])
        delete_collector(collector["id"])

print("CSV file 'dead_collectors.csv' created and dead collectors deleted successfully.")