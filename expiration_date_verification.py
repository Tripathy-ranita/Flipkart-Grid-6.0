from PIL import Image
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re
from datetime import datetime
import cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Tk().withdraw()

file_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])


def preprocess_image(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    processed_image_path = 'processed_image.jpg'
    cv2.imwrite(processed_image_path, thresh)

    return processed_image_path



def find_expiry_date(text):    
    date_pattern = r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2}|\d{1,2} \d{1,2} \d{2,4}|\d{4} \d{1,2} \d{1,2})'

    expiry_terms = ['expiry', 'expires', 'exp', 'use by', 'exp date']

    for line in text.split('\n'):
        if any(term in line.lower() for term in expiry_terms):
            match = re.search(date_pattern, line)
            if match:
                expiry_date = match.group(0)
                return expiry_date

    return None



def is_expired(expiry_date_str):
    date_formats = ['%d/%m/%Y', '%d %m %Y', '%Y/%m/%d', '%Y %m %d']

    for date_format in date_formats:
        try:
            expiry_date = datetime.strptime(expiry_date_str, date_format)
            break
        except ValueError:
            continue
    else:
        return False

    current_date = datetime.now()
    return expiry_date < current_date



if file_path:
    processed_image_path = preprocess_image(file_path)
    image = Image.open(processed_image_path)
    extracted_text = pytesseract.image_to_string(image)
    print("Extracted Text:\n", extracted_text)
    expiry_date_str = find_expiry_date(extracted_text)

    if expiry_date_str:
        print("Expiry Date Found:", expiry_date_str)
        if is_expired(expiry_date_str):
            print("This product has expired.")
        else:
            print("This product is not expired.")
    else:
        print("No expiry date found.")
else:
    print("No file selected.")
