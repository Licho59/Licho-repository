# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:33:23 2017

@author: Leszek
"""
# from XIII lectur on MIT - retirement savings scenarios
def retire(monthly, rate, terms):
    '''Counting the compound interests'''
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]

    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    '''Displaying saving results vs month payments.'''
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')
        
displayRetireWMonthlies([500, 600, 700, 800, 900,
                         1000, 1100], .05, 40 * 12)
        