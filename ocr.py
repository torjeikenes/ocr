import Image
import pytesseract
from sys import argv

script, filename = argv
text = pytesseract.image_to_string(Image.open(filename))

lines = text.split('\n')
print lines
