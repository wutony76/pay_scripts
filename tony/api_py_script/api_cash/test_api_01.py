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
  api_url = "http://52.79.37.229:8080/cash/add"

  print("api_url", api_url)
  pid = 69
  token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
  money = "2024.00"
#  sn = "sn%s" % int(time.time())
  sn = "20210506142801466UYHU"
  bc_type = "2"
  bc_name = u"邮政储蓄银行"
  bc_num = u"621*疑似敏感信息*4383943"
  bc_user = u"潘洋平"


  pay_type_group = 'banktocard'
  notify_url = "http://www.test.com"


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
