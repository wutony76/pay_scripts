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
  loop_delay = 1 / 8.0
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
  for i in range(10):
    threads.append(threading.Thread(target = work, args = (i,) ))
    threads[i].start()

  for i in range(10):
    threads[i].join()
  print("Done.")


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
  #api_url = "http://3.35.119.172:9410/pay"
  #api_url = "http://52.79.37.229:8080/cash/add"
  
  #api_url = "http://52.79.37.229:8080/cash/add"
  api_url = "http://13.124.29.97:8080/cash/add"

  #api_url = "http://api.dipay.cc/cash/add"

  print("api_url", api_url)
  #pid = 69
  #pid = 71
  pid = 72

  #ischeck =  random.randint(1,10)
  #if ischeck <= 1:
  #  bc_name = 70


  #token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
  token = "mWxThNaWeecfQesCLItMqlQvzvxhzHgD"
  ischeck =  random.randint(1,10)
  if ischeck <= 1:
    token = ""

  money =  random.randint(800,5599)
  #if total_coin < money and total_coin > 0:
  #  money = total_coin
  #else:
  #  total_coin = total_coin - money
  sn = "thred%s-sn%s" % (thread_index, int(time.time()))
  bc_type = "2"


  bc_name = "邮政储蓄银行"
  ischeck =  random.randint(1,10)
  if ischeck <= 1:
    bc_name = ""

  bc_num = "621*疑似敏感信息*4383943"
  bc_user = "潘洋平"

  ischeck =  random.randint(1,10)
  if ischeck <= 1:
    bc_user = ""



  pay_type_group = 'banktocard'
#  notify_url = "http://52.79.37.229:12009/callback"
  #notify_url = "http://13.124.29.97:8300/ant/test/testcallback"
  #notify_url = "http://52.79.37.229:8300/ant/test/testcallback"
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
    #json_data = json.loads(a)
    #print("code", json_data["code"])

  #  if json_data["code"] != 1:
  #    total_coin = total_coin + money
  #
  #print("total_coin -----------------------------------", total_coin)
  #return total_coin
        


    


if __name__ == "__main__":
  main()
