import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'F:\Download\tesseract.exe'
img = cv2.imread("static/images/img.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV)
plt.subplot(2, 2, 1)
plt.title("OTSU+BINARY INVERSION")
plt.imshow(th1)
plt.show()
cv2.waitKey(0)