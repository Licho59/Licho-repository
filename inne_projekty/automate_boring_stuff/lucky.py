# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display the text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='lxml')

# TODO: Open a browser tab for each result
# getting list of elements to open a browser tab for each result
linkElems = soup.select('.r a') # using selector('r. a') to find all <a> objects
                                # within an element that has the r CSS class

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    
