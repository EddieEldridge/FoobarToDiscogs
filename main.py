import urllib.parse
import requests

# Set the keys required to access the Discogs api
consumer_key = "uTweskQdRQLFmQcACKVo"
secret_key = "qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO" 

# Define the discogs api
main_api = 'https://api.discogs.com/database/search?q=SEARCHTERM&key=CONSUMERKEY&secret=SECRETKEY'

# User Input for their search term
searchTerm = input("Search: " )

# Construct our URL with keys and search term
url = main_api.replace("SEARCHTERM", searchTerm)
url = url.replace("CONSUMERKEY", consumer_key)
url = url.replace("SECRETKEY", secret_key)

# Print the request url
print ('Requesting: ', url)

#
json_data = requests.get(url).json()
print(json_data)