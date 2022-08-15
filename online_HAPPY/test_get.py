#!/usr/bin/python
# -*- coding: UTF-8 -*-


from __future__ import print_function
import time
import hashlib
from collections import OrderedDict
import requests




def main():
  api_url = "http://callback.mi-rich.com/api/v1/deposit/tuolajipay"
  req = requests.post(api_url, data=post_data)
  print("req", req)


  a = req.content
  print("call", req.status_code)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
