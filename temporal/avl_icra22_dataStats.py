"""
This file opens all the csvs with the labels of the data that
we collected, and gives some statistics.
"""
import csv
import os
location = os.getcwd()  # Get current working directory
counter = 0     # Keep a count of all files found
csvfiles = []   # List to store all csv files found at location

fields = []
rows = []
# --- Step 1: Open csf file



with open('/home/avl/ur_ws/src/apple_proxy/bag_files/csvs/stat_trial.csv') as csv_file:
    # Create  a csv object
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Extract field names through first row
    fields = next(csv_reader)

    # Extract each data row one by one
    for row in csv_reader:
        rows.append(row)

print(fields)
print(rows)


for file in os.listdir(location):
    try:
        if file.endswith(".py"):
            print("csv file found:\n", file)
            csvfiles.append(str(file))
            counter = counter + 1

    except Exceptio as e:
        raise e
        print("No files found here!\n")

print("Total files found:\n", counter)



#print(csv_reader)
# --- Step 2: Get the data from that file that we are interested in


