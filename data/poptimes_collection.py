""" Collect popular times data using lat/long coordinates (hard-coded for now).

Requirements:
- Get a Google Maps API Key: https://developers.google.com/maps/documentation/places/web-service/get-api-key
- Download and install the populartimes library: https://github.com/m-wrzr/populartimes
"""
import populartimes
import json

# You should have a file containing your reddit credentials
# This file should never be shared /or pushed to git
credentials_file = "../.secrets/credentials.json"
with open(credentials_file) as f:
    params = json.load(f)

# supported types: https://developers.google.com/maps/documentation/places/web-service/supported_types
types = ['restaurant', 'tourist_attraction', 'point_of_interest']

# manually get coordinates: https://www.latlong.net/
# lat/long coords roughly capturing UIUC campus:
# p1 = (40.090746, -88.240796)
# p2 = (40.116185, -88.219672)
# lat/long coords roughly capturing Chicago:
p1 = (41.829665, -87.674125)
p2 = (41.923483, -87.578274)

# include/exclude places without populartimes
include_all = False

response = populartimes.get(api_key, types, p1, p2, all_places=include_all)
print(len(response))

with open ('out.json', 'w+') as f:
    json.dump(response, f, indent=2)
