import PIL.ImageShow
from pytesseract import Output
import sys
sys.path.append("C:\Program Files (x86)\Tesseract-OCR")
import pytesseract
from PIL import Image
import numpy as np
import cv2




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    poza1 = 'poza1.jpg'
    poza2 = 'poza2.jpg'
    poza3 = 'Capture.PNG'
    poza4 ='Capture4.PNG'
    poza5 = 'Capture6.PNG'

    img1 = cv2.imread(poza4,cv2.IMREAD_GRAYSCALE)
    ##img1 = cv2.blur(img1, (5, 5))


    cv2.imshow('image window', img1)
    cv2.waitKey(0)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    ##text = pytesseract.image_to_string(poza2)
    text1= pytesseract.image_to_string(img1, lang='lets', config='--psm 6 -c tessedit_char_whitelist="0123456789"')
    print(text1)
    cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
