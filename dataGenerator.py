import random
import matplotlib.pyplot as plt
import requests
import json

API_KEY = "AIzaSyBwtm2VHMGqeY4v9vbbTnMfN_vrR5yEfes"

import requests
query = "farm"
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+API_KEY

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)['results']

with open('data.json', 'w') as f:
    json.dump(response, f)

print(response.text)
