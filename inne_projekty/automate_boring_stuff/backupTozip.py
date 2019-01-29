#! python
# backupToZip.py - Copies an entire folder and its contents into a Zip file
# whose filename increments.

import zipfile, os

def backupToZip(folder):
    # backup the entire contents of 'folder' into a ZIP file
    folder = os.path.abspath(folder) # make sure folder's path is absolute

    number = 1
    while True:
        # zipFilename will have the name of the last folder of abspath
        inne_projekty = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(inne_projekty):
            break
        number = number + 1 # while loop works until it does not find path with new number


    # creating the ZIP file
    print('Creating {}...'.format(inne_projekty))
    backupZip = zipfile.ZipFile(inne_projekty, 'w')
    

    # walking through the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        # adding the current folder to the ZIP file
        backupZip.write(foldername)

        # adding all the file in this folder to the Zip file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()

    print('Done.')
    
backupToZip('C:\\Users\\14000322\\Documents\\Pliki Pythona\\Licho-repository\\inne_projekty')

