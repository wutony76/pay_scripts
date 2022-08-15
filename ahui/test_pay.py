from __future__ import print_function
import sys
import time
import hashlib
import random
from collections import OrderedDict
import requests


def make_sign(token, key_values):

  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))

  a = '&'.join(args)
  print("a=", a)

  b = hashlib.md5(a.encode()).hexdigest()
  print("b=", b)

  return b.upper()


def main():
  argv = list(sys.argv)
  argv.pop(0)

  gen_count = 1
  if len(argv) > 0:
    gen_count = int(argv[0])

  api_url = "http://api.happytopays.com/pay"

  for i in range(gen_count):
  
    pid = 11 
    #token = "zWAgFTAtzpUfrWOMwKIjwNVaVBNlQOHL"
    token = "KUieywMacaDsGBBnWtuncskSvDmRZgyJ"
    money = "1000.00"
    sn = "%s" % int(time.time()*10000.0)
    pay_type_group = 'banktocard'
    notify_url = "http://13.125.212.29:13001/callback"

    print("api_url", api_url, 'out_sn', sn)

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
      "remark": 'none',
      #'sign': "iabc",
      'sign': sign,
    }

    req = requests.post(api_url, data=post_data)
    a = req.content
    print("call", req.status_code)
    if req.status_code == 200:
      print("response", a)



if __name__ == "__main__":
  main()
