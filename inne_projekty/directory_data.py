#! python3.6
# directory_data.py - returns content of current working directory with additional data

from datetime import datetime
from os import scandir, getcwd

def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

def get_files():
    current_dir_name = getcwd()
    dir_entries = scandir(getcwd())
    print(f'The list of files and folders in {current_dir_name} folder:\n')
    for entry in dir_entries:
        info = entry.stat()
        print(f'{entry.name}'.ljust(40), f'Last modified: {convert_date(info.st_mtime)}')




if __name__ == '__main__':
    get_files()

