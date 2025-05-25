import pytesseract
import platform
import os


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