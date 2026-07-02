import sys
import os
import csv


output_text = ""
input_file = "throwaway.txt"
output_file = None


# Get command line arguments
if (os.getcwd().split("/")[-1] != "grants_map"):
        exit("ERROR: This script must be run from the project root directory")

if len(sys.argv) <= 1 or len(sys.argv) > 3:
    print("Wrong number of arguments! Usage:")
    print("python3 name_to_group.py <input_file> [<output_file>]") 
    exit()

if len(sys.argv) > 1:
    input_file = sys.argv[1]
if len(sys.argv) > 2:
    output_file = sys.argv[1]


# Read in groupings from CSV
groupings = {}
with open("countries.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        groupings[row[1]] = row[2]


# Loop through input
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        if line.strip("\n") in groupings:
            output_text += groupings[line.strip("\n")] + "\n"
        else:
            print("Country " + line.strip("\n") + " not in a group!")


# Print/Write output
if output_file:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(output_text)
else:
    print(output_text)