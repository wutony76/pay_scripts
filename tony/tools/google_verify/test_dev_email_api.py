from __future__ import print_function
import json
import requests

def main(*args):

  #url = 'http://3.115.201.240:8092/api/v1'
  url = 'http://3.35.172.98:8092/api/v1'
  access_key = 'OGQ5NmRhNGItN2MwMS00YzA5LTg1MjctZGY5NzNkYmE2YzUy' 

  params = {
    'access_key': access_key,
    'method': 'email_new',
    'user_key': '2-dino01',
    'email': 'wutony76@gmail.com',
  }


  rep = requests.post(url, data={
    'params': json.dumps(params),
  })

  rep = rep.json()
  print('rep', rep)

if __name__ == "__main__":
  main()


