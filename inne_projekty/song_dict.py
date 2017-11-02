# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:10:56 2017

@author: Leszek
"""

# Analyse of song lyrics
def lyrics_to_frequencies(lyrics):
    '''Creates a dictionary of words in the lyrics with their
    frequency number of appearance.'''
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

all_my_loving = ['Close', 'your', 'eyes', 'and', "I'll", 'kiss',
'you', 'Tomorrow', "I'll", 'miss', 'you', 'Remember', "I'll",
 'always', 'be', 'true', 'And', 'then', 'while', "I'm", 'away',
 "I'll", 'write', 'home', 'every', 'day', 'And', "I'll", 'send',
 'all', 'my', 'loving', 'to', 'you', "I'll", 'pretend', 'that',
 "I'm", 'kissing', 'The', 'lips', 'I', 'am', 'missing', 'And',
 'hope', 'that', 'my', 'dreams', 'will', 'come', 'true', 'And',
 'then', 'while', "I'm", 'away', "I'll", 'write', 'home', 'every',
 'day', 'And', "I'll", 'send', 'all', 'my', 'loving', 'to', 'you',
 'All', 'my', 'loving', 'I', 'will', 'send', 'to', 'you', 'All',
 'my', 'loving,', 'darling', "I'll", 'be', 'true', 'Close', 'your',
 'eyes', 'and', "I'll", 'kiss', 'you', 'Tomorrow', "I'll", 'miss',
 'you', 'Remember', "I'll", 'always', 'be', 'true', 'And', 'then',
 'while', "I'm", 'away', "I'll", 'write', 'home', 'every', 'day',
 'And', "I'll", 'send', 'all', 'my', 'loving', 'to', 'you', 'All',
 'my', 'loving', 'I', 'will', 'send', 'to', 'you', 'All', 'my',
 'loving', 'darling', 'I' 'will', 'be', 'true', 'All', 'my', 'loving,'
 'all', 'my', 'loving', 'ooh', 'All', 'my', 'loving', 'I', 'will',
 'send', 'to', 'you']

beatles = lyrics_to_frequencies(all_my_loving)

def most_common_words(freqs):
    '''Returns the tuple with the list of most frequent existing words
    in the dictionary with the integer showing the frequency'''
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    '''Returns list of the words occurying more often than minTimes.'''
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(beatles, 5))
            

