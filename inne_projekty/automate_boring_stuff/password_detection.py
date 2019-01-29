'''
A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit.

You may need to test the string against multiple regex patterns to validate
its strength.
'''
import re

def password_detection(password):
    if re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password):
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        pw = input('Enter your password: ')
    
        if password_detection(pw):
            print('Good, your password is strong')
            break 
        else:
            print('The password must be at least 8 characters long and contain both lowercase and uppercase letters, and at least one digit')
    
        
