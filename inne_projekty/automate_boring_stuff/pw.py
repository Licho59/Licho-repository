# Project: Password Locker
#! python 3
# pw.py - An insecure password locker program

PASSWORD = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}
# storing the command line arguments in variable sys.argv
import sys, pyperclip
if len(sys.argv) < 2: # checking if after the file name('pw.py) is mandatory argument
                        # with account name(for which I want to have reminded password
    # warning for user if he forgot to add second argument
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS[account]:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    

