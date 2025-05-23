# 🧠 OCR - Optical Character Recognition

This project is an Optical Character Recognition (OCR) tool built using Python, OpenCV, and Tesseract. It processes input images and extracts text using multiple preprocessing techniques such as dilation, thresholding, and grayscale conversion.

<p align="center">
  <img src="OCR/images/Screenshot 2025-05-23 210328.png" width="600"/>
</p>

## 🔍 Project Description

The OCR model is capable of recognizing printed characters from images with an accuracy of **87% to 91%**, depending on image quality and preprocessing methods. It demonstrates the effect of various thresholding and dilation techniques to optimize recognition.

## 🛠 Features

- Convert image to grayscale and apply preprocessing
- Apply various thresholding methods:
  - Adaptive Mean Thresholding
  - OTSU Thresholding
  - Gaussian Thresholding
- Dilation-based image enhancement
- Text extraction using `pytesseract`

## 🎯 Applications

- **Document Digitization** – Convert scanned documents to editable text.
- **License Plate Recognition** – Useful for traffic surveillance systems.
- **Text from Images** – Extract text from screenshots or mobile captures.
- **Form Processing** – Automate reading of printed forms or invoices.

## 🚀 Future Enhancements

The next version of this project will include:

- 🌐 **Frontend Web Interface** using HTML/CSS/JavaScript
- 🔧 **Backend API** using Flask/Django for image upload and OCR
- 📈 Display of prediction confidence and text bounding boxes

## 📂 Project Structure
---
  -     OCR/
  -      images/
  -       our_image.png
  -       main.py
  -      resize.py
  -      playground.py
  -      recognized.txt
  -      requirements.txt
  -      README.md
## 🐍 Requirements

Install required dependencies with:

```bash
pip install -r requirements.txt
