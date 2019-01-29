#! python
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to
# European DD-MM-YYYY

import shutil, os, re

os.chdir('C:\\Users\\14000322\\Desktop')

# creating regex matching files with American date format
datePattern = re.compile(r"""^(.*?) # all text before the date (?-nongreedy)
                    ((0|1)?\d)-     # one or two digits for the month
                    ((0|1|2|3)?\d)- # one or two digits for the day(from 01 to 31)
                    ((19|20)\d\d)   # for digits for the day
                    (.*?)$          # all text after the date
                    """, re.VERBOSE)


# looping over the files in the working directory
for amerFilename in os.listdir('.'): # ('.') means current directory
    mo = datePattern.search(amerFilename)

    # skipping files without a date
    if mo == None:
        continue
    # getting the different parts of the filename; groups:3,5,7 are brackets inside 2,4,6
    beforePart = mo.group(1)
    monthPart = mo.group(2) 
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    # forming the European-style filename
    euroFilname = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart


    # getting the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # renaming the files
    print('Renaming {} to {}...'.format(amerFilename, eurofilename)) # to see what's going on
    # shutil.move(amerFilename, euroFilename) # uncomment if it works



