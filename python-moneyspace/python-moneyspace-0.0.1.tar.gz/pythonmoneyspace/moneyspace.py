import hashlib
import hmac
import requests

class MoneySpace:
    base_url = 'https://a.moneyspace.net'
    allowed_kwargs = [
        'address'
        'bankType',
        'description',
        'endTerm',
        'firstname',
        'lastname',
        'message',
        'phone',
        'startTerm',
    ]

    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    def call_api(self, path, params, optional_params={}):
        # update params
        params['secret_id'] = self.secret_id
        params['secret_key'] = self.secret_key

        # add optional parameters
        for key in optional_params:
            if key in self.allowed_kwargs:
                params[key] = optional_params[key]

        # send request to moneyspace
        r = requests.post(
            '%s%s' % (self.base_url, path),
            data=params
        )
        try:
            return r.json()
        except:
            return { 'status': 'error' }

    # check the status of a transaction using the merchant's
    # order_id as the identifier
    def check_order_id(self, order_id):
        return self.call_api('/CheckOrderID', { 'order_id': order_id })

    # check the status of a transaction using the moneyspace's
    # transaction_id as the identifier
    def check_payment(self, transaction_id):
        return self.call_api('/CheckPayment', { 'transaction_ID': transaction_id })

    # create a transaction
    def create_transaction(self, payment_type, email, amount, order_id, success_url, fail_url, cancel_url, agreement, **kwargs):
        # create params dict
        params = {
            'address': '',
            'agreement': agreement,
            'amount': '{:0.2f}'.format(amount),
            'cancel_Url': cancel_url,
            'description': '',
            'email': email,
            'fail_Url': fail_url,
            'feeType': 'include',
            'firstname': '',
            'lastname': '',
            'message': '',
            'order_id': order_id,
            'payment_type': payment_type,
            'phone': '',
            'success_Url': success_url,
        }

        # note: description is a required field for QR code payments
        # (and possibly other payment types too, let me know).
        # here i re-use the order_id as the description if no
        # description is passed in
        if payment_type == 'qrnone':
            params['description'] = kwargs.get('description', order_id)

        # call the api
        return self.call_api('/CreateTransactionID', params, kwargs)

    # validate webhooks send from moneyspace
    def webhook_validator(self, amount, status, order_id, transaction_id, hash):
        if status == 'OK':
            pre_hash = '%s%s' % (transaction_id, amount)
        else:
            pre_hash = '%s%s%s%s' % (transaction_id, amount, status, order_id)

        # compare results
        local_hash = hmac.new(self.secret_key.encode(), pre_hash.encode(), hashlib.sha256).hexdigest()
        return local_hash == hash
