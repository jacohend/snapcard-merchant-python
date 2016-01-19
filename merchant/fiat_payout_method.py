import json

def FiatPayoutMethod(object):
    id = None
    owner = None
    createdAt = None
    name = None
    defaultCurrency = None
    disabled = None
    nameOnMethod = None
    last4Digits = None
    brand = None
    expirationDisplay = None
    type = None
    linkType = None
    supportsDeposit = None
    supportsPayment = None

    def __init__(self, payout_dict):
        for key in payout_dict:
            try:
                setattr(self, str(key), payout_dict[key])
            except Exception as e:
                print(e)

    def toJson(self):
        return json.dumps(self.__dict__)



