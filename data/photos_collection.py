""" Collect photos for place data created by poptimes_collection.py

Requirements:
- Get a Google Maps API Key: https://developers.google.com/maps/documentation/places/web-service/get-api-key
- To use as intended, first run poptimes_collection.py to create a popular times json file (hard-coded filename for now)
"""
import googlemaps
import json
import traceback
import os

# You should have a file containing your reddit credentials
# This file should never be shared /or pushed to git
credentials_file = "./.secrets/credentials.json"
with open(credentials_file) as f:
    params = json.load(f)

# Create google api client
api_key = params['api_key']
client = googlemaps.Client(api_key)

# Read place data (created by poptimes_collection.py)
json_file = "chicago_clean.json"
with open(json_file) as f:
    place_data = json.load(f)

# Create image out directory
img_directory = json_file.split(".")[0]
if not os.path.exists(img_directory):
    os.makedirs(img_directory)

for place in place_data:

    place_id = place["id"]
    # TODO: how to pick filetype ??
    img_outfile = "{}/{}.jpg".format(img_directory, place_id)

    try:
        # Make a Place Details request to get photo reference
        response = client.place(place_id, fields=["photo"])
        photo_ref = response["result"]["photos"][0]["photo_reference"]

        # Make a Place Photos request and save actual photo
        with open(img_outfile, 'w+b') as of:
            for chunk in client.places_photo(photo_ref, max_height=200):
                if chunk:
                    of.write(chunk)

    except KeyboardInterrupt:
        quit()

    except:
        print("EXCEPTION ON", place_id)
        # TODO: get actual exception. currently written as a catch-all 
        continue
