
import statistics as stats


from code.StockData import StockData


class StockMetrics(StockData): 
    def __init__(self, path):
        
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        #Run this code first
        # pt1
        #python -m code.test.validate pt1
        
        #Convert each string inside of the list into a float
        averages = []
        for row in self.data:
            print ("old row",row)
            new_row = [float(val) for val in row [1:] if val !="" and val!=" "]
            print("new_row",new_row)
    
        #Take this average that was calculated and append it into the empty list "averages"
        avg=stats.mean(row)
        averages=list.append((round),1,3)
        return averages
            

    def median02(self):
        """pt2
        python -m code.test.validate pt2
        """
        #Convert each string inside of the list into a float
        averages = []
        for row in self.data:
            print ("old row",row)
            new_row = [float(val) for val in row [1:] if val !="" and val!=" "]
            print("new_row",new_row)
    
        #Take this average that was calculated and append it into the empty list "averages"
        avg=stats.mean(row)
        averages=list.append((round),1,3)
        return averages

    def stddev03(self):
        """pt3
        python -m code.test.validate pt3
        """
            #Convert each string inside of the list into a float
        averages = []
        for row in self.data:
            print ("old row",row)
            new_row = [float(val) for val in row [1:] if val !="" and val!=" "]
            print("new_row",new_row)
    
        #Take this average that was calculated and append it into the empty list "averages"
        avg=stats.mean(row)
        averages=list.append((round),1,3)
        return averages
