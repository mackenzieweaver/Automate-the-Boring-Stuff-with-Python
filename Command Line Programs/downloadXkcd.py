#! python3
# downloadXkcd.py - Dowloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'     # starting url
os.chdir('C:\\Users\\Mack W\\Documents\\Python\\' +
         'automateTheBoringStuffWithPython\\' +
         'Chapter 11 Web Scraping\\XKCD Comics')
while not url.endswith('#'):
    # Download the page
    print('Page: ', end='')
    print(url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        
    # Download the image
    print('Image: ', end='')
    print(comicUrl)
    res = requests.get(comicUrl)
    res.raise_for_status()
    
    # Save the image
    imageName = os.path.basename(comicUrl)
    imageFile = open(imageName, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
