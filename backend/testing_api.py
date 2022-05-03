import requests

import call_yelp_api

test = call_yelp_api.FoodRequest("Chinese", "1", "40.758896", "-73.985130", "1")

print(test.post_data())

