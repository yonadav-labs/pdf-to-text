import os
import  sys


class TextImageFile(object):
    def __init__(self, pdf_path, txt_path):
        self.pdf_path = pdf_path
        self.txt_path = txt_path

    # @property
    def extract(self):
        if not os.path.exists(self.pdf_path):
            print "PDF file path is not correct!"
            return None

        self.get_text_from_pdf(self.pdf_path)
        if len(self.text) < 10: # image based PDF
            print 'Start OCR...'
            ocr_path = '{}_ocr.pdf'.format(self.pdf_path[:-4])
            os.system("pypdfocr {} > /dev/null".format(self.pdf_path))
            self.get_text_from_pdf(ocr_path)
            os.remove(ocr_path)

        # write result to file
        with open(self.txt_path, 'w') as f:
            f.write(self.text)


    def get_text_from_pdf(self, path):
        """
        Read PDF file as text
        """
        os.system("pdftotext {} tmp.txt > /dev/null".format(path))
        with open('tmp.txt') as f:
            self.text = f.read()
        os.remove('tmp.txt')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "usage: pyocr <pdf file path> <txt file path>"
        exit()
    elif sys.argv[1][-4:] != '.pdf':
        print 'Please provide only pdf file as input'
        exit()

    tif = TextImageFile(sys.argv[1], sys.argv[2])
    tif.extract()
