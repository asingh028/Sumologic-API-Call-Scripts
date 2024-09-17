#This is for the community support only: 

# How to use the Scripts
- Specify the API URL and Basic Authentication credentials and "limit" value in api_url/script where ever it is
- save these scripts as "py" file and run the script in IDLE or any processor you have.
- Be Sure to have python3 installed along with "requests" library. 
- These script will help formating the json data into tabular format in csv format for easy normalized visualization.

## Current CSE rules List can be exported - getcseruleslist.py
This python code will help fetching the rules enabled on your Cloud SIEM. For the rules list which you are using in cloud SIEM, there is no direct way to get the list of rules with details
Reference Doc: https://api.au.sumologic.com/docs/sec/#operation/GetRules

## All collector list from Collector Page- [AllCollectors.py](https://github.com/asingh028/Sumologic-API-Call-Scripts/blob/main/AllCollectors.py)
This python script can import the list of all collectors in the collection page with Status, type and Name to a file name "collectors_with_status"

## List the Dead Collector- using Collector Management API- Sumologic - deadCollector.py
This python script will help you find the dead Collectors in Sumo Logic.
Reference Doc: https://help.sumologic.com/docs/api/collector-management/collector-api-methods-examples/

## Delete Collectors which are dead - DeleteCollectors.py
Use cautiously as this will be a permanent delete the collectors
Reference Doc: https://help.sumologic.com/docs/api/collector-management/collector-api-methods-examples/

## Get the list of Threat intel sources with the indicators- APIthreatindicatorswithsource.py
Script to export threat intel in CSE with the sources and indicators all together- might be helpful in providing a consolidate view of your threat intel sources and indicators- Use case is if you face indicators not been malicious but still generating signals, and you want to quickly identify the source of the indicator and since no export button is there yet in Cloud SIEM UI, you have to manually drill down on the sources. The Csv file you get from this API call script will give you consolidated view and quick reference to cleanup unnecessary indicators from the sources.
Reference Doc: https://api.au.sumologic.com/docs/sec/#operation/GetAllThreatIntelIndicators
               https://api.au.sumologic.com/docs/sec/#operation/GetThreatIntelligenceSources
