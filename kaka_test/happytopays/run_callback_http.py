

def app(env, start_response):
  print("request", env["PATH_INFO"])
  
  start_response('200 OK', [('Content-Type', 'text/html')])

  return [b'OK']

def main():
  from gevent.pywsgi import WSGIServer


  addr = ('0.0.0.0', 13001)
  print("listen", addr)
  wsgi = WSGIServer(addr, app)
  wsgi.serve_forever()


if __name__ == "__main__":
  main()
