import json
import hmac
import time
from requests import request

class Merchant_API(object):
    def __init__(self, merchant_id, api_version, api_key, api_secret):
        self.merchant_id = merchant_id
        self.api_url = 'https://api.snapcard.io'
        self.api_version = api_version
        self.api_key = api_key
        self.api_secret = api_secret

    #authentication decorator
    def authenticate_request(func):
        def wrap(self, *args, **kwargs):
            url, method, body = func(self, *args, **kwargs)
            timestamp = int(time.time() * 1000)
            url += '?timestamp={}'.format(timestamp)
            params={}
            headers = {}
            headers['Content-Type'] = 'application/json'
            headers['X-Api-Version'] = self.api_version
            headers['X-Api-Key'] = self.api_key
            headers['X-Api-Signature'] = hmac.new(self.api_secret.encode('utf-8'), (url + body).encode('utf-8'), 'SHA256').hexdigest()
            resp = request(method=method, url=url, params=params, data=(json.dumps(body) if body != '' else None), json=None, headers=headers)
            if resp.text is not None: #snapcard will always try to give an err body
                return resp.status_code, resp.json()
            return 404, {}
        return wrap

    @authenticate_request
    def retrieve_merchant(self):
        url = self.api_url + '/merchant/{}'.format(self.merchant_id)
        method = 'GET'
        body = ''
        return url, method, body

    @authenticate_request
    def retrieve_forex(self):
        url = self.api_url + '/rates'
        method = 'GET'
        body = ''
        return url, method, body

    @authenticate_request
    def create_invoice(self, invoice):
        url = self.api_url + '/invoices'
        method = 'POST'
        body = invoice
        return url, method, body 

    @authenticate_request
    def retrieve_invoice(self, invoice_id):
        url = self.api_url + '/invoice/{}'.format(invoice_id)
        method = 'GET'
        body = ''
        return url, method, body  

    @authenticate_request
    def cancel_invoice(self, invoice_id):
        url = self.api_url + '/invoice/{}/cancel'.format(invoice_id)
        method = 'POST'
        body = ''
        return url, method, body  

    @authenticate_request
    def list_invoices(self):
        url = self.api_url + '/invoices'
        method = 'GET'
        body = ''
        return url, method, body   

    @authenticate_request
    def retrieve_payouts(self, payout_id):
        url = self.api_url + '/payout/{}'.format(payout_id)
        method = 'GET'
        body = ''
        return url, method, body   

    @authenticate_request
    def list_payouts(self):
        url = self.api_url + '/payouts'
        method = 'GET'
        body = ''
        return url, method, body   

