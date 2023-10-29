# This is the file I modified on 10-22-2023
import csv
from msilib.schema import SelfReg


file = "data/raw/amzn.csv"

import time
from datetime import datetime

class StockData:
    def __init__(self, path):
        Self.path = path
        Self.data = None

    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header= next(reader,None) 
        for row in reader:
        # Split the row into a list of strings.
        #string.split(delimiter)
            row = "1,2,3" 
            row.split(",")
        # Strip the whitespace from each string in the list.
            row = [s.strip() for s in row]
            print(row)


epoch = time.time()
SelfReg._date = datetime.utcfromtimestamp(epoch).\
    strftime('%Y-%m-%d %H:%M:%S')
print("DATA LOADED AT", SelfReg._date)

#### Questions on this part
with open Self.data,newline="data/raw/amzn.csv"; csvfile: file
reader = csv.reader(file)
    # skip header row
next(reader, None)
    # append list of strings into list
Self.data = []
Self.data.extend(iter(reader))
            