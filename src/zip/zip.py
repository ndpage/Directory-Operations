import shutil
from os.path import exists
import sys

def zip_dir(dir):
    
    try:
        dir = str(dir)
        shutil.make_archive(dir, 'zip', dir)
        zipped = exists(dir+'.zip')

    # Basic error handling for displaying the error number and message
    except OSError as err:
        print(">>   OS error: {0}".format(err))
        zipped = False
        
    return zipped

zip_dir('C:/test')