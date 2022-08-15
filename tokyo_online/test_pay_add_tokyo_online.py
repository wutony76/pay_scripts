from __future__ import print_function
import sys
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
  #print("a=", a)

  b = hashlib.md5(a).hexdigest()
  #print("b=", b)

  return b.upper()


def main():

  print("=" *100)

  argv = list(sys.argv)
  argv.pop(0)

  gen_count = 1

  if len(argv) > 0:
    gen_count = int(argv[0])


  pay_add_url = "http://54.199.80.255:8080/pay"

  sn_seq = 0

  print("api_url", pay_add_url)

  for j in xrange(gen_count):

    now = datetime.now()

    sn_seq = (sn_seq + 1) % 0xffff

    pid = 98
    token = "ehCMZ1NTYwK87pUntFrVAEPByos9kmHG"
    #money = random.randint(501, 900)
    money = round(random.uniform(300, 20000), 2)
    #money = round(600, 2)
    _t0 = now.strftime('%Y%m%d')
    _t1 = int(now.strftime('%H%M%S'))
    
    #debug
    #_t1 = (_t1 // 2) * 2
    #sn_seq = 0;

    sn = "sn-%s-%s%s" % (_t0, _t1, str(sn_seq).zfill(5))
    pay_type_group = 'banktocard'
    #notify_url = "http://3.35.119.172:9414/mypay_callback"
    notify_url = "http://54.95.200.135:12009/callback"
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
    #print("post_data", post_data)
    print('out_sn', sn)

    t0 = time.time()
    req = requests.post(pay_add_url, data=post_data)
    a = req.content
    dt = time.time() - t0
    print("call", dt, req.status_code)
    print("response", a)
    #if req.status_code == 200:
    #  print("response", a)





if __name__ == "__main__":
  main()
