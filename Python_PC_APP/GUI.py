import tkinter as tk
from PIL import ImageTk, Image
from function import check_files

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

root = tk.Tk()
root.maxsize(900,  600)
left_frame  =  tk.Frame(root,  width=200,  height=  400,  bg='grey')
left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

right_frame  =  tk.Frame(root,  width=650,  height=400,  bg='grey')
right_frame.grid(row=0,  column=1,  padx=10,  pady=5)

# Left

# frame_logo = tk.Frame(master=window, width = 280)

logo = Image.open("C:/Users/pawel/Documents/GitHub/Learning-python/Python_PC_APP/Image_Logo.png")
logo = logo.resize((200,240))
logo = ImageTk.PhotoImage(logo)

label_logo = tk.Label(master = left_frame, image=logo)
label_logo_text = tk.Label(master = left_frame, text="Paweł Kińczyk (c) My blog: https://produktywnyprojektant.com"
, wraplength=200, justify="center")
# label_logo.pack()
# label_logo_text.pack()

label_logo.grid(row=0, column=0,padx=10, pady=20)
label_logo_text.grid(row=3, column=0,padx=10, pady=20)

# Right
right_frame1 = tk.Frame(right_frame,  width=650,  height=100,  bg='grey')
right_frame1.grid(row=0,  column=0,  padx=10,  pady=15)

right_frame2 = tk.Frame(right_frame,  width=650,  height=100,  bg='blue')
right_frame2.grid(row=1,  column=0,  padx=10,  pady=5)

right_frame3 = tk.Frame(right_frame,  width=650,  height=100,  bg='green')
right_frame3.grid(row=2,  column=0,  padx=10,  pady=5)

right_frame4 = tk.Frame(right_frame,  width=650,  height=100,  bg='yellow')
right_frame4.grid(row=3,  column=0,  padx=10,  pady=5)

# Right1
label_path = tk.Label(right_frame1, text="Pick path to folder in which you want to check files")
folder_path = tk.StringVar()
folder_path.set("***Folder Path***")
label_path_picked = tk.Label(right_frame1, wraplength=250,textvariable=folder_path)
button_path = tk.Button(right_frame1, text="Browse", command=browse_button_folder)

label_path.grid(row=0,  column=0,  padx=5,  pady=5)
label_path_picked.grid(row=1,  column=0,  padx=5,  pady=5)
button_path.grid(row=2,  column=0,  padx=5,  pady=5)

root.mainloop()