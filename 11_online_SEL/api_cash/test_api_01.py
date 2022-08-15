from __future__ import print_function
import time
import hashlib
from collections import OrderedDict
import random
import requests
import json


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
  api_url = "http://54.180.135.144:8080/cash/add"

  print("api_url", api_url)
  #pid = 69
  pid = 3 
  #token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
  token = "BgxcpSGAYRYcnCpWnhKUNbdLYTyqsxTh"
  money = str(random.randrange(2000))
  
  
  money = "2039.3333331"
#  sn = "sn%s" % int(time.time())
  _random = random.randrange(9999999)
  #print("_random", _random)
  sn = "20210506142801466UYHU"+str(_random)
  bc_type = "2"
  bc_name = u"ttt邮政储蓄银行"
  bc_num = u"ttt621*疑似敏感信息*4383943"
  bc_user = u"ttt"


  pay_type_group = 'banktocard'
  notify_url = "http://3.35.172.98:13001"
  print("notify_url ", notify_url)


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
    a_json = json.loads(a)

    print("code", a_json["code"])

    msg = a_json["msg"]
    print("msg", msg)

    
    


if __name__ == "__main__":
  main()
