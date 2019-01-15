#! python3
# imageSiteDownloader.py
'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that has
a search feature.
'''

import requests, bs4, os, pprint, re
os.chdir('C:\\Users\\Mack W\\Documents\\Python\\automateTheBoringStuffWithPython\\Chapter 11 Web Scraping\\Practice Projects')
url = re.compile(r'c1.*\.jpg')

# Which image site
print('Website: ', end='')
website = input().lower()
# Which category
print('Search: ', end='')
search = input().lower()

path = os.getcwd() + '\\' + search + '.txt'

# Request site
if os.path.isfile(path) == False:
    if website == 'flickr':
        res = requests.get('https://www.flickr.com/search/?text=%s' % search)

    elif website == 'imgur':
        res = requests.get('https://imgur.com/search?q=%s' % search)

    elif website == 'instagram':
        print('Instagram')

    else:
        print('It has to be either: flickr, imgur, or instagram.')
        print('Please run the program again.')
    res.raise_for_status()
    # Write html to file
    file = open('%s.txt' % search, 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()

# Create beautiful soup object
file = open('%s.txt' % search)
soup = bs4.BeautifulSoup(file, features="lxml")
if os.path.isdir(search) == False:
    os.makedirs(search)
os.chdir(search)

if website == 'flickr':
    elems = soup.select('div[class="view photo-list-photo-view requiredToShowOnServer awake"]')
    for i in range(len(elems)):
        # find image url
        mo = url.search(elems[i].get('style'))
        res = requests.get('http://'+ mo.group())
        res.raise_for_status()
        # Save image
        file = open('%d.jpg' % i, 'wb')
        for chunk in res.iter_content(100000):
            file.write(chunk)
        file.close()

elif website == 'imgur':
    elems = soup.select('')

elif website == 'instagram':
    elems = soup.select('')

    


