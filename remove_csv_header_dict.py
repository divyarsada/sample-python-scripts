#remove_csv_header_dict: removes the header from the csv files using DictReader and DictWriter objects of csv
import csv
import os
import glob
#creating the directory
try:
    os.mkdir('./remove_csv_header')
except OSError:
    print("Directory exist")

#creating a empty dict
csvRows={}

#fetching all the csv filenames in the current directory 
csvfiles=glob.glob('*.csv')

#iterating through the csv files, reading the rows from one file and copying it to new file without header
for csvfile in csvfiles:
   csvReadFile = open(csvfile)
   csvWriteFile = open(os.path.join('./remove_csv_header',csvfile),'w')
   csvDictReaderObject=csv.DictReader(csvReadFile)
   for row in csvDictReaderObject:
       #print(row)
       csvDictwriter = csv.DictWriter(csvWriteFile,["Item","Tax Status","Employer Status"])
       csvDictwriter.writerow(row)
   csvReadFile.close()
   csvWriteFile.close()

