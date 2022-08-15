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
  api_url = "http://13.124.29.97:8080/pay"
#  api_url = "http://52.79.37.229:8080/pay"

  print("api_url", api_url)

 # pid = 69
  pid = 75

  ischeck =  random.randint(1,10)
  if ischeck <= 1:
    token = "101"


  #token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
  token = "USMvePZFjkJfxEZACDeJYTcBiMYCbObR"
  ischeck =  random.randint(1,10)
  if ischeck <= 1:
    token = ""


  money = random.randint(1,3000)
  sn = "thred%s-sn%s" % (thread_index, int(time.time()))

  pay_type_group = 'banktocard'
  #notify_url = "http://52.79.37.229:12009/callback"
  #notify_url = "http://52.79.37.229:8300/ant/test/testcallback"
  notify_url = "http://52.79.37.229:12009/callback"
  #notify_url = "http://13.124.29.97:8300/ant/test/testcallback"

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

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)
  print("response", a)

  if req.status_code == 200:
    print("response", a)


if __name__ == "__main__":
  main()
