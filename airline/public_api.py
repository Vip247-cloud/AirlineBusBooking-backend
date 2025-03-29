import requests
import os

# AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")  # Add this to your .env

def get_flights(origin=None, destination=None):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        # "access_key": AVIATIONSTACK_API_KEY,
        "access_key": 'e16e5ada0efccdd2dcc2a6f0edd720b9',
        "dep_iata": origin,
        "arr_iata": destination,
        "limit": 5
    }
    response = requests.get(url, params=params)
    return response.json()
