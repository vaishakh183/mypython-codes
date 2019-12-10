import time
print(time.ctime())
print(time.time())
print(time.asctime())
print(time.gmtime())
now=time.gmtime()
print(now.tm_hour,now.tm_min)
print(now[0])


