#! python
# remove_csv_header.py - Removes the header from all CSV files in the current
# working directory.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# looping through every file in the current (or given) working directory.
for csvFilename in os.listdir('./csvs'):
    if not csvFilename.endswith('.csv'):
        continue # skipping non-csv files
    print('Removing header from ' + csvFilename + '...')

    # reading the csv file in (skipping first row).
    csvRows = []
    csvFileObj = open(os.getcwd() + '\\csvs\\' + csvFilename)
    readerObj = csv.reader(csvFileObj)
    
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvRows_1 = []
    for row in csvRows:
        csvRows_1.append(str(row).replace(';', ','))
        #csvRows_1.append(''.join(row))
    csvRows_1.insert(0, "Date,Time,Total_Wind_Power(MWh)")
    csvFileObj.close()

    # writing out the csv file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows_1:
        csvWriter.writerow(row.split(','))
    csvFileObj.close()
