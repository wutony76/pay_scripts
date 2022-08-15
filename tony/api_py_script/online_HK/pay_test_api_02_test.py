from __future__ import print_function
import time
import hashlib
from collections import OrderedDict
import requests


def make_sign(token, key_values):

  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))

  a = '&'.join(args)
  print("a=", a)

  b = hashlib.md5(a).hexdigest()
  print("b=", b)

  return b.upper()


def main():

  #api_url = "http://3.35.119.172:9410/pay"
  #api_url = "http://52.79.37.229:8080/pay"
  #api_url = "http://16.162.65.51:8080/pay"
  api_url = "http://18.166.235.5:8080/pay"
  


  print("api_url", api_url)
  pid = 77
  token = "rEGRwgxQuxOtgAxSwvKYWICmramjQpbN"
  money = "300.00"
  sn = "sn%s" % int(time.time())
  #pay_type_group = 'banktocard'
  pay_type_group = 'banktocard_payname'
  notify_url = "http://52.79.37.229:12009/callback"

  sign = make_sign(token, [
    ("pid", pid),
    ("money", money),
    ("sn", sn),
    ("pay_type_group", pay_type_group),
    ("notify_url", notify_url), 
    ("key", token),
  ])

  post_data = {
    "pid": 101,
    "money": "1000.00",
    "sn": "MP_05311709117rK0vt",
    "notify_url": "https://api.maxpay888.com/moneyin_async_notify/dipay",
    "pay_type_group": "banktocard_payname",
    "remark": "test",
    'sign': "DE3113D89F8F5F49E56967D1F08D9E7D",
  }

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)
  print("response", a)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
