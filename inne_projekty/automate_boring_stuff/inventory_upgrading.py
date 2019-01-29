# adding dictionaries elements

def displayInventory(inventory):
    count = 0
    print('Inventory:','\n')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k) + '\n')
        count += v
    print('Total number of items: ' + str(count))


def addToInventory(inventory, addedItems):
    for elm in addedItems:
        inventory.setdefault(elm, 0)
        inventory[elm] += 1
    return inventory


inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
