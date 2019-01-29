#! python3
# bulletPointAdder.py - program adding bullets to the start of each line of text from
#Wikipedia Markup consists of: pasting text from the clipboar, doing work and copying back
# to clipboard - in purpose to paste it back to Wikipedia article for example

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # addin star to the beginning of the line
    
# joining list elements in one string - because of pyperclip expectation
text = '\n'.join(lines)

pyperclip.copy(text)
