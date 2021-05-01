""" Collect distance matrix for place data created by poptimes_collection.py

Saves data to a csv with format [origin_id,destination_id,mode,duration_seconds,distance_meters]

Requirements:
- Get a Google Maps API Key: https://developers.google.com/maps/documentation/places/web-service/get-api-key
- To use as intended, first run poptimes_collection.py to create a popular times json file (hard-coded filename for now)
"""
import googlemaps
import json
import traceback
import csv

# You should have a file containing your reddit credentials
# This file should never be shared /or pushed to git
credentials_file = "./.secrets/credentials.json"
with open(credentials_file) as f:
    params = json.load(f)

# Create google api client
api_key = params['api_key']
client = googlemaps.Client(api_key)

# Read place data (created by poptimes_collection.py)
json_file = "uiuc.json"
with open(json_file) as f:
    place_data = json.load(f)
n_places = len(place_data)

# Create and open out csv file
csv_file = "{}_distances.csv".format(json_file.split(".")[0])
with open(csv_file, "w+") as outfile:

    csv_writer = csv.writer(outfile)
    csv_writer.writerow(['origin_id','destination_id','mode','duration_seconds','distance_meters'])

    # Function to get distance matrix data and write to csv
    # Note: modified to accept *one* origin and *one* destination. Writing to CSV with ids
    def get_dist_data(origin, dest, oid, did, mode):
        matrix_data = client.distance_matrix(origin, dest, mode=mode)
        # expecting output to have only one origin address and one destination address
        if (status := matrix_data['rows'][0]['elements'][0]['status']) != "OK":
            print("EXCEPTION ON {}->{}: {}".format(origin, dest, status))
        # Parse response and write to csv
        csv_writer.writerow([
            oid,
            did,
            mode,
            matrix_data['rows'][0]['elements'][0]['duration']['value'],
            matrix_data['rows'][0]['elements'][0]['distance']['value']
        ])

    # Progress Tracker
    print("\rProgress: 0/{}".format(n_places), end="")
    prog_tracker = 0

    # Get driving and walking distance data for each origin/dest pair 
    for place_origin in place_data:
        origin_addr = place_origin['address']
        origin_id = place_origin['id']
        for place_dest in place_data:
            if place_origin == place_dest:
                continue
            dest_addr = place_dest['address']
            dest_id = place_dest['id']
            
            """Note: 
            Constantly getting OVER_QUERY_LIMIT errors so this is sending one request 
            per pair, but according to the api limits we should be able to send 25x25?
            See: https://developers.google.com/maps/documentation/distance-matrix/usage-and-billing#other-usage-limits  
            Update: one at a time is fine because this allows writing to CSV with known place ids
            """
            get_dist_data(origin_addr, dest_addr, origin_id, dest_id, mode='driving')
            get_dist_data(origin_addr, dest_addr, origin_id, dest_id, mode='walking')
        
        prog_tracker += 1
        print("\rCompleted: {}/{}".format(prog_tracker, n_places), end="")

print ("\r\nDone.")


