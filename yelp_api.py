#!/usr/bin/env python3
# yelp_api.py

import requests
#import pandas as pd

#Yelp API Key
API_KEY = 'AQuSIIDGMQZ4l7SBHegjnoggcHOoh_mImR8Zatvg0a14fXNo1BK3mhKnPGK9t0wc-' \
          '4fIZIJA7A_D6AQ-YddfqffCSpQ0Pbus-iXJeQ9x8H3ehGf49RD_sFAiM3f9YXYx'

ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': f'bearer {API_KEY}'}

# Define parameters
def main():

    # User inputs
    food = input('What food do you want: ')
    distance = int(input('How far are you willing to go (miles): '))
    city = input('What city are you in: ')
    price = input('What price range are you looking for? (1-4): ')

    # Query Parameters
    PARAMETERS = {'term': food,
                  'radius': f'{distance * 1600}',
                  'location': city,
                  'price': price
                  }

    # Making request to Yelp API
    response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
    business_data = response.json()

    #print(business_data)
    for i, key in enumerate(business_data['businesses']):
        name = business_data['businesses'][i]['name']
        address = business_data['businesses'][i]['location']['address1']
        print(f'{name}: {address}')

    #print(business_data)

if __name__ == '__main__':
    main()