from __future__ import print_function

import os 
import sys
import time 

import boto3


ACCESS_KEY = 'AKIASBEDCTAPXEHLMC6H'
SECRET_KEY = 'FqSZA9TAtZrZ4NxqerBaZbT114fmX1Sihr4zS/Ir'


import boto3
from botocore.exceptions import ClientError


def test_email():
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    #SENDER = "Sender Name <sender@example.com>"
    SENDER = "SES <ttt@firecatworks.com>"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    #RECIPIENT = "recipient@example.com"
    RECIPIENT = "xizhiw247@gmail.com"

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the 
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "ap-northeast-2"

    # The subject line for the email.
    SUBJECT = "Amazon SES Test (SDK for Python)"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                )
                
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
          AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])




#def upload_to_aws(my_file, bucket, s3_file):
#  s3_client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY,region_name='ap-east-1')
#  print("s3.client", s3_client)
#
#  try:
#    s3_client.upload_file(my_file, bucket, s3_file)
#    print("File Upload Successful.")
#    return True
#
#  except Exception as e:
#    print("File Upload errors.")
#    print(e)
#    return False


def main():
  print("start main")
  test_email()
  ##test_redis()
  #argv = list(sys.argv)
  #try:
  #  up_file = argv[1]
  #except:
  #  print ("no up_file.")
  #  return

  #try:
  #  print ( "up_file -", up_file)   #select my upload file
  #  file_list = os.listdir('.')
  #  print (os.listdir('.'), len(file_list))

  #  if len(file_list) <= 0:
  #    raise Exception ("no file.")
  #  if up_file not in file_list:
  #    raise Exception ("no this file.")
  #  

  #  #--- upload this file ---#
  #  #--get bucket_list--
  #  s3 = boto3.resource('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_KEY)
  #  bucket_list = []
  #  for bucket in s3.buckets.all():
  #    print(bucket.name)
  #    bucket_list.append(bucket.name)

  #  bucket_name = "hk-sql"  #select s3 bucket
  #  if bucket_name not in bucket_list:
  #    raise Exception ("no this bucket.")

  #  #--upload file--
  #  ts = time.time()

  #  uploaded = upload_to_aws(up_file, bucket_name, up_file)

  #  n_ts = time.time()
  #  delta = n_ts - ts
  #  print("----- run.time -----= ", delta)

  #  if uploaded:
  #    print("upload success.")
  #  else:
  #    print("upload errors.")
  #  #--- upload this file end.---#
  #
  #except Exception as e:
  #  print ("Exception =",e)


if __name__ == "__main__":
  main()
