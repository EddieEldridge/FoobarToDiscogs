import urllib.parse
import requests
import json
from pprint import pprint
from collections import OrderedDict

# Set the keys required to access the Discogs api
consumer_key = "uTweskQdRQLFmQcACKVo"
secret_key = "qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO" 

# Define the discogs api
main_api = 'https://api.discogs.com/database/search?q=SEARCHTERM&key=CONSUMERKEY&secret=SECRETKEY'

# Define file location
json_file = 'lib.json'
output_file = 'output.json'


# Setup our json file to be read, encoding it as UTF 8, and giving it a variable name of 'file'
with open(json_file, 'r', encoding='UTF-8') as file:
    
    # Unique list
    unique_list = []

    # Load the opened json file in as an Ordered Dictionary
    json_dictionary = json.load(file)
    
   # For loop to iterate through our information
    for element in json_dictionary:
            #pprint(element['meta']['album'])

            if element['meta']['album'] not in unique_list:
               unique_list.append(element['meta']['album'])
    
pprint(unique_list)



# User Input for their search term
#searchTerm = input("Search: " )

# Construct our URL with keys and search term
#url = main_api.replace("SEARCHTERM", searchTerm)
#url = url.replace("CONSUMERKEY", consumer_key)
#url = url.replace("SECRETKEY", secret_key)

# Print the request url
#print ('Requesting: ', url)

# Print our requested data
#requested_data = requests.get(url).json()
#print(requested_data)