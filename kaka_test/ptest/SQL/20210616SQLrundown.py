import requests
import sys
import pymysql
import time
import threading



def get_db_opts():
  opts = {
    "host": "13.124.70.143",
    "port": 3306,
    "user": "chen02",
    "password": "7291220Cc/",
    "db": "chenpays",
    "charset": "utf8",
  }
  return opts

def test_mysql():
  opts = get_db_opts()
  conn = pymysql.connect(**opts)
  
  print ("conn",conn)


  with conn.cursor() as cursor:
    cursor.execute("use chenpays") 
    cmd = "show tables;"
    cursor.execute(cmd)
    rows  = cursor.fetchall()
    #print(cmd,rows)
    for r in rows:
        print (cmd,r)
    for i in range(100):
      money = i+1
      status = 5
      notify_url = "test"+time.ctime()
      
      cmd_inser = """INSERT INTO `chenpays`.`lq_lowerhairs` (`real_money`, `status`, `notify_url`) VALUES ('%s', '%s', '%s');""" % (money,status,notify_url )
      print ("insert --- ",cmd_inser)
      cursor.execute(cmd_inser)
      conn.commit()
      rs = cursor.fetchall()
      print ("rs ---- ",rs)


    cmd = "SELECT count(*) FROM lq_lowerhairs;"
    cursor.execute(cmd)
    rs = cursor.fetchall()
    print ("rs ---- ",rs)
    



def main():


  test_mysql()

 #mian()
