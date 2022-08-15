import time
import os
import sys
import subprocess
import pymysql
import logging

def main():
  
  #proc = subprocess.Popen(
  #  ['sudo su -'],
  #)
  
  retval = os.getcwd()
  strtime = time.strftime("%Y_%m_%d_%H%M", time.localtime())
  print (strtime)
  #os.popen("sudo su -")
  #os.system("sudo su -")
  #retval = os.getcwd()
  #print (retval)
  #os.chdir("/")
  #retval = os.getcwd()
  #print (retval)
  #print(1)
  #os.chdir("/home/")
  #retval = os.getcwd()
  #print (retval)
  #print(2)
  #os.system("/")
  #os.system("cd home/centos/")
  #os.system("ls")
  #os.system("""ssh -i "firedino_dev.pem" centos@13.124.70.143""")
  #os.system("sudo su -")
  #os.system("cd sqlchen/")
  #os.system("ls")
  #os.system("mysqldump -u root -p chenpays > kaka_copychenpays_%s.sql;"%(strtime))
  d = "dtest"
  
  print ("""ddd"%s"ddd%s"""%(d ,d))
if __name__ == '__main__':
    main()
