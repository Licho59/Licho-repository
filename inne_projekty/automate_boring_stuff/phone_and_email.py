#! python
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard.
# after copying some text to the clipboard(Ctrl-C) and running that script you should
# get info about result ready or not to paste into any place you want

import pyperclip, re

# creating phone numbers regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (optional)
    (\s|-|\.)?                      # separator (optional)
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# creating email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)

# finding the matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copying the results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) # all matches will be shown in vertical view
    print('Copied to clipboard:')
    print('\n.join(matches)')
else:
    print('No phone numbers or email addresses found.')
    
