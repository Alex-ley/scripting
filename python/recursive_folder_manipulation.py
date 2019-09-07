import os
from shutil import copy2, move
import fnmatch #could also use re (regular expression)
import multiprocessing as mp
import timeit

def manipulate_folder(dir,manipulate_type,file_match,destination_dir=None,multiprocessing=False):
    """
    A function to manipulate a given folder and its subfolders
    ____________________
    Positional arguments:
      dir: directory to be investiaged
      manipulate_type: 'delete', 'copy', 'move' or 'find'
      file_match: Unix filename pattern matching - https://docs.python.org/3.7/library/fnmatch.html
      destination_dir: default=None, only required if copying or moving files
      multiprocessing: true or false
      _PLANNED_ match_folders: true, false. true would also copy/move/delete folders that match
    """
    r = []
    index = 0
    _manipulate_current_folder(dir,manipulate_type,file_match,destination_dir,multiprocessing,r,index)
    print(r)
    print(len(r))

def _manipulate_current_folder(dir,manipulate_type,file_match,destination_dir,multiprocessing,r,index):

    for root, dirs, files in os.walk(dir):
        for name in files:
            if fnmatch.fnmatch(name, file_match):
                if manipulate_type.lower() == 'delete':
                    os.remove(os.path.join(root, name))
                elif manipulate_type.lower() == 'copy':
                    if destination_dir != None:
                        copy2(os.path.join(root, name),destination_dir)
                    else:
                        print('You need to specify a destination_dir')
                        return r
                elif manipulate_type.lower() == 'move':
                    if destination_dir != None:
                        move(os.path.join(root, name),destination_dir)
                    else:
                        print('You need to specify a destination_dir')
                        return r
                elif manipulate_type.lower() == 'find':
                    pass
                else:
                    print('invalid manipulate_type')
                r.append(name)
        for folder in dirs:
            print(folder.encode("utf-8"))
            _manipulate_current_folder(folder,manipulate_type,file_match,destination_dir,multiprocessing,r,index+1)

    return r

if __name__ == '__main__':
    dir = r"C:\Users\alexander.ley\Downloads" #OneDrive-TMO\OneDrive - Thermo Fisher Scientific" #\Test\TestA"
    start = timeit.default_timer()
    manipulate_folder(dir,'find','*.csv',multiprocessing=False)
    stop = timeit.default_timer()
    execution_time = stop - start
    print(f"Time taken: {execution_time} seconds")
    # dir = r"C:\Users\alexander.ley\Documents"
    # destination_dir = r"C:\Users\alexander.ley\Downloads\Test"
    # manipulate_folder(dir,'copy','19Rev*.csv',destination_dir)
    # dir = r"C:\Users\alexander.ley\Documents"
    # destination_dir = r"C:\Users\alexander.ley\Downloads\Test"
    # manipulate_folder(dir,'move','19*.csv',destination_dir)
    # dir = r"C:\Users\alexander.ley\Downloads\Test"
    # manipulate_folder(dir,'delete','19*.csv')
