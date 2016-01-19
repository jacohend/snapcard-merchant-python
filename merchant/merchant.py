from .fiat_payout_method import FiatPayoutMethod
import json

class Merchant(object):
    id = None
    name = None
    createdAt = None
    defaultRawPayout = None
    rawPayoutSrn = None
    verified = None
    invoiceFeePercentage = None
    memberships = None
    fiatPayoutMethod = None
    totalBalances = None
    availableBalances = None

    def __init__(self, merc_dict):
        for key in merc_dict:
            try:
                if key=="fiatPayoutMethod":
                    self.fiatPayoutMethod = FiatPayoutMethod(merc_dict[key])
                else:
                    setattr(self, str(key), merc_dict[key])
            except Exception as e:
                print(e)

    def toJson(self):
        return json.dumps(self.__dict__)
