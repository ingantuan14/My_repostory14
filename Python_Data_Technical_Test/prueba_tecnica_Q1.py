import csv
# Import ZipFile class from zipfile module
from zipfile import ZipFile


# Files Path 
source_path = "C:/Users/Antonio Arana/proyecto_git/Python_Data_Technical_Test/Programming+Excercise (1).zip"
dirpath = "C:/Users/Antonio Arana/data_engineer"



# Seting variables

entries = []


# Question 1 - Determine the exchange with more transactions
def most_frequent(List):
    return max(set(List), key = List.count)

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
        QUESTION 1:
        What Exchange has had the most transactions in the file?

        '''
        # Looping and parsing: Getting the name and id from companies
        for row in csv_reader:
            exchange_name = row[-1]            
            entries.append(exchange_name)

        # Determine which exchange had most activity
        print('The exchange with most activity was' +'\n'+
        most_frequent(entries))


        




        