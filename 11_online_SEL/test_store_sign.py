from __future__ import print_function
import time
import hashlib
from collections import OrderedDict
import requests

import json
import random



def make_sign(token, key_values):

  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))

  a = '&'.join(args)
  print("a=", a)

  b = hashlib.md5(a.encode("utf-8")).hexdigest()
  print("b=", b)

  return b.upper()


def main():

  #api_url = "http://3.35.119.172:9410/pay"
  api_url = "http://54.180.135.144:8080/pay"

  print("api_url", api_url)
  pid = 18
  token = "cShoOVTfkZYuzjxIIsyZmnWdqJutUSLB"
  money = "1000.00"
  sn = "sn%s" % int(time.time())
  sn = "TLJPAY20220519194836860117"

  pay_type_group = 'banktocard_payname'
  notify_url = "http://127.0.01:8087/api/yiranpay/channelpay/tljpay/notify/TLJPAY10001"
  print("notify_url ", notify_url)


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

  #req = requests.post(api_url, data=post_data)
  #a = req.content
  #print("call", req.status_code)

  #if req.status_code == 200:
  #  print("response", a)
  #  a_json = json.loads(a)

  #  print("code", a_json["code"])

  #  msg = a_json["msg"]
  #  print("msg", msg)

  #  if a_json["code"] == 1:
  #    data = a_json["data"]
  #    bank_url = data["code_url"]
  #    print("bank_url", bank_url)


if __name__ == "__main__":
  main()
