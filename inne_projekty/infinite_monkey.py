import random

def generate():
    check_text = ''
    for i in range(6):
        check_text += random.choice(alpha)
    return check_text
    
def score(check_text, sh_text):
    if check_text == sh_text:
        return 'True'
    '''else:
        print('Continue!')'''

def checking(n):
    while n > 0:
        check_text = generate()
        result = score(check_text, sh_text)
        if result is True:
            print('Text has been generated')
            break
        else:
            n -= 1
    
if __name__ == '__main__':
    sh_text = 'met ink'
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    print(checking(10000000))
     
    
     
    
        

