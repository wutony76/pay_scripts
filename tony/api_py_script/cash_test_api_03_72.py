#!/usr/bin/python
# -*- coding: UTF-8 -*-


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
  #api_url = "http://52.79.37.229:8080/cash/add"
  #api_url = "http://52.79.37.229:8080/cash/add"
  api_url = "http://13.124.29.97:8080/cash/add"

  print("api_url", api_url)
  pid = 72
  #mWxThNaWeecfQesCLItMqlQvzvxhzHgD
  token = "mWxThNaWeecfQesCLItMqlQvzvxhzHgD"
  money = "1001.00"
#  sn = "sn%s" % int(time.time())
  sn = "sn%s" % int(time.time())
  bc_type = "2"
  bc_name = "邮政储蓄银行"
  bc_num = "621*test*4383943"
  bc_user = "test123"

  pay_type_group = 'banktocard'
  notify_url = "http://52.79.37.229:12009/callback"


  sign = make_sign(token, [
    ("pid", pid),
    ("money", money),
    ("sn", sn),
    ("bc_type", bc_type),
    ("bc_name", bc_name), 
    ("bc_num", bc_num), 
    ("bc_user", bc_user), 
    ("key", token),
  ])

  post_data = {
    "pid": pid,
    "money": money,
    "sn": sn,
    "bc_type":bc_type,
    "bc_name":bc_name,
    "bc_num":bc_num,
    "bc_user":bc_user,

    "notify_url": notify_url,
    'sign': sign,
  }

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
