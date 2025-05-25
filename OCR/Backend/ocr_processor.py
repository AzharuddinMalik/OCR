import cv2
import pytesseract
from resize import image_resize

pytesseract.pytesseract.tesseract_cmd = r'F:\Download\tesseract.exe'


def process_image(image_path):
    img = cv2.imread(image_path)
    img = image_resize(img, 800, 800)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Your existing processing logic
    ret, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Perform OCR
    text = pytesseract.image_to_string(th1)
    return text