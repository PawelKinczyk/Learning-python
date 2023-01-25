from pathlib import Path
import os

# Create paths

# Path('spam', 'baco', 'eggs')
# str(Path('spam', 'bacon', 'eggs'))

# Create batch of files

# my_files = ['accounts.txt', 'work.txt', 'job.txt']
# for file in my_files:
#     print(Path(r'C:\User\Al', file))

# Merge paths

# Path('spam') / 'bacon' / 'eggs'
## Unsafe version because this path could work only on win

# home = r'C:\Users\Al'
# sub_folder = 'work'
# dir_folder = home + "\\" + sub_folder
# print(dir_folder)

## Version working everywhere

# home = Path('C:/Users/Al')
# sub_folder = Path('work')
# dir_folder = home / sub_folder
# print(dir_folder)
# str(home / sub_folder)

# Change curent directory

# Path.cwd()
# os.chdir('C:\\Windows\\System32')
# Path.cwd()

# Path.home()

# Relative and absolute path
# ..\ -before folder
# .\ - next folder

# Creating folders

# os.makedirs('C:\\delicious\\walnut\\waffles')

# Veryfication paths

# Path.cwd().is_absolute()
# os.path.abspath('.')
# os.path.abspath('.\\Scripts')
# os.path.isabs('.')

# Path options

# p = Path('C:/Users/Al/spam.txt')
# p.anchor
# p.parent
# p.stem
# p.suffix
# p.drive

# Path.cwd().parents[0] # get previous folder

# The same with os.dir

# dir ='C:\\Windows\\Sys\\text.txt'
# os.path.basename(dir)
# os.path.dirname(dir)

# Finding file sizes and folder content

# os.path.getsize(os.getcwd())

# List of size
# p = Path('C:/Users/pawel/Documents/GitHub/Learning-python')
# list = [p.glob('*')]
# print(list[0])
# list(p.glob('*.txt'))

# for file in p.glob('*'):
#     print(file)

# Checking and path validation
# list = []
# list.append(Path('C:/Windows'))
# list.append(Path('C:/This/Folder/Does/Not/Exist'))
# list.append(Path('C:/Windows/you'))

# for path in list:
#     path.exists()
#     path.is_dir()

# Opening Files with the open() Function
p = Path('C:/Users/pawel/Documents/GitHub/Learning-python/Automated_Boring_Tasks_With_Python')
text_file= open(p / 'text.txt')
text_content = text_file.read()
text_content

text_file.readlines()

# Writing to files
write_text = open('C:/Users/pawel/Documents/GitHub/Learning-python/Automated_Boring_Tasks_With_Python/write_text.txt', 'w') # if file doesnt exist it will create it
write_text.write("Hi all i am PAwel\n") # write something
write_text.close() # close file