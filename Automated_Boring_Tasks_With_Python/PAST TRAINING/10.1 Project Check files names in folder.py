import os
from pathlib import Path
import glob
from openpyxl import load_workbook

# def / class

def list_to_string(list):
    str=''
    for i in list:
        str+=(i+' ')
    
    return str

# Get path files 

p = Path('C:/Users/pawel/Desktop/FOLDER_1') # path to check files
folder = p.glob('*')

# Collect names inside folder

file_list = []
for i in folder:
    file_list.append(Path(i).stem)
    print(i)

# Open excel file

excel = load_workbook(filename="C:/Users/pawel/Desktop/FOLDER_1/Nowy folder/pyth prog.xlsx")

excel_sheet = excel['Arkusz1'] # Pick defaul worksheet

# Get listed names of files

excel_list =[]
for i in excel_sheet['A']:
    excel_list.append(i.value)
    print(i.value)

# Search for listed files in folder

n=0
for i in excel_list:
    n+=1
    sheet_cell = 'B{}'.format(n)
    if i in file_list:
        excel_sheet[sheet_cell] = "True"
    else:
        excel_sheet[sheet_cell] = "False"    

# Return not listed files inside folder 

n+=1
sheet_cell = 'B{}'.format(n)
other_files = file_list = excel_list
excel_sheet[sheet_cell] = list_to_string(other_files)

# Overwrite excel 

excel.save(filename="C:/Users/pawel/Desktop/FOLDER_1/Nowy folder/pyth prog.xlsx")
excel.close()