from datetime import datetime
from marqeta.response_models.card_product_config import CardProductConfig

class CardProductResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
            return datetime.strptime(self.json_response['start_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return datetime.strptime(self.json_response['end_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def config(self):
        if 'config' in self.json_response:
            return CardProductConfig(self.json_response['config'])

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')
