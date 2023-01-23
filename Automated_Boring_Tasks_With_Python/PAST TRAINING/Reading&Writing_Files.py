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

Path.cwd()
os.chdir('C:\\Windows\\System32')
Path.cwd()

Path.home()

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

dir ='C:\\Windows\\Sys\\text.txt'
os.path.basename(dir)
os.path.dirname(dir)


