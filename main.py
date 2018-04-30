import urllib.parse
import requests
import json
from pprint import pprint

# Set the keys required to access the Discogs api
consumer_key = "uTweskQdRQLFmQcACKVo"
secret_key = "qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO" 

# Define the discogs api
main_api = 'https://api.discogs.com/database/search?q=SEARCHTERM&key=CONSUMERKEY&secret=SECRETKEY'

#Read in our file containing information about our Foobar library
data = json.load(open('test.json'))

data["meta"]["ALBUM"]

# Pretty print our data
pprint(data)

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