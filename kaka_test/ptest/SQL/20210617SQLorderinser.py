from __future__ import print_function
import pymysql
import time
import threading


def get_db_opts():
  opts = {
    "host":"13.124.70.143",
    "port":3306,
    "user":"chen02",
    "password":"7291220Cc/",
    "db":"chenpays",
    "charset":"utf8",
  }
  return opts

def test_mysql():
  opts = get_db_opts()
  conn = pymysql.connect(**opts)
  print("conn",conn)
  with conn.cursor() as cursor:
    cursor.execute("use chenpays")
    cmd = "show tables;"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    #for r in rows:
      # print (cmd,r)
    
    
    
    #for i in range(1000000):

    
    #money =1+i 
    adminid = 93
    status = 1
    notify_url = "test"+time.ctime()
    sn = "sn%s" % time.time()

    #cmd_inser = """INSERT INTO `chenpays`.`lq_lowerhairs` (`real_money`, `status`, `notify_url`) VALUES ('%s', '%s', '%s');""" % (money,status,notify_url )
    cmd_inser = """INSERT INTO `chenpays`.`lq_orders` (`admin_id`, `sn`, `notify_url`, `status`) VALUES ('%s', '%s', '%s', '%s');""" % (adminid,sn,notify_url,status)
   

    print ("insert ----  "  ,cmd_inser)
    cursor.execute(cmd_inser)
    conn.commit()
    rs = cursor.fetchall()
    print ("rs ---  ", rs)



def main():
  print("def main")
  test_mysql()


if __name__ == "__main__":
  main()
  print(123)
