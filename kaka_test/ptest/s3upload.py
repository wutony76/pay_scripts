import boto3
import os
import sys


ACCESS_KEY = 'AKIASBEDCTAPXEHLMC6H'
SECRET_KEY = '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'

def find_last_file(path):  
  files = os.listdir(path)
  files.sort(key=lambda file_name:os.path.getmtime(os.path.join(path,file_name)))
  last_file_name = files.pop()
  return last_file_name



def main():
  
  s3_client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY,region_name='ap-east-1')
  
  print('s3_client--->',s3_client)

  s3_bucket = boto3.resource('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY)
  bucket_list=[]
  for bucket in s3_bucket.buckets.all():
    print(bucket.name)
    bucket_list.append(bucket.name)

  path= '/sql_copy/'

  print('lsit_file_name--->',find_last_file(path))

  
  last_file = find_last_file(path)
  bucket_name = "hk-sql"

  if bucket_name not in bucket_list:
    raise Exception ("no this bucket.")

  last_file_path = path+last_file


  #try:

  print('last_file_path',last_file_path)
  uploaded =s3_client.upload_file(last_file_path,bucket_name,last_file)
  if uploaded:
    print('success.')
  else:
    print('fail.')
 # except Exception as e:
   # print('error--->',e)

  










if __name__=='__main__':
  main()


