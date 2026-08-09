
# Task 1________________________________________________________
print("Task 1"+ "-"*100)
filtered_lines = []
with open("hblog.txt", "r") as f:
    for line in f:
        if "Key TSTFEED0300|7E3E|0400" in line:
            # print(line)
            filtered_lines.append(line)

timestamp_list = []
for line in filtered_lines:
    split_line = line.split("Timestamp")
    timestamp = split_line[1].split("Key")
    timestamp = timestamp[0].strip()
    timestamp_list.append(timestamp)

print(timestamp_list)


#Task 2_______________________________________________________
print("Task 2"+ "-"*100)

import logging
from datetime import datetime

logging.basicConfig(filename="hblog_test.log",level=logging.WARNING)


for i in range(len(timestamp_list) - 1):
    a = timestamp_list[i]
    b = timestamp_list[i+1]
    a = datetime.strptime(a, "%H:%M:%S")
    b = datetime.strptime(b, "%H:%M:%S")
    difference = a - b
    dif = difference.total_seconds()

    if dif > 31 and dif < 33:
        logging.warning(f"Heartbeat at {b}: {dif} seconds")
    if dif >= 33:
        logging.error(f"Heartbeat error at {b}: {dif} seconds")

    # print(dif)
