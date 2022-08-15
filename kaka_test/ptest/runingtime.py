import os
import re

comm = "ps -A -o cmd,time,etime,stime,%cpu,%mem |grep python|awk '$1==\"python\"'"
print("comm-->",comm)
comm_list= os.popen(comm).readlines()
print("comm_list-->",comm_list)
#comm_split=[]
#comm_split[:] = [str(re.split(r'\s+',item.replace("\n","")))for item in comm_list]

pyoutlist = []

for item in comm_list:
  print ("item-->",item)
  comm_kill_space = re.split(r'\s+',item)
  print ("comm_kill_space-->",comm_kill_space)
  print("comm_kill_space-->grep ",comm_kill_space [0])
  print("comm_kill_space-->cmd ",comm_kill_space [1])
  pyname = comm_kill_space [1]
  print("comm_kill_space-->time ",comm_kill_space [2])
  utime = comm_kill_space [2]
  print("comm_kill_space-->etime ",comm_kill_space [3])
  etime = comm_kill_space [3]
  print("comm_kill_space-->stime ",comm_kill_space [4])
  stime = comm_kill_space [4]
  print("comm_kill_space-->%cpu ",comm_kill_space [5])
  cpuuse = comm_kill_space [5]
  print("comm_kill_space-->%mem ",comm_kill_space [6])
  memuse= comm_kill_space [6]
  print(comm_kill_space[1:7])
  strinfo = ("name:%s,utime:%s,rtime:%s,sdate:%s,cpu:%s,mem:%s "%(pyname,utime,etime,stime,cpuuse,memuse))
  pyoutlist.append(strinfo)


print(pyoutlist)
'''
print ("comm_split-->",comm_split)
for item in comm_split:
  print("item-->",item)
  for initem in item:
    print ("initem-->",initem)
'''
'''

print("comm_split-->grep ",comm_split[1][0])
print("comm_split-->cmd ",comm_split[1][1])
print("comm_split-->time ",comm_split[1][2])
print("comm_split-->etime ",comm_split[1][3])
print("comm_split-->stime ",comm_split[1][4])
print("comm_split-->%cpu ",comm_split[1][5])
print("comm_split-->%mem ",comm_split[1][6])
'''



  #comm_cut=comm_print.split(" ")
  #print ("re.split-->",re.split(r'\s+',comm_print.replace("\n","")))
  #print ("re.findall-->",re.findall(r'\s+',comm_print))

