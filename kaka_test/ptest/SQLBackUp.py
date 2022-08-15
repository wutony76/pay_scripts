import os
import sys
import time
import datetime

def timeutcplusight():
  timenow = datetime.datetime.now()
  timedelta = datetime.timedelta(hours=8)
  strtime = (timenow +timedelta).strftime("%Y_%m_%d_%H%M")
  return strtime

def main():
  print(timeutcplusight)
  dbname = "enpays"
  username = "root"
  password = "8ph7uaf6wR+q"
  os.system("mysqldump -u%s -p%s %s > SEL_kaka_enpays_%s.sql;"%(username,password,dbname,timeutcplusight))
  print ("SEL SQL Backup Done!")
  os.system("du -sh *")
  print ("check SEL SQL File size!!!")


if __name__== '__main__':
  main()
