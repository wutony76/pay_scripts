from __future__ import print_function
import os 
import sys
import time 

import boto3


ACCESS_KEY = 'AKIASBEDCTAPXEHLMC6H'
SECRET_KEY = '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'


def upload_to_aws(my_file, bucket, s3_file):
  s3_client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY,region_name='ap-east-1')
  print("s3.client", s3_client)

  try:
    s3_client.upload_file(my_file, bucket, s3_file)
    print("File Upload Successful.")
    return True

  except Exception as e:
    print("File Upload errors.")
    print(e)
    return False


def main():
  #test_redis()
  argv = list(sys.argv)
  try:
    up_file = argv[1]
  except:
    print ("no up_file.")
    return

  try:
    print ( "up_file -", up_file)   #select my upload file
    file_list = os.listdir('.')
    print (os.listdir('.'), len(file_list))

    if len(file_list) <= 0:
      raise Exception ("no file.")
    if up_file not in file_list:
      raise Exception ("no this file.")
    

    #--- upload this file ---#
    #--get bucket_list--
    s3 = boto3.resource('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY)
    bucket_list = []
    for bucket in s3.buckets.all():
      print(bucket.name)
      bucket_list.append(bucket.name)

    bucket_name = "hk-sql"  #select s3 bucket
    if bucket_name not in bucket_list:
      raise Exception ("no this bucket.")

    #--upload file--
    ts = time.time()

    uploaded = upload_to_aws(up_file, bucket_name, up_file)

    n_ts = time.time()
    delta = n_ts - ts
    print("----- run.time -----= ", delta)

    if uploaded:
      print("upload success.")
    else:
      print("upload errors.")
    #--- upload this file end.---#
  
  except Exception as e:
    print ("Exception =",e)


if __name__ == "__main__":
  main()
