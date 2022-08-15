from __future__ import print_function
import requests
import json

def main(*args):

  url = 'http://3.115.201.240:8092/api/v1'
  access_key = 'OGQ5NmRhNGItN2MwMS00YzA5LTg1MjctZGY5NzNkYmE2YzUy' 

  params = {
    'access_key': access_key,
    'method': 'uservkey',
    #'user_key': '2-dino01',
    'user_key': '2-dino01',
    #'user_v_key':111111,
    'user_v_key':111111,
  }


  rep = requests.post(url, data={
    'params': json.dumps(params),
  })

  rep = rep.json()
  print('rep', rep)

  print()

if __name__ == "__main__":
  main()

