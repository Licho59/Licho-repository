# Fantasy game inventory

myInventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    count = 0
    print('Inventory:','\n')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k) + '\n')
        count += v
    print('Total number of items: ' + str(count))

displayInventory(myInventory)
