def FiatPayoutMethod(object):
    id = ""
    owner = ""
    createdAt = 0
    name = ""
    defaultCurrency = ""
    disabled = False
    nameOnMethod = ""
    last4Digits = ""
    brand = None
    expirationDisplay = None
    type = ""
    linkType = ""
    supportsDeposit = False
    supportsPayment = False
    def __init__(self, payout_dict):
        for key in payout_dict:
            try:
                setattr(self, key, payout_dict[key])
            except Exception as e:
                print(e)

