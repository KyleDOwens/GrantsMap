import sys
import os
import csv



# Get command line arguments
if (os.getcwd().split("/")[-1] != "grants_map"):
        exit("ERROR: This script must be run from the project root directory")

if len(sys.argv) <= 1 or len(sys.argv) > 2:
    print(len(sys.argv))
    print("Wrong number of arguments! Usage:")
    print("python3 code_to_name.py <input_file>")
    exit()

input_file = "throwaway.txt"
if len(sys.argv) > 1:
    input_file = sys.argv[1]



# Loop through input of visited countries
visited = []
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip("\n").lower()
        line = line.replace(" ", "_")
        visited.append(line)
print(visited)
# Create new CSV data
rows = None
with open("countries.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
    for row in rows[1:]:
        row[3] = str(row[1] in visited)
        if (row[1] in visited):
            print(row[1])

# Write output to CSV
with open("countries.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)