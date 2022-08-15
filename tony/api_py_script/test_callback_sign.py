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

  token = "NEYnMvtiKWdsiRlNKulPyWGQLOwbpeUd"
  
  money = "300.00"
  sn = "sn%s" % int(time.time())
  pay_type_group = 'banktocard'
  notify_url = "http://52.79.37.229:12009/callback"

  sign = make_sign(token, [
    ("sn", "588476"),
    ("out_sn", "sn1636619398"),
    ("money", "300.00"),
    ("pay_type_group", "banktocard"),
    ("trade_status", "TRADE_SUCCESS"),
    ("key", "BgxcpSGAYRYcnCpWnhKUNbdLYTyqsxTh"),
  ])

  print("sign = ", sign)


  print("="*10)

  sign = make_sign(token, [
    ("pid", "117"),
    ("money", "500.00"),
    ("sn", "32WD16249476447880001"),
    ("bc_type", "bank"),
    ("bc_name", "中国农业银行,中国农业银行爱神的箭支行"),
    ("bc_num", "6214252547452145697"),
    ("bc_user", "张三疯"),
    ("key", "luVMkZmYRbTscEPpUAWcfCMOPeAvsgxo"),
  ])

  print("cash_sign = ", sign)
  

  #post_data = {
  #  "pid": pid,
  #  "money": money,
  #  "sn": sn,
  #  "notify_url": notify_url,
  #  "pay_type_group": pay_type_group,
  #  "remark": 'remark',
  #  'sign': sign,
  #}

  #req = requests.post(api_url, data=post_data)
  #a = req.content
  #print("call", req.status_code)
  #print("response", a)

  #if req.status_code == 200:
  #  print("response", a)


if __name__ == "__main__":
  main()
