import shutil
from os.path import exists



def zip_dir(dir):
    dir = str(dir)
    shutil.make_archive(dir, 'zip', dir)

    file_exists = exists(dir+'.zip')

    return file_exists
