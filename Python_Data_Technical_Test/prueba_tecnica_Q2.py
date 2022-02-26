import csv
# Import ZipFile class from zipfile module
from zipfile import ZipFile


source_path = "C:/Users/Antonio Arana/proyecto_git/Python_Data_Technical_Test/Programming+Excercise (1).zip"
dirpath = "C:/Users/Antonio Arana/data_engineer"

# Seting Variables
value_aug = {}
num = 1
q2_datecheckpoint = '201708'


# Question 2 - Finding the MAX value in  a dictionary
def max_dict(Dict):
    max_key = max(Dict, key= Dict.get)
    return max_key


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
        QUESTION 2
        In August 2017, which companyName had the highest combined valueEUR?

        '''
        for row in csv_reader:
            company_name = row[2]
            trade_date = row[-14]
            date = trade_date[:-2] 
            valueEUR = float(row[-8])
            if date == q2_datecheckpoint:
                value_aug[num] = [company_name, valueEUR]
            num += 1

#print(len(value_aug))
#print(value_aug[37548])
total_valaug = {}

for x in value_aug.values():
    if x[0] not in total_valaug:
        total_valaug[x[0]] = x[1]
    else:
        total_valaug[x[0]] + x[1]


#print(total_valaug.values())

# How to find the max value in a dictionary in Python
# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python

result_2 = max_dict(total_valaug)
print(result_2)



       
            















