import Image
import pytesseract
from sys import argv

script, filename = argv
text = pytesseract.image_to_string(Image.open(filename))

lines = text.split('\n')
phone = 0
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def isPhone(n):
    num = ""
    for i in n:
        if((i != "+") or (i != " ")):
            num+=i
    print num
    return num

for line in lines:
    num = line.replace("+", "")
    num2 = num.replace(" ", "")
    if(isNumber(isPhone(num2))):
        phone = line

print lines
print phone
