# Current CSE rules List can be exported
This python code will help fetching the rules enabled on your Cloud SIEM- getcseruleslist.py

For the rules list which you are using in cloud SIEM, there is no direct way to get the list of rules with details- 

here is the end to end solution to that:

Python Script to get Rules from CSE using API- update the following - 
#Specify the API URL and Basic Authentication credentials and "limit" value in api_url if number of rules are more than 1000--> save this script as "py" file and run the script
Be Sure to have python3 installed along with "requests" library. 
This script will help formating the json data into tabular format in csv format for easy normalized visualization.

# List the Dead Collector- using Collector Management API- Sumologic - 
This python code will help you find the dead Collectors in Sumo Logic - DeadCollector.py.
https://help.sumologic.com/docs/api/collector-management/collector-api-methods-examples/

# Delete Collectors which are dead
Use cautiously as this will be a permanent delete - DeleteCollectors.py.
https://help.sumologic.com/docs/api/collector-management/collector-api-methods-examples/
