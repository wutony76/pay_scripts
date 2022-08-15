from __future__ import print_function
import json
import requests

def main(*args):

  url = 'http://3.115.201.240:8092/api/v1'
  access_key = 'OGQ5NmRhNGItN2MwMS00YzA5LTg1MjctZGY5NzNkYmE2YzUy' 

  params = {
    'access_key': access_key,
    'method': 'bind_otp',
    #'user_key': '2-dino01',
    #'user_key': 'B&T-TOKYO-97-DINO01',
    'user_key': 'B&T-TOKYO-84-jlb1688',
    #'google_key':'VCU6WYCQAUS657TL',
    'google_key':'X7QKDU4DIMTENZ67',
  }


  rep = requests.post(url, data={
    'params': json.dumps(params),
  })

  rep = rep.json()
  print('rep', rep)

if __name__ == "__main__":
  main()


