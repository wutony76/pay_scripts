from __future__ import print_function
from datetime import datetime
import random
import json
#import Queue
#import msgpack
import gevent.queue

def app(env, start_response):

  print("="*100)
  print("request env", env)

  http_method = env['REQUEST_METHOD']
  #print("request METHOD", http_method)
  data = env['wsgi.input'].read()
  print("request", repr(data))
  data = json.loads(data)
  print("data", data)

  delay_sec = random.randint(0, 2)
  que = gevent.queue.Queue()

  for i in range(delay_sec):
    print('delay', i)
    try:
      que.get(timeout=1)
    except gevent.queue.Empty:
      pass


  start_response('200 OK', [('Content-Type', 'text/html')])

  return [b'success']

def handle_stream(sock, addrs):

  data = sock.recv(65536)
  print("handle_stream", repr(data))
  print("")
  print(data)

  content = "success"

  headers = [
    ('Content-Length',  len(content)),
    ('Content-Type',  'text/html'),
  ]


  headers = "\r\n".join(["%s: %s" % h for h in headers])


  rep = "HTTP/1.1 200 OK" + headers + "\r\n\r\n" + content


  sock.send(rep)


def main():
  from gevent.pywsgi import WSGIServer

  addr = ('0.0.0.0', 12009)

  print("run", addr)

  serv = WSGIServer(addr, app, log=None)
  serv.serve_forever()
  #from gevent.server import StreamServer

  #serv = StreamServer(addr, handle_stream)
  #serv.serve_forever()

if __name__ == "__main__":
  main()