import hashlib



def make_sign(token, key_values):

  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))

  a = '&'.join(args)
  print("a=", a)

  b = hashlib.md5(a.encode("utf-8")).hexdigest()
  print("b=", b)

  return b.upper()



def main():

  pid = 18
  money="1000.00"
  sn = "508930"
  pay_type_group = "banktocard_payname"  
  notify_url="http://127.0.01:8087/api/yiranpay/channelpay/tljpay/notify/TLJPAY10001"
  token = "cShoOVTfkZYuzjxIIsyZmnWdqJutUSLB"

  sign = make_sign(token, [
  ("pid", pid),
  ("money", money),
  ("sn", sn),
  ("pay_type_group", pay_type_group),
  ("notify_url", notify_url), 
  ("key", token),
  ])




  pass


if __name__=="__main__":
  main()