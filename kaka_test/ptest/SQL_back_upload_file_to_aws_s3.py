from __future__ import print_function
import os
import sys
import time
import datetime
import boto3

ACCESS_KEY = 'AKIASBEDCTAPXEHLMC6H'
SECRET_KEY = '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'


def find_last_file(path):  
  files = os.listdir(path)
  files.sort(key=lambda file_name:os.path.getmtime(os.path.join(path,file_name)))
  last_file_name = files.pop()
  return last_file_name

def upload_to_aws_s3(path,last_file_name,bucket_name):
  try:
    s3_client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY,region_name='ap-east-1')
    s3_bucket = boto3.resource('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY)
    bucket_list=[]
    for bucket in s3_bucket.buckets.all():
        bucket_list.append(bucket.name)
    last_file_path = path+last_file_name
    
    s3_client.upload_file(last_file_path,bucket_name,last_file_name)
    return True
  except Exception as e:
    print("upload_to_aws_s3_error--->",e)
    return False


def UTC_plus_eight():
  time_now = datetime.datetime.now()
  time_plus = datetime.timedelta(hours=8)
  str_time = (time_now+time_plus).strftime("%Y_%m_%d_%H%M")
  return str_time

def pick_str(comme):
  readaline = os.popen(comme).readline()
  str_replace = str(readaline).replace("\n","")
  return str_replace

def back_up_sql(username,password,path,hostname,dbname,time):
  back_up_comme = os.system("mysqldump -u%s -p%s %s > %s%s_%s_%s.sql;"%(username,password,dbname,path,hostname,dbname,time))
  print ('back_up_comme',back_up_comme)
  print ("%s Backup Done!"%(hostname))

def file_size_check(path_name,location):
  os.system("du -sh %s*"%(path_name))
  print("check %s SQL File size!!!"%(location))

def SQL_back_up():
  SEL_db_name = "enpays"
  HKG_db_name = "pays"
  TYO_db_name = "pays"
  SEL_path= "/sql_backup/"
  HKG_path = "/sql_copy/"
  TYO__path = "/sql_copy/"
  user_name= "root"
  SEL_password = "8ph7uaf6wR+q"
  HKG_password = "\&4Rldo93n!@"
  TYO_password = "jSfhaN50i"
  SEL_host_name = "ip-13-0-1-190"
  HKG_host_name = "ip-10-0-1-101"
  TYO_host_name = "ip-10-0-1-100"
  bucket_name = "hk-sql"
  host_name_comme = "hostname -s"
  host_name = pick_str(host_name_comme)
  print(host_name)

  try:

    if host_name == TYO_host_name:
      print('here is TYO')
      TYO = "TYO"
      back_up_sql(user_name,TYO_password,TYO__path,TYO,TYO_db_name,UTC_plus_eight())
      file_size_check(TYO__path,TYO)
      last_file_name=find_last_file(TYO__path)
      upload = upload_to_aws_s3(TYO__path,last_file_name,bucket_name)
      if upload:
        print('success')
      else:
        print('fail')
    elif host_name == HKG_host_name:
      print('here is HKG')
      HKG = "HKG"   
      back_up_sql(user_name,HKG_password,HKG_path,HKG,HKG_db_name,UTC_plus_eight())
      file_size_check(HKG_path,HKG)
      last_file_name=find_last_file(HKG_path)      
      upload=upload_to_aws_s3(HKG_path,last_file_name,bucket_name)
      if upload:
        print('success')
      else:
        print('fail')
      
    elif host_name == SEL_host_name:
      print('here is SEL')
      SEL = "SEL"
      back_up_sql(user_name,SEL_password,SEL_path,SEL,SEL_db_name,UTC_plus_eight())
      file_size_check(SEL_path,SEL)
      last_file_name=find_last_file(SEL_path)
      upload=upload_to_aws_s3(SEL_path,last_file_name,bucket_name)
      if upload:
        print('success')
      else:
        print('fail')
    else:
      print("unknow")
      print("Now_time:",UTC_plus_eight())
  except Exception as e:
    print('SQL_back_up_e--->',e)

  
def main():
  print("start")
  SQL_back_up()


if __name__ == '__main__':
  main()