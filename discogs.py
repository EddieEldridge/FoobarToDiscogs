import urllib.parse
import requests
import json
from pprint import pprint
from collections import OrderedDict
import discogs_client
import webbrowser
import time

# Set the keys required to access the Discogs api
consumer_key = "uTweskQdRQLFmQcACKVo"
secret_key = "qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO" 

# Define file location
json_file = 'lib.json'
output_file = 'output.json'

# Create the client
doClient = discogs_client.Client('FoobarToDiscogs/0.1', consumer_key='uTweskQdRQLFmQcACKVo',consumer_secret='qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO')
authStuff = doClient.get_authorize_url()

# Process auth details
request_token = authStuff[0]
request_secret = authStuff[1]
authorizationURL = authStuff[2]

# Open the auth url in a browser
webbrowser.open_new_tab(authorizationURL)

authKey = input("Please enter the key shown by Discogs: ")
doClient.get_access_token(authKey)

currentUser = doClient.identity()

# Setup our json file to be read, encoding it as UTF 8, and giving it a variable name of 'file'
with open(json_file, 'r', encoding='UTF-8') as file:
    
    # Unique list
    albumList = []

    # Load the opened json file in as an Ordered Dictionary
    json_dictionary = json.load(file)
    
   # For loop to iterate through our information
    for element in json_dictionary:
            #pprint(element['meta']['album'])

            if element['meta']['album'] not in albumList:
               albumList.append(element['meta']['album'])
    
#pprint(unique_list)
currentUser.wantlist.add(doClient.release(5))
artistID = []

for i in range(len(albumList)):
    albumListElement = albumList[i]
    albumElementString = str(albumListElement)
    result = doClient.search(albumElementString, type='release')
    if(len(result)==0):
        print("No results found for: " + albumElementString)
    else:
        album = result[0]
        print("Your album: " + albumElementString)
        print("Album found: " + album.title)
        userInput = input("Add this album to wantlist? (y/n):  ")
        if(userInput=='y'):
             currentUser.wantlist.add(album.id)
        else:
            continue

        

