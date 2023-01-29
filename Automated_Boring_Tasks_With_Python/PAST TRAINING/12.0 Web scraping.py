import webbrowser
import sys
import pyperclip

# Open web page -> very nice free source of knowledge

# webbrowser.open('https://inventwithpython.com/')

# Program to open adress from clipboard 

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address, new=0) # You need to have opened browser