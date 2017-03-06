import os
import shutil
import zipfile
from pygame import image
from pygame.transform import scale


class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
    
    def scale_image(self):
        '''scale image'''
        for filename in os.listdir(self.temp_directory):
            im = image.load(self._full_filename(filename))
            scaled = scale(im, eval(input('please set size (width, heigt)'
                                          ' as in example: (1024,720): ').replace(' ',',')))
            image.save(scaled, self._full_filename(filename))

    def _full_filename(self, filename):
        '''return a correct path to directory'''
        return os.path.join(self.temp_directory, filename)
    
    def process_scale(self):
        self.unzip_files()
        self.scale_image()
        self.zip_files()

    def unzip_files(self):
        '''extract files from zip'''
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()
            
    def zip_files(self):
        '''zip files and remove created directory'''
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)
