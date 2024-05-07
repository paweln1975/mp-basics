import time

current_time = time.gmtime()
print(f"It's {current_time}.")

current_time = time.asctime(time.gmtime())  # first option
print(f"It's {current_time}.")

current_time = time.strftime("%H:%M", time.gmtime())  # second option
print(f"It's {current_time}.")

current_time = time.strftime("%H:%M", time.localtime())
print(f"It's {current_time}.")

print(time.ctime(time.time())) # returns in seconds time passed from epoch

print(time.gmtime(0))  # on Windows

start = time.perf_counter()


last_time = time.time()
current_time = time.strftime("%H:%M", time.localtime())
time.sleep(1)
new_cur_time = time.time()
time_passed = int((new_cur_time - last_time))  # let's print the result in minutes

print(f"Time passed: {time_passed} second(s)")

print("Something")
end = time.perf_counter()
total_time = end - start
print(f"Your program has executed for {total_time} seconds.")

print(time.timezone / 3600)  # let's print the result in hours for readability
print(time.tzname)
print(time.daylight)
