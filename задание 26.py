import time
import datetime

#1
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#2
print(time.localtime())

#3
for d in range(1, 6):
    print(d)
    time.sleep(3)