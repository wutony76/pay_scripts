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



def callback( test_url):
  #api_url = "http://3.35.119.172:9410/pay"
  #api_url = "http://52.79.37.229:8080/pay"
  post_data = {
    #"pid": pid,
    #"money": money,
    #"sn": sn,
    #"notify_url": notify_url,
    #"pay_type_group": pay_type_group,
    #"remark": 'remark',
    #'sign': sign,
  }
  headers = {'content-type':'application/json; utf-8'}
  #  rep = requests.post( url, headers = headers , data = json.dumps(params) )
  req = requests.post(test_url, headers = headers, data=post_data)
  a = req.content
  print("*" * 100)
  print("call", req.status_code)
  print("response", a)

def main():
  callback("http://syo.vgs999.net")
  callback("http://www.test.com")
  


if __name__ == "__main__":
  main()
