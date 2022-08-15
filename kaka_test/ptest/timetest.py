import datetime
import time
import threading
import pytz


def timeutcplusight():
  timenow = datetime.datetime.now()
  timedelta = datetime.timedelta(hours=8)
  strtime = (timenow +timedelta).strftime("%Y_%m_%d_%H%M")
  return strtime


print(timeutcplusight())

tw = pytz.timezone('Asia/Taipei')
tokyo = pytz.timezone('Asia/Tokyo')
ddn = datetime.datetime.now()
ddnutc = ddn.replace(tzinfo=pytz.utc)
ddntw = ddn.replace(tzinfo=tw)
ddntokyo = ddn.astimezone(tokyo)
print ("ddn",ddn)
print ("ddnutc",ddnutc)
print ("ddntw",ddntw)
print ("ddntokyo",ddntokyo)

#print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
#print ((datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"))
'''
nowtime = time.time()
timedelta = datetime.timedelta(hours=8)
timezone = datetime.timezone(datetime.timedelta(hours=8))
timenow = datetime.datetime.now()
deltime = (timenow +timedelta).strftime("%Y_%m_%d_%H%M")
timeint = int(time.time())
localtime = time.localtime(time.time())
year = localtime.tm_year
mon = localtime.tm_mon
strtime = time.strftime("%Y_%m_%d_%H%M", time.localtime()) 
print ("test%stest"%(strtime))
print ("timeint",timeint)
print ("localtime",localtime)
print ("mon",mon)
print ("strtime",strtime)
print ("nowtime",nowtime)
print ("timezone",timezone)
print ("timenow",timenow)
print ("timedelta",timedelta)
print ("deltime",deltime)
'''