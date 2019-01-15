#! python3
# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

search = ' '.join(sys.argv[1:])

#res = requests.get('http://google.com/search?q=' + search)
#res.raise_for_status()
print(search)

# Retrieve top search result links
#soup = bs4.BeautfilfulSoup(res.text)

# Open a browser tab for each result
#linkElems = soup.select('.r a')
#for i in range(5):
    #print(str(linkElems[i].get('href'))
    #webbrowser.open('http://google.com' + linkElems[i].get('href'))
