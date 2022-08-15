from __future__ import print_function
import time
import threading
import Queue



def kaka_test(num):
  print("work"+str(num))
  


def work(num):
  #pass
  que = Queue.Queue()
  loop_delay = 1  #s

  while True:

    try:
      que.get(timeout=loop_delay)
    except Queue.Empty:
      pass

    kaka_test(num)



def main():
  print("testmain")
  threads= []

  for i in range(3):
    threads.append(threading.Thread(target = work, args=(i,)))
    threads[i].start()

  for i in range(3):
    threads[i].join()

  print("Done.")

if __name__ == "__main__":
  main()
