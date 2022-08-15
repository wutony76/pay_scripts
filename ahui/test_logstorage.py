from __future__ import print_function
import time
import socket
import struct
import random
import uuid
import msgpack


class Client(object):

  def __init__(self):
    self.sock = None

  def connect(self, addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)

    self.sock = sock
    self._recv_state = 0
    self._recv_buf = ''
    self._packet_len = None

  def call(self, cmd, *cmd_args):
    self.send_packet(2, cmd, *cmd_args)

    while True:
      packet = self.recv_packet()
      #print('recv_packet', packet)
      op = packet[0]
      if op == 3:
        code = packet[1]
        rtn = packet[2]
        reason = packet[3]
        if code == 0:
          return rtn

        raise Exception(reason)

  def recv_packet(self):
    
    for i in xrange(4096):
      buf = self.sock.recv(4096)
        
      if not buf:
        print('recv', repr([buf]))
        raise Exception('connectionLost')

      self._recv_buf = self._recv_buf + buf
      
      if self._recv_state == 0:
        if len(self._recv_buf) >= 4:
          hdr, self._recv_buf = self._recv_buf[:4], self._recv_buf[4:]
          self._packet_len = struct.unpack('>I', hdr)[0]
          self._recv_state = 1

      if self._recv_state == 1:
        if len(self._recv_buf) >= self._packet_len:
          packet, self._recv_buf = self._recv_buf[:self._packet_len], self._recv_buf[self._packet_len:]
          packet = msgpack.unpackb(packet)
          self._packet_len = None
          self._recv_state = 0

          return packet
          
      

  def send_packet(self, op, cmd, *cmd_args):
    packet = [op, cmd, cmd_args]
    data = msgpack.packb(packet)
    send_data = struct.pack('>I', len(data)) + data
    self.sock.send(send_data)


def main():

  cli = Client()
  cli.connect(('127.0.0.1', 9422))


  total_rows_count = 0

  for k in xrange(2**20):

    test_args = []

    for i in xrange(32):
      rows = []
      #admin_id = random.choice([69, 70, 71])
      now_t = time.time()
      uts = int(now_t * 10000)

      t_k = "%014x" % uts

      admin_id = random.choice([69])
      out_sn = "%s-%s" % (t_k[:12], str(uuid.uuid4()))

      rows_count = random.randint(1, 100)
      _rnd = random.randint(0, 10000)
      if _rnd > 9000:
        rows_count = random.randint(1, 2048)
      elif _rnd > 7000:
        rows_count = random.randint(1, 256)

      test_args.append((admin_id, out_sn, rows_count))

      for j in xrange(rows_count):
        ts = time.time()
        data = {
          'admin_id': admin_id,
          'out_sn': out_sn,
          'seq': j,
          'rows_count': rows_count,
        }
        row = [ts, 1001, data]
        rows.append(row)

      cli.call('APPEND_ORDER_LOG', *rows)

    for x in test_args:
      admin_id, out_sn, rows_count = x
      rows = cli.call('GET_ORDER_LOG', admin_id, out_sn)[0]
      #first = rows[0]
      #rows_count = first['rows_count']

      total_rows_count += rows_count

      print('GET_ORDER_LOG total_rows_count=%s out_sn=%s' % ('{:,}'.format(total_rows_count), out_sn), 'rows_count', rows_count, 'rows', len(rows))
      assert len(rows) == rows_count

  


if __name__ == "__main__":
  main()
