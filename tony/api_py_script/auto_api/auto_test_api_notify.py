from __future__ import print_function
import time
import hashlib
from collections import OrderedDict
import requests


def make_sign(values):
  #a = ''.join(key_values)

  str_v = ""
  for v in values:
    str_v += str(v)


  #args = []
  #for k, v in key_values:
  #  args.append('%s=%s' % (k, v))

  #a = '&'.join(args)
  #print("a=", a)

  b = hashlib.md5(str_v).hexdigest()
  print("b=", b)

  #return b.upper()
  return b



def main():
#  api_url = "http://3.35.119.172:9410/pay"
  #api_url = "http://52.79.37.229:8080/gongxi/notify"
  api_url = "http://13.124.29.97:8080/gongxi/notify"
  card = 8168 
  amount = "300.71"
  #is_super = "jat*#0264857*#1"
  secret = "TESTTESTTEST"
  sign = make_sign([secret,amount, card, "UfZktxDKCqkDgZJLjsnPPKizQmKowbok"])

  get_data = {
    "amount": amount,
    "card": card,
    "secret":secret,
    "sign":sign,
  #  "is_super" : is_super,
  }

  req = requests.get(api_url, params = get_data)
  a = req.content
  print("call", req.status_code)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
