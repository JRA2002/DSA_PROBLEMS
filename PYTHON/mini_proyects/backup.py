import shutil
import os
import datetime
import time
import schedule

source_dir = "/Users/javier/Desktop/PYTHON_PROBLEMS/photos"
dest_dir1 = "/Users/javier/Desktop/PYTHON_PROBLEMS/photos_backup"

def copy_data(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
    except FileExistsError:
        print(f'Folder already exist in : {dest}')
    

copy_data(source_dir,dest_dir1)