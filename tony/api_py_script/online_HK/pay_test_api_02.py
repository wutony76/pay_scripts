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
  
  api_url = "http://api.dtoys.click/pay"
  


  print("api_url", api_url)
  #pid = 77
  #token = "rEGRwgxQuxOtgAxSwvKYWICmramjQpbN"
  pid = 98 
  token = "NEYnMvtiKWdsiRlNKulPyWGQLOwbpeUd"
  
  money = "300.00"
  sn = "sn%s" % int(time.time())
  pay_type_group = 'banktocard'
  notify_url = "http://52.79.37.229:1009/callback"

  sign = make_sign(token, [
    ("pid", pid),
    ("money", money),
    ("sn", sn),
    ("pay_type_group", pay_type_group),
    ("notify_url", notify_url), 
    ("key", token),
  ])

  post_data = {
    "pid": pid,
    "money": money,
    "sn": sn,
    "notify_url": notify_url,
    "pay_type_group": pay_type_group,
    "remark": 'remark',
    'sign': sign,
  }

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)
  print("response", a)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
