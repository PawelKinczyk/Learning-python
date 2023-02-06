import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os
from pathlib import Path
import glob
from openpyxl import load_workbook

def browse_button_folder():

    global folder_path
    filename =fd.askdirectory()
    folder_path.set(filename)
    print(filename)
    

def browse_button_file():

    global folder_path
    filename =fd.askopenfilename(filetypes=(("excel file", "*.xlsx"), ("All files", "*.*"),))
    file_path.set(filename)
    print(filename)
    

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


window = tk.Tk()
logo = Image.open("C:/Users/pawel/Documents/GitHub/Learning-python/Python_PC_APP/Image_Logo.png")
logo = logo.resize((200,240))
logo = ImageTk.PhotoImage(logo)

# logo = tk.PhotoImage(file="C:/Users/pawel/Documents/GitHub/Learning-python/Python_PC_APP/Image_Logo.png")

# Program window
window.geometry('500x400')
window.title('Folder checker')

## Logo and text
frame_logo = tk.Frame(master=window, width = 280)
label_logo = tk.Label(master = frame_logo, image=logo)
label_logo_text = tk.Label(master = frame_logo, text="Paweł Kińczyk (c) My blog: https://produktywnyprojektant.com"
, wraplength=200, justify="center")
label_logo.pack()
label_logo_text.pack()

## Ask for folder path
frame_path = tk.Frame(master=window, width=150, bg="gray")

label_path = tk.Label(master = frame_path, text="Pick path to folder in which you want to check files")
folder_path = tk.StringVar()
folder_path.set("***Folder Path***")
label_path_picked = tk.Label(master=frame_path, wraplength=250,textvariable=folder_path)
button_path = tk.Button(master = frame_path, text="Browse", command=browse_button_folder)
# entry_path = tk.Entry(master = frame_path)

# frame_file = tk.Frame(master=window, width=150, bg="blue")

file_path = tk.StringVar()
file_path.set("***File Path***")
label_file_picked = tk.Label(master=frame_path, wraplength=250,textvariable=file_path)
button_file = tk.Button(master = frame_path, text="Browse", command=browse_button_file)

label_path.pack()
label_path_picked.pack()
button_path.pack()
# entry_path.pack()

label_excel = tk.Label(master = frame_path, text="Insert excel path which you want to check")
# entry_excel = tk.Entry(master = frame_path)
label_excel.pack()
# entry_excel.pack()
label_file_picked.pack()
button_file.pack()

## Run code

button_run = tk.Button(master = frame_path, text="Run", command= lambda: check_files(str(folder_path.get()),str(file_path.get())))
button_run.pack()

# Grid
# frame_file.grid(row=0,column=0)
# frame_path.grid(row=1,column=0)
## Show frames

frame_logo.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
frame_path.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


window.mainloop() # take program in loop
