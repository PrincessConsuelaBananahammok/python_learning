from datetime import datetime

row1 = "2026-08-03 19:49:59" #UTC ISO format
row2 = "24-08-03T7:49:40.200 PM" #UTC
row3 = "24-08-03 19:49:40.200 -0200" #TZ -2



row1_dt = datetime.fromisoformat(row1)


row1_dt = datetime.strptime(row1, "%Y-%m-%d %H:%M:%S")
row2_dt = datetime.strptime(row2, "%y-%m-%dT%I:%M:%S.%f %p")
row3_dt = datetime.strptime(row3, "%y-%m-%d %H:%M:%S.%f %z")
#
# print(row1_dt.date())
# print(type(row1_dt))
#
# print(row2_dt.date())

print(row2_dt)
print(row3_dt)

