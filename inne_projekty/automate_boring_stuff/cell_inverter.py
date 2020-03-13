# cell_inverter.py - a program to invert the row and column of the cells in the spreadsheet

import sys, openpyxl

# name of spreadsheet to be inverted
name = sys.argv[1]

print('Reading a spreadsheet...')
wb = openpyxl.load_workbook(name)
sheet = wb.active
max_row = sheet.max_row
max_col = sheet.max_column
print(max_row, max_col)
rows = []
for row in range(1, max_row+1):
    data = []
    for cell in range(1, max_col+1):
        cell_value = sheet.cell(row=row, column=cell).value
        data.append(cell_value)
    rows.append(data)

print('Inverting cells in spreadsheet....')
wb = openpyxl.Workbook()
sheet = wb.active

for row in range(1,max_col+1):
    for cell in range(1, max_row+1):
        sheet.cell(row=row, column=cell).value = rows[cell-1][row-1]
        

wb.save('invert-'+name)
print("Inverted spreadsheet has been saved as 'invert-spreadsheet_name' at the same folder.")
