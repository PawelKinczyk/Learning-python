# import webbrowser
# import sys
# import pyperclip

# Open web page -> very nice free source of knowledge

# webbrowser.open('https://inventwithpython.com/')

# Program to open adress from clipboard 

# if len(sys.argv) > 1:
#     ## Get address from command line
#     address = ' '.join(sys.argv[1:])
# else:
#     ## Get address from clipboard.
#     address = pyperclip.paste()

# webbrowser.open('https://www.google.com/maps/place/' + address, new=0) # You need to have opened browser

# Downloading Web page

# import requests

# download = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# type(download)

# download.status_code == requests.codes.ok # HTTP status more info https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# len(download.text)
# print(download.text[:50])

# ## See errors

# download = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#     download.raise_for_status() # !!! important, remember to check status after requests.get() to know that all is fine
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# ## Saving files fromm hard drive

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)

# playFile.close()

# Creating a beautifulSoup object from html

# import requests
# import bs4

# download = requests.get("https://www.wp.pl")
# print(download.content)
# download.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(download.text, 'html.parser')
# type(noStarchSoup)

# # there is few methods for select each elements in html

# web_soup = bs4.BeautifulSoup(download.content, 'html.parser')
# elements = web_soup.select('.beSrCx')
# len(elements)
# str(elements[0])
# elements[0].getText()
# elements[0].attrs
# elements[0].get('id')

# Working with selenium 

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Firefox()
# type(browser)
# browser.get('https://www.wp.pl/')

# ## Accept cookies

# # time.sleep(5)
# # linkElem = browser.find_element(By.CSS_SELECTOR, 'button.urpqq7t:nth-child(2)')
# linkElem = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div/button[2]') 
# type(linkElem)
# linkElem.click()

# ## Input in search 

# passwordElem = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/form/input')
# passwordElem.send_keys('PAWEL')
# passwordElem.submit()