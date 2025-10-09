import csv

all_uids = []
with open("10-07.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        if len(row) > 1:
            all_uids.append(row[1].strip())

for i in range(0, len(all_uids), 20):
    print(",".join(all_uids[i:i+20]))

