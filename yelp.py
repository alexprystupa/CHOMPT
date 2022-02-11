#!/usr/bin/env python3
# yelp_class.py
"""
Making a class that has an object ready to be called upon by the API.
Has method calls that call API
"""
from typing import Dict, Union, Set, Any

import requests

class Yelp:
    def __init__(self, party_data, api_key, endpoint):
        self.party_data = party_data
        self.api_key = api_key
        self.endpoint = endpoint
        self.headers = {'Authorization': f'bearer {self.api_key}'}

    def call_api(self):

        ## GONNA HAVE TO MAKE A QUIZ WHOSE QUESTIONS IN ORDER ARE
        # 1. Food Type #2. Radius, #3. Location #4. Price
        parameters = {'term': self.party_data['Food Type?'][0],
                      'radius': str(int(self.party_data['Distance (miles)?'][0]) * 1600),
                      'location': self.party_data['Location?'][0],
                      'price': self.party_data['Price?'][0]
                      }

        # Making request to Yelp API
        response = requests.get(url=self.endpoint, params=parameters, headers=self.headers)

        return response.json()

    @staticmethod
    def print_data(business_data):
        for i, key in enumerate(business_data['businesses']):
            name = business_data['businesses'][i]['name']
            address = business_data['businesses'][i]['location']['address1']
            print(f'{name}: {address}')
