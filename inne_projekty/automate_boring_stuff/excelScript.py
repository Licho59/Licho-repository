# excelSript.py - some training about Excel2003 and older with spreadsheet
# extensions '.xls', using Python libray - 'xlwt'

import xlwt

def main():
    '''Function creates a blank 'xls' file, writes something
        and saves it to the file.'''
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1')

    sheet.write(0, 0, 'sample') # this will write 'sample' on zeroth row and zeroth column

    book.save('Sample.xls')

if __name__ == '__main__':
    main()
