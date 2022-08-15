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

  b = hashlib.md5(a).hexdigest()
  print("b=", b)

  return b.upper()


def main():
  argv = list(sys.argv)
  argv.pop(0)

  gen_count = 1
  if len(argv) > 0:
    gen_count = int(argv[0])

  for i in xrange(gen_count):
    main_call()

def main_call():

  #api_url = "http://3.35.119.172:9410/pay"
  #api_url = "http://52.79.37.229:8080/cash/add"
  api_url = "http://3.35.119.172:9410/cash/add"
  #api_url = "http://api.dipay.cc/cash/add"

  print("api_url", api_url)
  pid = 69
  token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
  money = "1001.00"
#  sn = "sn%s" % int(time.time())

  ts = int(time.time() * 10000.0)

  sn = "sn-%016x-%03x" % (ts, random.randint(0, 4095))
  bc_type = "2"
  bc_name = "邮政储蓄银行"
  bc_num = "621*疑似敏感信息*4383943"
  bc_user = "潘洋平"


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
  elif req.status_code == 500:
    print('req', req.content)


if __name__ == "__main__":
  main()


