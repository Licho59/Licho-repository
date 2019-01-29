#! python 3
# selective_copy.py - finds and copies to separate folder files with .jpg and .pdf extensions
import os, shutil

folder_path = 'D:\\PYTHON\\Nauka'
backup_folder = 'C:\\Users\\14000322\\Desktop\\backup_folder'


for folderName, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.jpg') or filename.endswith('.pdf'):
            filename = os.path.join(os.path.abspath(folderName), filename)
            shutil.copy(filename, backup_folder)
            
