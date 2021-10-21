# click-pass
ClickPass API
Link: https://docs.click.uz/click-pass/


```python
from click_pass import click_pass
click = click_pass(
      service_id: str, 
      otp_data: str, 
      merchant_user_id: str, 
      secret_key: str, 
      amount: 500, 
      cashbox_name: 'TEST-KASSA',
      transaction_id: 'my_order_id'
      )
print(click)
```
