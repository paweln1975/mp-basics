import time
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
