from os import times
import pymysql
from pymysql import cursors
import time

from pymysql.times import Time

def get_db_opts():
  opts = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"1qaz",
    "db":"dnstest",
    "charset":"utf8",
  }
  return opts

def dbconnect():
  
  opts = get_db_opts()
  for key,value in opts.items():
    print(key,value)  
  db = pymysql.connect(**opts)
  with db.cursor() as cursor:
    cursor.execute("use dnstest")
    #cmd = "show tables;"
    while True:
      inputstr = input("enter :  ")
      print(inputstr)
      localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
      print (localtime)
      if inputstr == 'quit':
        break;
      cmd_inser= """INSERT INTO `dnstest`.`dns_str` (`str`, `date_time`) VALUES ('%s', '%s');""" % (inputstr,localtime)
      print (cmd_inser)
      cursor.execute(cmd_inser)
      db.commit()
      rs = cursor.fetchall()
      print(rs)

 
  
  


def main():
  #inputstr = input("輸入單字,")  
  #print (inputstr)
  dbconnect()

if __name__ == '__main__':
  main()