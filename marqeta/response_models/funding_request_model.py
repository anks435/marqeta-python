from datetime import datetime

class FundingRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def order_number(self):
        if 'order_number' in self.json_response:
            return self.json_response['order_number']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def funding_source(self):
        if 'funding_source' in self.json_response:
            return self.json_response['funding_source']

    @property
    def funding_address(self):
        if 'funding_address' in self.json_response:
            return self.json_response['funding_address']

    @property
    def fundgpadetail(self):
        if 'fundgpadetail' in self.json_response:
            return self.json_response['fundgpadetail']

    @property
    def order_token(self):
        if 'order_token' in self.json_response:
            return self.json_response['order_token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']
