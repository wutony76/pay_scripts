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

  b = hashlib.md5(a.encode("utf-8")).hexdigest()
  print("b=", b)

  return b.upper()

def main():

  api_url= "http://api.happytopays.com/balance_query"

  print("api_url",api_url)

  #DINO_02
  #pid = 3
  #token = "BgxcpSGAYRYcnCpWnhKUNbdLYTyqsxTh"
  #DINO_05
  pid = 14
  token = "SFpVbHhWVvOVuCZvggRDLIXeFxnUnZMx"
  #sn = "kasn1623333929"
  #sn = "ka-sn%s"%int(time.time())
  notify_url = "http://3.36.41.218:12009/callback"
  
  sign = make_sign(token, [
    ("pid", pid),    
    #("sn", sn), 
    ("key", token),
  ])
  print("sign", sign)
  
  post_data = {
    "pid": pid,
    #"sn": sn,  
    "notify_url": notify_url,
    'sign': sign,
  }

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)
  print('text',req.text)
  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()