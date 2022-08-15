from __future__ import print_function
import time
from datetime import datetime
import random
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

  print("=" *100)


  site_prefix = "http://13.124.29.97:9413"
  pay_add_url = "http://13.124.29.97:8080/pay"

  sn_seq = 0

  for j in xrange(1):

    now = datetime.now()

    sn_seq = (sn_seq + 1) % 0xffff

    print("api_url", pay_add_url)
    pid = 69
    token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
    #money = random.randint(501, 900)
    money = round(random.uniform(300, 900), 2)
    #money = round(600, 2)
    sn = "sn-%s%s" % (now.strftime('%Y%m%d-%H%M%S'), str(sn_seq).zfill(5))
    pay_type_group = 'banktocard'
    #notify_url = "http://3.35.119.172:9414/mypay_callback"
    notify_url = "http://3.35.119.172:12009/callback"
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
    print("post_data", post_data)

    req = requests.post(pay_add_url, data=post_data)
    a = req.content
    print("call", req.status_code)
    print("response", a)
    #if req.status_code == 200:
    #  print("response", a)





if __name__ == "__main__":
  main()
