import subprocess
import os

def machine_cpu():
  comm_cpu_usage = "ps -aux| tail -n +2 | awk '{print $3}'"
  linux_cpu_data = os.popen(comm_cpu_usage).readlines()
  #print ("linux_cpu_data", linux_cpu_data )
  cpu_data = [ float(str_d.replace("\n", "")) for str_d in linux_cpu_data ]
  cpu_usage = sum(cpu_data)
  print ("cpu_usage", cpu_usage )
  return cpu_usage


def maxopenfile():


  lsofwcl = "lsof |wc -l"
  filemax= "cat /proc/sys/fs/file-max"
  nropen = "cat /proc/sys/fs/nr_open"
  ulimitof = "ulimit -n"

  lsofwcl_data = os.popen(lsofwcl).readlines()
  filemax_data = os.popen(filemax).readlines()
  nropen_data = os.popen(nropen).readlines()
  ulimitof_data = os.popen(ulimitof).readlines()


  lsofwcl_data_str= (str(lsofwcl_data)[2:-4])  
  filemax_data_str = (str(filemax_data)[2:-4])
  nropen_data_str = (str(nropen_data)[2:-4])
  ulimitof_data_str = (str(ulimitof_data)[2:-4])
 
  print (lsofwcl_data_str)
  print (filemax_data_str)
  print (nropen_data_str)
  print (ulimitof_data_str)

  return lsofwcl_data_str,filemax_data_str,nropen_data_str,ulimitof_data_str
  

def main():

  maxopenfile()


if __name__ == '__main__':
  main()