import os
import sys
from os import listdir

def main():
  mypath ="/sql_backup/"
  serkey ="c_pays.pem"
  transtrage = "13.0.0.104"

  files = listdir(mypath)
  files.sort(key=lambda filename: os.path.getmtime(os.path.join(mypath, filename)))
  print(files)
  lastfile = files.pop()
  print(lastfile)
  print(serkey)
  print(transtrage)

  ml = mypath+lastfile
  print(ml)
  print("""scp -i "%s" %s centos@%s:~/."""%(serkey,ml,transtrage))
  os.system("""scp -i "%s" %s centos@%s:~/."""%(serkey,ml,transtrage))
  print ("File SQL Backup Transport to 13.0.0.104")

if __name__ == '__main__':
  main()
