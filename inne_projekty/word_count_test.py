#! python

import os

def help_func(filename):
  f = open(filename, 'r')
  word_dict = {}
  for line in f:
    m = line.split()
    for elm in m:
      elm = elm.lower()
      if elm in word_dict:
        word_dict[elm] += 1
      else:
        word_dict[elm] = 1
  f.close()
  return word_dict
  

def print_words_test(filename):
  m = help_func(filename)
  m = sorted(m.items(), key=lambda x: x[0])
  for key, value in m:
    print(key, value)
 


def print_top(filename):
  m = help_func(filename)
  k = sorted(m.items(), key=lambda x: x[1], reverse=True)
  for key, value in k[:10]:
    print(key)



filename = 'text_file.txt'

print_words_test(filename)
print('\nThe top 10 of most used words:')
print_top(filename)
