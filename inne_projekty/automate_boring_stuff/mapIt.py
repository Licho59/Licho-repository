# 'mapIt.py' - program launches a map in webbrowser using the address
# from the command line or clipboard

import webbrowser, pyperclip, sys

if len(sys.argv) > 1:
    # get the address from command line
    address = ' '.join(sys.argv[1:]) # it takes all strings after argument 1
else:
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

