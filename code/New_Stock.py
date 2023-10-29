import csv



class StockData:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_csv(self):
        with open(self.filename, 'r') as file:
            # TODO: Use the csv.reader function to read the contents of the file
            reader = csv.reader(file)  # Replace None with appropriate code

            # TODO: Skip the header of the CSV file
            next(reader)
            for row in reader:
                print(row)
                self.data.append(row)

    def calculate_lengths(self):
        lengths = []
        for row in self.data:
            # TODO: Count the number of non-empty items in each row
            # and append the count to the lengths list
            # also be sure to ignore the date value in this list
            lengths = len(row[1:0]) # Replace None with appropriate code
            lengths.append()
        return lengths


# Part 2: Instantiate the StockData class and call its methods
# TODO: Create an instance of StockData with the filename 'stock_data.csv'
stocks = StockData ("C:/Users/deema/Desktop/2-TKH/bank-activity-lab/data/raw/stock_data.csv")

# TODO: Call the read_csv method of the instance
stocks.read_csv()

# TODO: Print the data attribute of the instance
print(stocks.filename)

# TODO: Call the calculate_lengths method and print the result

def calculate_lengths(self):
        lengths = []
        for row in self.data:
            # TODO: Count the number of non-empty items in each row
            # and append the count to the lengths list
            # also be sure to ignore the date value in this list
            new_row = [] 
        for val in row if val [1:] else print("next row"):
            length = new_row(row)  # Replace None with appropriate code
            lengths.append(length)
            return lengths
        print(val)

