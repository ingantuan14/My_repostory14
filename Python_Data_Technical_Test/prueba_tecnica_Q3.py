import csv
# Import ZipFile class from zipfile module
from zipfile import ZipFile

# Files Path 
source_path = "C:/Users/Antonio Arana/proyecto_git/Python_Data_Technical_Test/Programming+Excercise (1).zip"
dirpath = "C:/Users/Antonio Arana/data_engineer"

# Seting variables
months = {
    '0': 'Jan',
    '1': 'Feb',
    '2': 'Mar',
    '3': 'Apr',
    '4': 'May',
    '5': 'Jun',
    '6': 'Jul',
    '7': 'Aug',
    '8': 'Sep',
    '9': 'Oct',
    '10': 'Nov',
    '11': 'Dec'
}

date_checkpoint = '20170000'
ts_key = '3'
new_dates = []




'''
INTRO:
Getting csv file from zip and openning to read the content 

'''

# read the content from Zipfile
with ZipFile(source_path, "r") as zipfile:
    # Determine elements inside the zipfile to know which one select 
    names_list = zipfile.namelist()
    #print(names_list)

    # Extracting the csv file
    csv_file_path = zipfile.extract(names_list[1], path=dirpath)
    
    # opening the csv file by specifying
    with open(csv_file_path, 'r', encoding="utf8") as csv_file:
    # creating an object of csv reader
    # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter = ',')
        # Getting header to visualize the structure of the columns 
        header = next(csv_reader)
        #print(header)
        '''
        QUESTION 3:
        For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?
            
        '''
        # First lets filter by tradeSignificance 3 and then lets filter by year, just records from 2017
        for row in csv_reader:
            trade_date = row[-14]
            month = trade_date[-4:-2]   
            trade_significance = row[-4]
            if trade_significance == ts_key:
                if trade_date > date_checkpoint:
                    new_dates.append(month)


# Total of transactions
total_trnsc = len(new_dates)

print('List of the percentage of transactions with tradeSignificance 3 by each month  of 2017: ')

for x in range(12):
    str_x = str(x)
    month_name = months[str_x] # str
    if x < 10: 
        month = "0"+str_x
    else:
        month = str_x
    amount = new_dates.count(month) # int
    prctg = round((amount/total_trnsc)*100, 2) # float
    print(f'{month_name}, {prctg} %')










