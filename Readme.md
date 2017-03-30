## Prerequisites 

### Mac
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

* brew install imagemagick
* brew install tesseract
* brew install ghostscript
* brew install poppler

### Ubuntu
* apt-get install poppler-utils
* apt-get install tesseract-ocr
* apt-get install imagemagick
* pip install pypdfocr

### To run
```
python pyocr.py <pdf file path> <txt file path>
```
