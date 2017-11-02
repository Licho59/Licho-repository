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
        
def displayRetireWRates(month, rates, terms):
    '''Displaying saving results vs rate.'''
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(month) +
                 ':' + str(int(rate*100)))
    plt.legend(loc = 'upper left')
    
def displayRetireWMonthsAndRates(monthlies, rates, terms):
    '''Displaying saving results with both month and rate.'''
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel,
                label = 'retire:' + str(monthly) + ':' + str(int(rate*100)))
    plt.legend(loc = 'upper left')
               
#==============================================================================
# displayRetireWMonthlies([500, 600, 700, 800, 900,
#                          1000, 1100], .05, 40*12)
#==============================================================================
#==============================================================================
# displayRetireWRates(800, [.03, .05, .07], 40*12)
#==============================================================================
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)     