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
    folder_path_.set(filename)
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

    p = Path(folder_path)
    folder = p.glob('*')
    # Collect names inside folder

    file_list = []
    for i in folder:
        file_list.append(Path(i).stem)
        print(i)

    # Open excel file

    excel = load_workbook(filename=file_path)

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


window = tk.Tk()

logo = ImageTk.PhotoImage(Image.open("C:/Users/pawel/Documents/GitHub/Learning-python/Python_PC_APP/Image_Logo.png"))

# logo = tk.PhotoImage(file="C:/Users/pawel/Documents/GitHub/Learning-python/Python_PC_APP/Image_Logo.png")

# Program window
window.geometry('500x400')
window.title('Folder checker')

## Logo and text
frame_logo = tk.Frame(master=window, width = 200)
label_logo = tk.Label(master = frame_logo, image=logo)
label_logo_text = tk.Label(master = frame_logo, text="Paweł Kińczyk (c) My blog:https://produktywnyprojektant.com"
, wraplength=150, justify="center")
label_logo.pack()
label_logo_text.pack()

## Ask for folder path
frame_path = tk.Frame(master=window, width=150, bg="yellow")

label_path = tk.Label(master = frame_path, text="Pick path to folder in which you want to check files")
folder_path = tk.StringVar()
label_path_picked = tk.Label(master=frame_path,textvariable=folder_path)
button_path = tk.Button(master = frame_path, text="Browse", command=browse_button_folder)
entry_path = tk.Entry(master = frame_path)


file_path = tk.StringVar()
label_file_picked = tk.Label(master=frame_path,textvariable=file_path)
button_file = tk.Button(master = frame_path, text="Browse", command=browse_button_file)

label_path.pack()
label_path_picked.pack()
button_path.pack()
entry_path.pack()

label_excel = tk.Label(master = frame_path, text="Insert excel path which you want to check")
entry_excel = tk.Entry(master = frame_path)
label_excel.pack()
entry_excel.pack()
label_file_picked.pack()
button_file.pack()

## Run code

button_run = tk.Button(master = frame_path, text="Run", command= lambda: check_files(button_path.getvar(),button_file.getvar()))
button_run.pack()

## Show frames

frame_logo.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
frame_path.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop() # take program in loop
