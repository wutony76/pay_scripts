#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import time
import hashlib
from collections import OrderedDict
import requests

import threading
import Queue

import random
import json


def work(num):
  print("Thread ---------", num)

  que = Queue.Queue()
  #loop_delay = 1 / 8.0
  loop_delay = 3 
  while True:
    try:
      que.get(timeout=loop_delay)
    except Queue.Empty:
      pass
    
    #total_coin = post_api(num, total_coin)
    post_api(num)

def main():
  #total_coin = 300000
  threads =[]
  for i in range(4):
    threads.append(threading.Thread(target = work, args = (i,) ))
    threads[i].start()

  #for i in range(3):
  #  threads[i].join()
  #print("Done.")


def make_sign(token, key_values):
  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))

  a = '&'.join(args)
  print("a=", a)

  b = hashlib.md5(a).hexdigest()
  print("b=", b)

  return b.upper()


def post_api(thread_index):

  api_url = "http://54.199.80.255:8080/pay"

  print("api_url", api_url)
  pid = 98
  token = "NEYnMvtiKWdsiRlNKulPyWGQLOwbpeUd"

  #money = random.randint(1,3000)
  
  money = "6000.00"
  sn = "thred%s-sn%s" % (thread_index, int(time.time()))
  pay_type_group = 'banktocard'
  notify_url = "http://52.79.37.229:12048/callback"

  sign = make_sign(token, [
    ("pid", pid),
    ("money", money),
    ("sn", sn),
    ("pay_type_group", pay_type_group),
    ("notify_url", notify_url), 
    ("key", token),
  ])
  

  remark = random.choice(["王武","王5","王五","三五","135XX","35XX35"])

  post_data = {
    "pid": pid,
    "money": money,
    "sn": sn,
    "notify_url": notify_url,
    "pay_type_group": pay_type_group,
    "remark": remark,
    'sign': sign,
  }

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)
  print("response", a)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
