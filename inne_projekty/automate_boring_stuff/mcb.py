#! python
#mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: python.exe mcb.pyw save <keyboard> - Saves clipboard to keyword
#       python.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       python.exe mcb.pyw list - Loads all keywords to clipboard


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'cls':
        del mcbShelf[sys.argv[2]]
        
elif len(sys.argv) == 2:
    #  list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(str(mcbShelf[sys.argv[1]]))
    
    elif sys.argv[1].lower() == 'cla':
        mcbShelf.clear()
        
        

mcbShelf.close()
