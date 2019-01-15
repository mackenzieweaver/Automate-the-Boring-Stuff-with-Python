#! python3
# linkVerification.py
'''
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links.
'''

# imports
import requests, bs4, os
directory = os.chdir('C:\\Users\\Mack W\\Documents\\Python\\automateTheBoringStuffWithPython\\Chapter 11 Web Scraping\\Practice Projects')

# Start page and name
print('url: ', end='')
url = input()
print('name: ', end='')
name = input()
res = requests.get(url)

# flag broken links
try:
    res.raise_for_status()
except Exception as exc:
    print('%s' % (exc))
    
# save website to file if it doesn't already exist
if os.path.isfile('%s.html' % name) == False:
    file = open('%s.html' % name, 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()
# if it does exist just read the file
file = open('%s.html' % name, 'rb')

# create soup object
soup = bs4.BeautifulSoup(file, features="lxml")

# find link elements
elems = soup.select('a')
for i in range(len(elems)):
    #print(elems[i].get('href'))
    extension = elems[i].get('href')
    # download each page
    if extension:
        if extension.startswith('/'):
            print(url + extension)
            res = requests.get(url + extension)
            # flag broken links
            try:
                res.raise_for_status()
            except Exception as exc:
                print('%s' % (exc))    
file.close()
