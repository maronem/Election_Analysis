#Import csv module
import csv
import os

# Chaining to assign variable for file to load and the path
election_file = os.path.join("Module_3_resources", "election_results.csv")

#Open Election results and read the file
with open(election_file) as election_data:
    print(election_data)

# To do: read and analyze the data here:
    file_reader = csv.reader(election_data)

# Print each row in the CSV file
    #for row in file_reader:
        #print(row)
        #adding for gitbash
# Print the header row - next() skips the first row and returns next item on the list
    headers = next(file_reader)
    print(headers)




