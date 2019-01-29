#! python3
# del_unneeded_files.py - finding files which are not needed

import os, shutil, send2trash

folder = 'C:\\Users\\14000322\\Desktop\\backup_folder'

#folder = 'D:\\PYTHON\\Nauka'

deleted_files = []
for folderName, subfolders, filenames in os.walk(folder):
    print('The current folder is ', folderName, '\n')
    print('Files bigger than 2 MB will be deleted:')
    for filename in filenames:
        file = os.path.join(os.path.abspath(folderName), filename)
        if os.path.getsize(file) > 2000000:
            print(file + ': ' + str(os.path.getsize(file)))
            deleted_files.append(filename)
            send2trash.send2trash(file)
print('\nDeleted files:')
print(deleted_files)
            
