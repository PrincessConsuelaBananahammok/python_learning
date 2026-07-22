import csv

# Дані для запису у CSV-файл
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# with open("output.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)

with open("output.csv", "r") as csvfile:
    reader = list(csv.reader(csvfile))
    header = reader[0]
    rows = reader[1:]
    print("fff",header)
    for row in rows:
        print(row)
