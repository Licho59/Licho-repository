# update_prices.py - program is correcting prices for some products and updates data to new file

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')

sheet = wb.active

# counting total of sold products(revenue)
total_old, total_new = 0, 0

# looping over rows to find produces: 'Celery', 'Garlic' and 'Lemon'
# and update their present prices to new, respectively: 1.19, 3.07, 1.27
for row in range(2, sheet.max_row+1):
    total_old += round((sheet['B'+str(row)].value*sheet['C'+str(row)].value), 2)
   
    if sheet['A' +str(row)].value == 'Celery':
        sheet['B' + str(row)] = float(1.19)
    elif sheet['A' + str(row)].value == 'Garlic':
        
        sheet['B'+str(row)] = float(3.07)
    elif sheet['A' + str(row)] == 'Lemon':
        sheet['A'+str(row)] = float(1.27)

    total_new += round((sheet['B'+str(row)].value*sheet['C'+str(row)].value), 2)

print('The revenue lost because incorrect prices:', round((total_new - total_old), 2), 'dollars')
# saving to the new sheet
wb.save('produceSales_copy.xlsx')



                            
