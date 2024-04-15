import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

img = cv2.imread("images/Sample2.jpg")
img = cv2.resize(img, (600, 360))

# Preprocessing the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))

hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
with open("recognized.txt", "w") as fileobj:
    for b in boxes.splitlines():
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
        cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

        fileobj.write(b[0])

cv2.imshow('Detected text', img)
cv2.waitKey(0)
