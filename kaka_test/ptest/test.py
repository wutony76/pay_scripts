import time
import datetime
import queue
#import requests
#from requests import post
import os
import re
import subprocess
import sys
import random
import string


print("1")

'''
seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_ =-"
sa = []
for i in range(12):
  sa.append(random.choice(seed))
  salt = ''.join(sa)
print (salt)


path = r'C:\file_last_test'
#path= '/sql_copy/'
print('*'*100)
print('path--->',path)
print('*'*100)
files = os.listdir(path)
files.sort(key=lambda filename: os.path.getmtime(os.path.join(path, filename)))
#files.sort(key=lambda file_name:os.path.getmtime(file_name))
print(files)
print('*'*100)
lastfile = files.pop()
print(lastfile)






argv = list(sys.argv)[1]
print(argv)


VPS_data={

  #Hong Kong VPS
"user777":"18.162.82.121",
"user772":"18.167.76.60",
"user773":"18.163.181.247",
"user774":"18.163.127.181",
"user775":"18.162.245.192",
"user776":"18.167.84.108",
"user778":"18.167.84.155",

#Hong Kong VPS

"user801":"13.229.215.41",
"user802":"13.212.247.123",
"user803":"54.251.73.146",
"user804":"3.0.148.190",
"user805":"18.136.212.184",
"user806":"13.229.125.83",
"user807":"3.1.8.166",
"user808":"52.221.196.184",
"user809":"18.141.204.175",
"user810":"54.251.71.182",
"user811":"52.77.219.189",
"user812":"18.140.51.223",
"user813":"54.169.117.176",
"user814":"3.1.102.124"

}

for key,value in VPS_data.items():
  print("1",key,value)

for key in VPS_data:
  print("2",key,VPS_data[key])


test1 = "test1,test2,test3,"

splittest = (test1.split(","))[:-1]
print(splittest)
print(len(splittest))
for item in splittest:
  
  print(item)




q = queue.Queue()



post_time= "['2021/08/02 22:49:38']"
now_time = datetime.datetime.now()
post_time_1 = post_time.replace("[","").replace("]","").replace("\'","").replace("/","-")


date_str = datetime.datetime.strptime(post_time_1,"%Y-%m-%d %H:%M:%S")

print(post_time_1)
print(post_time)
print(now_time)
print(date_str)

time_cut = (now_time-date_str)
print(time_cut)



time_start = time.time()
print(time_start)
time.sleep(9)
time_end= time.time()
print(time_end)

time1 = time_end-time_start

if time1 >= 10:
  print("timeout")
else:
  print("pass")
print(time1)



list1 = [1,1,1,1,1]
list2 = [2,2,2,2,2]
list3 = [3,3,3,3,3]

listcount=[]

listcount = listcount+list1[0]+'\n'

print (listcount)

test = "test1"

list1 = ["1"+test,"2%s"]
print(list1)
strlist = str(list1)
print (strlist)

list1=[]
list1=[[1,2,3],[4,5,6]]
list2 = [[1,2,3],[4,5,6]]

print (list1[0][0])
print (list1)
print(list2)
toge=[]
toge.append(list1)
toge.append(list2)

print(toge)
togestr = (str(toge))
print (togestr)

try:
  i=1/0
  print("ri")
except Exception as e:
  print("not zero")

try:
  i=1/0
  print("ri")
except:
  print("not zero")

'''



