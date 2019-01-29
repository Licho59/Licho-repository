#!python3

# table_printer.py - displays the aligned to right columns of words


def printTable(table):
    # list with length of longest word in each sublist - future column
    l_words = [max([len(k) for k in elm]) for elm in table]
    
    # printing words from original list in a way of a table
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(l_words[j], ' '), '  ', end='') 
        print()

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
    


printTable(tableData)
