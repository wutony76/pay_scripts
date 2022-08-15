#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import time
import hashlib
import requests
import json


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

  #api_url = "https://www.golden-gac.com/MT4_IIS/banker/getinit"
  api_url = "https://www.golden-gac.com/MT4_IIS/banker/user_meta"

  post_data = {
    #"version": 136,
    #"account": 12583079,
    "account": 12583134,
    #"password": "ry52514j",
    #"login":12583079,
    #"groupname":"demoforex",
    #"device":"Model: Veriton M6620G (Acer),　Name: DESKTOP-RPRFHR1,　Type: Desktop　",
  }

  req = requests.post(api_url, data=json.dumps(post_data))
  a = req.content
  print("call", req.status_code)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()


