import cv2
import pytesseract
import platform
import os
from .resize import image_resize


# Configure Tesseract path based on operating system
def configure_tesseract():
    system = platform.system()

    if system == "Windows":
        # Windows path (your local development)
        possible_paths = [
            r"F:\Download\tesseract.exe",
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Users\{}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe".format(os.getenv('USERNAME', ''))
        ]

        for path in possible_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                break
    else:
        # Linux/Unix systems (including Render)
        # Tesseract should be in PATH after installation
        pytesseract.pytesseract.tesseract_cmd = 'tesseract'


# Call this function at the start of your OCR processing
configure_tesseract()


def process_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Could not read image from {image_path}")

        img = image_resize(img, 800, 800)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Your existing processing logic
        ret, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

        # Perform OCR
        text = pytesseract.image_to_string(th1)
        return text
    except Exception as e:
        raise Exception(f"OCR processing failed: {str(e)}")