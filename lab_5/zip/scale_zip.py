from zip_processor import ZipProcessor


class ScaleZip():

    def process_scale(self, zipname):
        '''Perform scaling and saving file'''
        ex = ZipProcessor(zipname)
        ex.process_scale()
