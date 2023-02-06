import os
from pathlib import Path
import glob
from openpyxl import load_workbook

def list_to_string(list):
    str=''
    for i in list:
        str+=(i+' ')
    
    return str

def check_files(folder_path, file_path):
    # Get path files 
    print("sciezka folderu: "+folder_path)
    p = Path(folder_path)
    folder = p.glob('*')
    
    # Collect names inside folder
    print(p)
    file_list = []
    for i in folder:
        file_list.append(Path(i).stem)
        print("file list" + str(i))

    # Open excel file
    print("sciezka pliku: "+file_path)
    excel = load_workbook(filename=file_path)

    excel_sheet = excel['Arkusz1'] # Pick defaul worksheet

    # Get listed names of files

    excel_list =[]
    for i in excel_sheet['A']:
        excel_list.append(i.value)
        print(i.value)

    # Search for listed files in folder
    
    n=0
    print("To wartosc n " + str(n))
    for i in excel_list:
        n+=1
        sheet_cell = 'B{}'.format(n)
        if i in file_list:
            excel_sheet[sheet_cell] = "True"
        else:
            excel_sheet[sheet_cell] = "False"    

    # Return not listed files inside folder 

    m=n+1
    sheet_cell = 'B{}'.format(m)
    other_files = list(set(file_list) - set(excel_list))
    excel_sheet[sheet_cell] = list_to_string(other_files)

    # Overwrite excel 

    excel.save(filename=file_path)
    excel.close()