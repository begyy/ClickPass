import requests
from datetime import datetime
import hashlib


def click_pass(
        service_id: str,
        otp_data: str,
        merchant_user_id: str,
        secret_key: str,
        amount: int,
        cashbox_name: str,
        transaction_id: str
):
    """
    :DOCUMENTATION URL : https://docs.click.uz/click-pass/
    :param service_id: 12345678
    :param otp_data: 12345678
    :param merchant_user_id: 123455678
    :param secret_key: qwerty
    :return: {}
    """
    payment_url = 'https://api.click.uz/v2/merchant/click_pass/payment'

    now_timestamp = int(round(datetime.utcnow().timestamp()))
    digest = hashlib.sha1(f'{now_timestamp}{secret_key}'.encode())
    digest = digest.hexdigest()

    token = f'{merchant_user_id}:{digest}:{now_timestamp}'
    headers = {'Auth': token, 'Accept': 'application/json'}

    data = {
        'service_id': service_id,
        'otp_data': otp_data,
        'amount': amount,
        'cashbox_code': cashbox_name,
        'transaction_id': transaction_id
    }

    r = requests.post(payment_url, json=data, headers=headers)
    return r.json()
