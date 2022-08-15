import requests

def main(*args):
  print ("run sms.")

#  requests.get()
  url = "http://api.twsms.com/json/sms_send.php"
  data = {
    "username":"xizhiw247",
    "password":"avfddcec78",
    "mobile":"0912345678", #接收簡訊手機
    "message":" test 123456. ", #簡訊訊息
  }
 
  rep = requests.get( url, data )
  print( rep ) 


  if rep.status_code == 200:
    print( rep.content )

