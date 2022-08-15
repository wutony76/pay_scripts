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

  api_url= "http://54.199.80.255:8080/balance_query"

  print("api_url",api_url)



  pid = 93
  token = "zWAgFTAtzpUfrWOMwKIjwNVaVBNlQOHL"
  #sn = "kasn1623333929"
  #sn = "ka-sn%s"%int(time.time())
  notify_url = "http://52.79.37.229:12009/callback"
  
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

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()