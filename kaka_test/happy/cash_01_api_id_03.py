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


  api_url = "http://api.happypay.click/cash/add"

  print("api_url", api_url)
  pid = 3
  token = "BgxcpSGAYRYcnCpWnhKUNbdLYTyqsxTh"
  money = "500.00"
  sn = "sn%s" % int(time.time())
  #sn = "kasn%s" % int(time.time())
  #sn = "sn1623406259111"
  bc_type = "1"
  #bc_type = "bank"
  bc_name = "邮政储蓄银行"
  bc_num = "6214383943"
  bc_user = "王成功"

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
  print("sign", sign)
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
