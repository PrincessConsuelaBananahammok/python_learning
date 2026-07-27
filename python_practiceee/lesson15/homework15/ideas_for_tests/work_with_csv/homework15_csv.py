import csv

rows_without_duplicates = set()

with open("r-m-c.csv") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        rows_without_duplicates.add(tuple(row))

with open ("random-michaels.csv") as csvfile2:
    reader2 = csv.reader(csvfile2)
    next(reader2)
    for row in reader2:
        rows_without_duplicates.add(tuple(row))

with open("result_file.csv", "w") as csvfile3:
    writer3 = csv.writer(csvfile3)
    writer3.writerow(header)
    writer3.writerows(rows_without_duplicates)