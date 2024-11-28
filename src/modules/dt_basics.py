import time
import datetime
from time import perf_counter as myTimer # elapsed time
from time import process_time as processTimer # CPU time

# time library
print(time.gmtime(0))
print(time.localtime())
print(time.time())

print("Started at: {}".format(time.strftime("%X", time.localtime())))


start = myTimer()
startProcess = processTimer()
for i in range(1, 300000):
    x = i * i
end = myTimer()
endProcess = processTimer()

curr_time = time.localtime()
print(f"Year:{curr_time.tm_year} Month:{curr_time.tm_mon} Day;{curr_time.tm_mday}")

print(f"Time elapsed {end - start} Process time elapsed {endProcess - startProcess}")

print("=" * 80)
print("Epoch starts at: " + time.strftime("%c", time.gmtime(0)))
print("The current time zone: {} with an offset {}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("DST is effect for this location")
    print("DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

print("=" * 80)
print("Today from datetime " + str(datetime.datetime.today()))
print("Now from datetime " + str(datetime.datetime.now()))
print("UTC Now from datetime " + str(datetime.datetime.utcnow()))
