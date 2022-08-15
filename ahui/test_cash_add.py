import time
import hashlib
import requests

def make_sign(token, key_values):

  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))

  a = '&'.join(args)
  print("a=", a)

  b = hashlib.md5(a.encode()).hexdigest()
  print("b=", b)

  return b.upper()


def main():
  
  api_url = "http://api.happytopays.com/cash/add"


  pid = 11
  #token = "ELPpceENGvFiXXqwehhHCQNwzOrPQgWE"
  token = "KUieywMacaDsGBBnWtuncskSvDmRZgyJ"

  money = "1001.00"
#  sn = "sn%s" % int(time.time())
  sn = "snn%s" % int(time.time())


  bc_type = "2"
  bc_name = "邮政储蓄银行"
  bc_num = "621*test*4383943"
  bc_user = "test123"

  pay_type_group = 'banktocard'
  notify_url = "http://13.125.212.29:13001/callback"


  sign = make_sign(token, [
    ("pid", pid),
    ("money", money),
    ("sn", sn),
    ("bc_type", bc_type),
    ("bc_name", bc_name), 
    ("bc_num", bc_num), 
    ("bc_user", bc_user), 
    ("key", token),
  ])

  post_data = {
    "pid": pid,
    "money": money,
    "sn": sn,
    "bc_type":bc_type,
    "bc_name":bc_name,
    "bc_num":bc_num,
    "bc_user":bc_user,

    "notify_url": notify_url,
    'sign': sign,
  }
  print("post", api_url)

  req = requests.post(api_url, data=post_data)
  a = req.content
  print("call", req.status_code)

  if req.status_code == 200:
    print("response", a)

if __name__ == "__main__":
  main()
