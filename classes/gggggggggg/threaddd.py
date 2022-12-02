
import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print (str(self.threadID)+" Starting " + self.name)
      print_time(self.name, 3, self.counter)
      print (str(self.threadID)+"Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime()))
      counter -= 1


thread1 = myThread(1, "aaa", 2)
thread2 = myThread(2, "bbb", 1)
thread3 = myThread(3,"ccc",2)

thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
