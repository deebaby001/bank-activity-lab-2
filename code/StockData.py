import csv
from fileinput import filename
from msilib.schema import SelfReg


import time
from datetime import datetime

#from typing import Self
#from isort import file

from sklearn.semi_supervised import SelfTrainingClassifier


class StockData:
    def __init__(self, filename):
        self.path = filename
        self.data = None
        
        #def load(self):
        """A function to assign 
        Does not include headers.
        All data is expected to be a string
        """
    def load(self, filename):
            with open(filename, 'r') as f:
                self = self.load(f)
        #print(file)
        
        # to keep us in compliance with EU standards, we must log the datetime
        # of all data loads
    epoch = time.time()
    SelfTrainingClassifier.date = datetime.utcfromtimestamp(epoch).\
            strftime('%Y-%m-%d %H:%M:%S')
    print("DATA LOADED AT", SelfTrainingClassifier.date)

        # open data using csv reader
    def read_csv(self):
        with open(self.filename,'r') as file:
            reader = csv.reader(file)
            # skip header row
        next(reader, None)
            # append list of strings into list
        for row in reader:
                print(row)
                self.data.append(row)
