from __future__ import print_function
import sys
#import redis
import pymysql



def test_redis():
  r = redis.StrictRedis('11.0.0.154')

  keys = ["key1",]

  for key in keys:

    r.set(key, '123')
    rtn = r.get(key)
    print("get", key, rtn)

def get_db_opts():
  opts = {
    "host": "3.35.172.98",
    "port": 3306,
    "user": "root",
    "password": "&4Rldo93n!@",
    "db": "ttt_dapp",
    "charset": "utf8",
  }
  return opts



def show_columns(cursor, table_name):
    cmd = "SHOW COLUMNS FROM %s;" % table_name
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for r in rows:
      print("show_columns", r)


def test_mysql():
  opts = get_db_opts()
  conn = pymysql.connect(**opts)
  print("conn", conn)
  #with conn.cursor() as cursor:
  #  
  #  cursor.execute("use DB2")

  #  if True:
  #    cmd = "show tables;"
  #    cursor.execute(cmd)
  #    rows = cursor.fetchall()
  #    #print(cmd, rows)
  #    for r in rows:
  #      print("show table", r)

  #  show_columns(cursor, "lq_users")


def main():
  #test_redis()
  argv = list(sys.argv)
  argv.pop(0)

  #incr_member_dfbalance(argv)
  test_mysql()

if __name__ == "__main__":
  main()
