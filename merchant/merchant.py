from fiat_payout_method import FiatPayoutMethod

def Merchant(object):
    id = ""
    name = ""
    createdAt = 0
    defaultRawPayout = 0
    rawPayoutSrn = ""
    verified = False
    invoiceFeePercentage = 0.0
    memberships = []
    fiatPayoutMethod = None
    totalBalances = {}
    availableBalances = {} 

    def __init__(self, merc_dict):
        for key in merc_dict:
            try:
                if key=="fiatPayoutMethod":
                    self.fiatPayoutMethod = FiatPayoutMethod(merc_dict[key])
                setattr(self, key, merc_dict[key])
            except Exception as e:
                print(e)
    

