import os
import time
import datetime

def UTCpluseight():
  timenow = datetime.datetime.now()
  timeplus = datetime.timedelta(hours=8)
  strtime = (timenow+timeplus).strftime("%Y_%m_%d_%H%M")
  return strtime

def main():
  
  while True:
    time.sleep(2)  
    os.popen("free -m >> free.txt")
    #os.popen("date -d \"+8 hour\">> free.txt")

if __name__=='__main__':
  main()