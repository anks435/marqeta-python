from datetime import datetime, date
from marqeta.response_models.shipping_information_response import ShippingInformationResponse
from marqeta.response_models.card_personalization import CardPersonalization
from marqeta.response_models import datetime_object
import json
import re

class CardFulfillmentResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def shipping(self):
        if 'shipping' in self.json_response:
            return ShippingInformationResponse(self.json_response['shipping'])

    @property
    def card_personalization(self):
        if 'card_personalization' in self.json_response:
            return CardPersonalization(self.json_response['card_personalization'])

    def __repr__(self):
         return '<Marqeta.response_models.card_fulfillment_response.CardFulfillmentResponse>' + self.__str__()
