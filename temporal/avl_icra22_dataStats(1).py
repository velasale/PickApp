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

# --- Step 1: Get a list of the csv files that will be analyzed
location = location + '/2 - Apple Proxy with spherical approach/' + 'sep03_appleProxy_spherical_withoutNoise (Round1)'
for file in os.listdir(location):
    try:
        if file.endswith(".csv"):
            print("csv file found:\n", file)
            csvfiles.append(str(file))
            counter = counter + 1
    except Exceptio as e:
        raise e
        print("No files found here!\n")
print("Total files found:\n", counter)


# --- Step 2: Obtain the desired data of each file and
success = 0
failures = 0
other = 0
for i in range(counter):
    file_to_open = location + '/' + csvfiles[i]
    print(file_to_open)
    with open(file_to_open) as csv_file:
        # Create  a csv object
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Extract field names through first row
        fields = next(csv_reader)
        # Extract each data row one by one
        for row in csv_reader:
            rows.append(row)

        if rows[0][10] == 's':
            success = success + 1
        elif rows[0][10] == 'f':
            failures = failures + 1
        else:
            other = other + 1
        #print(rows[0])
        #print(rows[0][10])

print('Success: ', success)







#print(csv_reader)
# --- Step 2: Get the data from that file that we are interested in


