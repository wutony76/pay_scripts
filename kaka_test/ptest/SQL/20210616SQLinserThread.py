from __future__ import print_function
import time
import threading
import Queue
import pymysql




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



def kaka_test_orderinser(thread_index):

  print("work"+str(thread_index))
  opts = get_db_opts()
  conn = pymysql.connect(**opts)
  #print("conn",conn)
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
    sn = "thread%s_sn%s" % (thread_index,int(time.time()))
    
    #cmd_inser = """INSERT INTO `chenpays`.`lq_lowerhairs` (`real_money`, `status`, `notify_url`) VALUES ('%s', '%s', '%s');""" % (money,status,notify_url )
    cmd_inser = """INSERT INTO `chenpays`.`lq_orders` (`admin_id`, `sn`, `notify_url`, `status`) VALUES ('%s', '%s', '%s', '%s');""" % (adminid,sn,notify_url,status)

    #print ("insert ----  "  ,cmd_inser)
    #print ("addcount --- ",i)
    cursor.execute(cmd_inser)
    conn.commit()
    rs = cursor.fetchall()
    #print ("rs ---  ", rs)



    cmd_count = "SELECT count(*) FROM lq_orders;"

    #print ("count ----  "  ,cmd_count)
    
    cursor.execute(cmd_count)
    conn.commit()
    rs = cursor.fetchall()
    
    print ("rs ---  ", rs)
    
    



  

def work(num):
  #pass
  que = Queue.Queue()
  loop_delay = 1  #s
  
  while True:

    try:
      que.get(timeout=loop_delay)
    except Queue.Empty:
      pass
    
    
    kaka_test_orderinser(num)



def main():
  print("testmain")
  threads= []

  for i in range(100):
    threads.append(threading.Thread(target = work, args=(i,)))
    threads[i].start()

  #for i in range(500):
  #  threads[i].join()

  #print("Done.")

if __name__ == "__main__":
  main()
