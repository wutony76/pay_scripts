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


import sys
import pymysql



def work(num):
  print("Thread ---------", num)

  que = Queue.Queue()
  loop_delay = 1 / 8.0
  while True:
    try:
      que.get(timeout=loop_delay)
    except Queue.Empty:
      pass
    
    post_api(num)


def show_columns(cursor, table_name):
    cmd = "SHOW COLUMNS FROM %s;" % table_name
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for r in rows:
      print("show_columns", r)


def get_db_opts():
  opts = {
    "host": "17.0.0.153",
    "port": 3306,
    "user": "root",
    "password": "&4RFV5tgb&",
    "db": "DB3",
    "charset": "utf8",
  }
  return opts


def test_mysql():
  opts = get_db_opts()
  conn = pymysql.connect(**opts)
  print("conn", conn)
  with conn.cursor() as cursor:
    cursor.execute("use DB3")
    if True:
      cmd = "show tables;"
      cursor.execute(cmd)
      rows = cursor.fetchall()
      #print(cmd, rows)
      for r in rows:
        print("show table", r)

      cmd = "SELECT id FROM lq_lowerhairs where status = 5;"
      cursor.execute(cmd)
      rows = cursor.fetchall()
      for r in rows:
        print("show table", r)
        print("---", r[0])
        #UPDATE `DB2`.`lq_lowerhairs` SET `users_id` = '1234', `status` = '1' WHERE (`id` = '1306');
        #cmd_update ="""UPDATE lq_lowerhairs SET users_id = '16760', status = '1' WHERE id = '%s';""" % r[0] 
        cmd_update ="""UPDATE lq_lowerhairs SET status = '3' WHERE id = '%s';""" % r[0] 
        print("---", cmd_update)
        cursor.execute(cmd_update)
        conn.commit()
        rs = cursor.fetchall()
        print("---", rs)

    #show_columns(cursor, "lq_users")

def main():
  test_mysql()





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
  pid = 69
  ischeck =  random.randint(1,10)
  if ischeck <= 1:
    bc_name = 70

  ischeck =  random.randint(1,10)
  token = "ewDimllyUOYMheMrqFCrnXqaTyCVVdNh"
  if ischeck <= 1:
    token = ""

  money =  random.randint(800,5599)

#  sn = "sn%s" % int(time.time())
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


if __name__ == "__main__":
  main()
