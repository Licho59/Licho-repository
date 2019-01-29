'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string.

'''
import re

def regex_strip(text, rm_text=None):
    if rm_text == None:
        return text.strip()
    else:
        text = text.strip()
        text_regex = re.compile(rm_text)
        return text_regex.sub('', text)

if __name__ == '__main__':
    text = input('Enter a text: ')
    rm_text = input('Enter the string you want to remove from the text or just click enter: (Optional)')
    clean_text = regex_strip(text,rm_text)
    print(clean_text)
