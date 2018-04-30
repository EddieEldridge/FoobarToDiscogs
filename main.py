import urllib.parse
import requests
import json
from pprint import pprint

# Set the keys required to access the Discogs api
consumer_key = "uTweskQdRQLFmQcACKVo"
secret_key = "qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO" 

# Define the discogs api
main_api = 'https://api.discogs.com/database/search?q=SEARCHTERM&key=CONSUMERKEY&secret=SECRETKEY'


# Setup our json file to be read in
json_file = open('lib.json',  encoding='UTF-8')

# Assign the content of our json file to a variable called 'library_data'
library_data = json.load(json_file)

# Define the length of our array as
array_length = len(library_data)

for i in range(array_length):
    pathTitle=library_data[i]['meta']
    pprint(pathTitle)
    print()

# Pretty print our data

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