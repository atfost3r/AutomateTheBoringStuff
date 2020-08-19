#! python3

# readCencusExcel.py - Tabulates population and the number of cencus tracts for each country

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('cencuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Cencus Tract')
countyData = {}

#TODO: Fill in countryData with each contry's population and tracts.
