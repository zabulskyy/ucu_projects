from zip_processor import ZipProcessor
import os
import sys
from pygame import image
from pygame.transform import scale
from PIL import Image

class ScaleZip(ZipProcessor):
	def process_files(self):
		'''Scale each image in the directory to 640x480'''
		for filename in os.listdir(self.temp_directory):
			im = image.load(self._full_filename(filename))
			scaled = scale(im, eval(input('please set size (width, heigt) as in example: (1024,720): ').replace(' ',',')))
			image.save(scaled, self._full_filename(filename))

