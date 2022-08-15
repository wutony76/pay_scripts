from __future__ import print_function
import time
import threading
import Queue
import pymysql
import random



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



def kaka_test_orderupdata():
  print ("testupdatadef")
  #iprint("work"+str(thread_index))
  opts = get_db_opts()
  conn = pymysql.connect(**opts)
  #print("conn",conn)
  with conn.cursor() as cursor:
    cursor.execute("use chenpays")
    cmd = "show tables;"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for r in rows:
      #print (1)
      #print (cmd,r)    
      cmd_fineidstatus = "SELECT id,status FROM chenpays.lq_orders;" 
      #print ("id",cmd_fineidstatus)    
      cursor.execute(cmd_fineidstatus)
      conn.commit()
      rs = cursor.fetchall()
      

      for r in rs:
        #print (2)
        
        
        print("show id;",r[0] )
        cid, cstatus = r
        #id = r[0]
        print("show id", cid )
        print("show status",cstatus)
        status = 1
        #ran = random.randint(2,3)
        #cmd_update="UPDATE `chenpays`.`lq_orders` SET `status` = '%s' WHERE (`id` = '%s');"%(status,id)   
        #cursor.execute(cmd_update)
        #conn.commit()
        #rs = cursor.fetchall()
        #print("rs --- ",rs)
    
    #cmd_inser = """INSERT INTO `chenpays`.`lq_lowerhairs` (`real_money`, `status`, `notify_url`) VALUES ('%s', '%s', '%s');""" % (money,status,notify_url )
    #cmd_inser = """INSERT INTO `chenpays`.`lq_orders` (`admin_id`, `sn`, `notify_url`, `status`) VALUES ('%s', '%s', '%s', '%s');""" % (adminid,sn,notify_url,status)

    #print ("insert ----  "  ,cmd_inser)
    #print ("addcount --- ",i)
    #cursor.execute(cmd_inser)
    #conn.commit()
    #rs = cursor.fetchall()
    #print ("rs ---  ", rs)



    cmd_count = "SELECT count(*) FROM lq_orders;"

    #print ("count ----  "  ,cmd_count)
    
    cursor.execute(cmd_count)
    conn.commit()
    rs = cursor.fetchall()
    
    print ("rs count ---  ", rs)
    
    



  

def work():
  #pass
  que = Queue.Queue()
  loop_delay = 1  #s
  print ("testwork")
  #while True:
    #print("testwhile")
    #try:
      #que.get(timeout=loop_delay)
    #except Queue.Empty:
      #pass
    
    
  kaka_test_orderupdata()



def main():
  print("testmain")

  work()

  #threads= []

  #for i in range(100):
  #  threads.append(threading.Thread(target = work, args=(i,)))
  #  threads[i].start()

  #for i in range(500):
  #  threads[i].join()

  #print("Done.")

if __name__ == "__main__":
  main()
