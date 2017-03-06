from scale_zip import *
from zip_replace import *
'''
## scale_zip ##
if __name__ == "__main__":
    ScaleZip().process_scale(input("please, type zip-file name: ").replace('.zip','') + '.zip')

## zip_replace ##
if __name__ == "__main__":
    ZipReplace(input("please, type a directory name: ").replace('.zip','') +
               '.zip', input('which string should be removed?: '),
               input('which string should be instead?: ')).process_files()
'''