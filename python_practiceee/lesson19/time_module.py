import time

print(time.time())
print(time.localtime())

cur_date = time.localtime()

print(cur_date)
print(cur_date.tm_mon)
print(cur_date.tm_mday)
print(cur_date.tm_year)
print(cur_date.tm_sec)
print(cur_date.tm_zone)

# print(f"Current time is {cur_date.tm_hour}:{cur_date.tm_min}:{cur_date.tm_sec}")
# cur_time_sec = time.time()
# time.sleep(3.5)
#
# print(f"Difference was {time.time() - cur_time_sec}")

cur_time = time.time()
while time.time() - cur_time < 10:
    print("sending..")
    time.sleep(1)