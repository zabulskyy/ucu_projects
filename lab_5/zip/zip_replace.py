from zip_processor import ZipProcessor
import os


class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.ex = ZipProcessor(filename)
        self.filename = filename
        self.temp_directory = str(filename[:-4])
        #super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string
        
    def process_files(self):
        '''perform a search and replace strings on all files in the temporary directory'''
        for filename in os.listdir(self.temp_directory):
            with open(self.ex._full_filename(filename).replace('unzipped-', '')) as file:
                contents = file.read()

            contents = contents.replace(self.search_string, self.replace_string)
            
            with open(
                self.ex._full_filename(filename).replace('unzipped-', ''), "w") as file:
                file.write(contents)
