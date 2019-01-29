import timeit
"""All three functions count only the minimum number of coins needed to make change - but they do not keep track of coins used for making change."""

def recMC(coinValueList, change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList, change - i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins
   

def recDC(coinValueList, change, knownResults):
   '''It remembers counted change values in purpose to avoid repetitive counting; knownResults given as the list with all values = 0 and length equal to given parameter 'change'.'''
   
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change - i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins

   return minCoins

def dpMakeChange(coinValueList,change,minCoins):
    '''minCoins is initially a list of 'change +1' length with all values equal to 0; due to for loop the list fulfills with values of minimum coins needed to change given amount of money(change)'''
   for cents in range(change+1):
      coinCount = cents #initially number of coins for given change (in cents)
      for j in [c for c in coinValueList if c <= cents]: #list of valid coins 
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]


slow = timeit.Timer(
    "recMC([1, 5, 10, 25], 63)", "from __main__ import recMC")
print("slow change counted only 1 time: ", slow.timeit(number=1), "seconds")

fast = timeit.Timer(
    "recDC([1, 5, 10, 25], 63, [0] * 64)", "from __main__ import recDC")
print("fast change counted 1000 times: ", fast.timeit(number=1000), "seconds")

fastest = timeit.Timer("dpMakeChange([1, 5, 10 ,25], 63, [0]*64)", "from __main__ import dpMakeChange")
print("dynamic change algorithm counted 1000 times: ", fastest.timeit(number=1000), "seconds")
