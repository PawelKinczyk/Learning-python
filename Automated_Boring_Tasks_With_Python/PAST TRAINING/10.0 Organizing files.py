import shutil
import os
from pathlib import Path

# # Copying files and folders

# p = Path('C:/Users/pawel/Documents/GitHub/Learning-python/Automated_Boring_Tasks_With_Python/')
# shutil.copy(p / 'text.txt', p / 'folder_1') # copy file to folder
# shutil.copy(p / 'text.txt', p / 'folder_1/text_copy.txt') # copy file and change name
# shutil.copytree(p / 'folder_1', p / 'folder_1__backup') # copy whole folder

# # Moving and renaming files&folders

# shutil.move(p / 'ddd.txt', p / 'folder_1') # move files to other folder

# # Deleting files

# os.link() # deleting file 
# os.rmdir() # deleting folder
# shutil.rmtree() # deleting folder and all inside

# shutil.rmtree(p / 'folder_1__backup')

# # Safe delete with send2trash

# import send2trash

# send2trash.send2trash() # send file to trash bin

# # "walking" in directory tree

# # create some folders
# for i in range(3):
#     p = 'C:/Users/pawel/Documents/GitHub/Learning-python/Automated_Boring_Tasks_With_Python/{}/{}.txt'.format(i,i)
#     os.makedirs(p)

# # batch going by folders
# for folderName, subfolders, filenames in os.walk('C:/Users/pawel/Documents/GitHub/Learning-python/Automated_Boring_Tasks_With_Python'):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)

#     print('')

# # Working with zip files

# import zipfile

# p = Path('C:/Users/pawel/Documents/GitHub/Learning-python/Automated_Boring_Tasks_With_Python/')
# zip_path = zipfile.ZipFile(p / 'Automate_the_Boring_Stuff_2e_onlinematerials.zip')
# zip_path.namelist()
# zip_info = zip_path.getinfo('automate_online-materials/allMyCats1.py')
# zip_info.file_size
# zip_info.compress_size

# f'Compressed file is {round(zip_info.file_size / zip_info.compress_size, 2)}x smaller!'

# zip_path.extractall() # extract all
# zip_path.extract('spam.txt', 'C:\\some\\new\\folders') # extract only one file

# # Adding to zip

# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()

ended - Create a Regex for American-Style Dates