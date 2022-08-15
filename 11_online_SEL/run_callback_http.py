from __future__ import print_function

import hashlib
import json




def make_sign(token, key_values):
  args = []
  for k, v in key_values:
    args.append('%s=%s' % (k, v))
  a = '&'.join(args)
  print("step1 a=", a)
  b = hashlib.md5(a.encode("utf-8")).hexdigest()
  print("step2 b=", b)
  return b.upper()


def app(env, start_response):
  print("request", env["PATH_INFO"])
  #print("request", env)

  data = env['wsgi.input'].read()
  data = json.loads(data)
  print("data", data)


  if env["PATH_INFO"].index('cash') > 0:
    print( "ttt", "iscash" )

    #pid = 2
    #token = "ePTXmOMkGoKPEpDntfqfUkWYIffrMWgs"
    #pid = 3 
    token = "BgxcpSGAYRYcnCpWnhKUNbdLYTyqsxTh"

    sign = make_sign(token, [
      ("sn", data["sn"]),
      ("out_sn", data["out_sn"]),
      ("money", data["money"]), 
      ("pay_type", data["pay_type"]), 
      ("trade_status", data["trade_status"]), 
      ("key", token),
    ])
    print("sign", sign)
    print("="*50)

    if data["encryption"] == sign:
      print( "sn_check")
      print( "sn ", str(data["sn"]))
      print( "out_sn ", str(data["out_sn"]))
      print( "check is True.")




  if env["PATH_INFO"].index('pay') > 0:
    print( "ttt", "ispay" )

    #pid = 3 
    token = "BgxcpSGAYRYcnCpWnhKUNbdLYTyqsxTh"

    sign = make_sign(token, [
      ("sn", data["sn"]),
      ("out_sn", data["out_sn"]),
      ("money", data["money"]), 
      ("pay_type_group", data["pay_type_group"]), 
      ("trade_status", data["trade_status"]), 
      ("key", token),
    ])
    print("sign", sign)
    print("="*50)

    if data["encryption"] == sign:
      print( "sn_check")
      print( "sn ", str(data["sn"]))
      print( "out_sn ", str(data["out_sn"]))
      print( "check is True.")


  start_response('200 success', [('Content-Type', 'text/html')])
  #return [b'OK']
  return [b'success']




def main():
  from gevent.pywsgi import WSGIServer

  addr = ('0.0.0.0', 13001)
  print("listen", addr)
  wsgi = WSGIServer(addr, app)
  wsgi.serve_forever()

if __name__ == "__main__":
  main()
