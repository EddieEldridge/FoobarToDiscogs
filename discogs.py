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


output_file = 'output.json'

# Create the client
doClient = discogs_client.Client('FoobarToDiscogs/0.1', consumer_key='uTweskQdRQLFmQcACKVo',consumer_secret='qyprAKEvdbRJAuFzPPdRbyELDPcYgyQO')

def addToWantList(albumList, currentUser):
    artistID = []
    unAddedAlbums = []
    addedAlbumsCount = 0
    unAddedAlbumsCount= 0

    for i in range(len(albumList)):
        albumName = str(albumList[i])
        result = doClient.search(albumName, type='release')
        if(len(result)==0):
            print("No results found for: " + albumName)
            unAddedAlbums.append(albumList[i])
            unAddedAlbumsCount += 1

        else:
            album = result[0]
            print("Adding: " + album.title)
            time.sleep(1.2)
            try:
                currentUser.wantlist.add(album.id)
                addedAlbumsCount += 1
            except:
                print("HTTPError: 502: The Discogs API is undergoing maintenance. This is beyond my control.")
    
    print("Added albums: " + str(addedAlbumsCount))
    print("Skipped albums: " + str(unAddedAlbumsCount))

    print("=== SKIPPED ALBUMS ===")
    pprint(unAddedAlbums)

def discogsAuth():
    authStuff = doClient.get_authorize_url()

    # Process auth details
    request_token = authStuff[0]
    request_secret = authStuff[1]
    authorizationURL = authStuff[2]

    # Open the auth url in a browser
    webbrowser.open_new_tab(authorizationURL)

    # Prompt the user for their authentication key
    authKey = input("Please enter the key shown by Discogs: ")

    # Get an access token using the authentication key
    doClient.get_access_token(authKey)

    # Set currentUser to be the user that just authenticated
    currentUser = doClient.identity()

    return currentUser

def readJSON():
    # Define file location  
    json_file = input("Please enter the name of the generated JSON File (eg. lib.json): ")

    # Setup our json file to be read, encoding it as UTF 8, and giving it a variable name of 'file'
    with open(json_file, 'r', encoding='UTF-8') as file:
        
        # Unique list of albums
        albumList = []

        # Load the opened json file in as an Ordered Dictionary
        json_dictionary = json.load(file)
        
    # For loop to iterate through our information
        for element in json_dictionary:
            if element['meta']['album'] not in albumList:
                albumName = element['meta']['album']
                albumList.append(albumName)
        
    for i in range(len(albumList)):
        print("Album " + str(i) + ": " + str(albumList[i]))

    print("File loaded successfully!")
    print("Albums found: " + str(len(albumList)))

    shouldContinue = input("Continue? (y/n): ")
    if(shouldContinue=='y'):
        currentUser = discogsAuth()
        addToWantList(albumList, currentUser)
    else:
        print("Exiting...")
        exit

readJSON()


        
