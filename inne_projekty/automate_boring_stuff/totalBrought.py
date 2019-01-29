# counting the item numbers from many dictionaries
allGuests = {'Alice':{'apples':5, 'pretzels':12},
            'Bob':{'ham sandwiches': 3, 'apples': 2},
            'Carol':{'cups':3, 'appple pies': 1}}

def totalBrought(guests, item):
    itemCount = 0
    for k, v in guests.items():
        itemCount = itemCount + v.get(item, 0)
    return itemCount
print('Number of apples brought by guests: ' + str(totalBrought(allGuests, 'apples')))

      

        
