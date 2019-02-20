import os
import shutil
import xlrd
import unidecode

comp_names = xlrd.open_workbook("comp_names.xlsx")

try:
    shutil.rmtree("Names")
finally:
    os.mkdir("Names")
    os.chdir("Names")
    
    # Iterate through sheets
    for index in range(0, comp_names.nsheets):
        
        # Make folder for current sheet
        curr_sheet = comp_names.sheet_by_index(index)
        os.mkdir(curr_sheet.name)
        os.chdir(curr_sheet.name)
        
        # Iterate through rows
        for row in range(curr_sheet.nrows):
            # Extract athlete's number, convert to 3 digits
            number = str(int(curr_sheet.cell(row,0).value))
            if len(number) == 1:
                number = "000" + number
            elif len(number) == 2:
                number = "00" + number
            elif len(number) == 3:
                number = "0" + number
            # Extract the athlete's name
            fname = unidecode.unidecode(curr_sheet.cell(row,1).value)
            lname = unidecode.unidecode(curr_sheet.cell(row,2).value)
            # Create folder for athlete
            fldr_name = "{0}-{1}-{2}".format(number, fname, lname)
            os.mkdir(fldr_name)
        os.chdir("..")
