#!python
#excel2csv.py - converts all the Excel files in the current working directory into a CSV file

import csv, openpyxl, os

for excelFile in os.listdir('.'):
    #skip non-xslx files, load the workbook object
    