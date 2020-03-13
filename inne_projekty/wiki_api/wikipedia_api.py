# wikipedia_api.py - a few examples of using 'wikipedia' python library to search and get data from Wikipedia page

import urllib.request
import wikipedia

wikipedia.set_lang('en')
#print(wikipedia.summary('facebook', sentences=10))
print('--------------------------------')



#print(wikipedia.summary('Amazon, rivers, sentences=1'))

#print(wikipedia.page('Google').content)

#print(wikipedia.page('Amazon Company').url)

page_image = wikipedia.page('Google')
image_down_link = page_image.images[2]
#urllib.request.urlretrieve(image_down_link, 'loc_2.jpg') # loc.jpg - name given to the link
#print(len(page_image.images))
#for image in page_image.images:
 #   print(image)
 
page_title = wikipedia.page('Indian Demographic')
print(page_title.title)