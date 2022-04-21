import requests


class YelpAPI:
    def __init__(self):
        self.api_key = 'AQuSIIDGMQZ4l7SBHegjnoggcHOoh_mImR8Zatvg0a14fXNo1BK3mhKnPGK9t0wc-' \
                       '4fIZIJA7A_D6AQ-YddfqffCSpQ0Pbus-iXJeQ9x8H3ehGf49RD_sFAiM3f9YXYx'
        self.endpoint = 'https://api.yelp.com/v3/businesses/search'
        self.headers = {'Authorization': f'bearer {self.api_key}'}


class FoodRequest(YelpAPI):
    def __init__(self, food, radius, location, price):
        super().__init__()
        self.params = {
            'term': food,
            'radius': f'{int(radius) * 1650}',
            'location': location,
            'price': int(price)
        }

    def request_yelp(self):
        response = requests.get(url=self.endpoint, params=self.params, headers=self.headers)
        return response.json()

    def post_data(self):
        business_data = self.request_yelp()
        business_dict = [self.post_convert(business) for business in business_data['businesses']]
        return business_dict

    @staticmethod
    def post_convert(business):
        name = business['name']
        address = business['location']['address1']
        return {"name": name, "address": address}
