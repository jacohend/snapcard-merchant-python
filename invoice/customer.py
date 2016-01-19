import json

class Customer(object):
    street1 = None
    street2 = None
    city = None
    state = None
    postalCode = None
    country = None
    id = None
    merchantId = None
    merchantProvidedId = None
    name = None
    phoneNumber = None
    email = None

    def __init__(self, merc_dict):
        for key in merc_dict:
            try:
                setattr(self, str(key), merc_dict[key])
            except Exception as e:
                print(e)

    def toJson(self):
        return json.dumps(self.__dict__)
