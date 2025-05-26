# OCR Flask App

[![Live Deployment](https://img.shields.io/badge/LIVE-DEMO-brightgreen?style=for-the-badge&logo=render)](https://ocr-flask-app-0la0.onrender.com)

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Development Setup](#local-development-setup)
- [Deployment](#deployment)
- [Uploading & Viewing Results](#uploading--viewing-results)
- [Project Structure](#project-structure)
- [Lessons Learned](#lessons-learned)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project
**Live Demo:** [https://ocr-flask-app-0la0.onrender.com](https://ocr-flask-app-0la0.onrender.com)

This web-based OCR application built with Flask allows users to upload images, processes them using OpenCV, performs OCR with Tesseract, and displays extracted text. Designed to handle deployment challenges for system-level dependencies in cloud environments.

---

## Features
- **Image Upload**: JPG/PNG support with drag-and-drop
- **Result Display**: Side-by-side view of original image and extracted text
- **Image Processing**: 
  - Grayscale conversion
  - Thresholding
  - Noise reduction
- **OCR Results**:
  - Clean text formatting
  - Direct image/text comparison
  - Copy-to-clipboard functionality

---

## Uploading & Viewing Results
### Step-by-Step Process:
1. **Upload Image**:
   - Drag & drop into the designated zone
   - Or click "Browse Files" to select from device
   
2. **Image Processing**:
   - Automatic conversion to optimal OCR format
   - Background processing using OpenCV

3. **Result Display**:
   - Original image shown in left panel
   - Extracted text displayed in right panel
   - Text appears in formatted `<pre>` block
   - Image stored temporarily at: 
     ```bash
     static/uploads/{filename}
     ```

4. **New Conversion**:
   - Click "Convert Another Image" to restart

---

## Deployment
### Live Deployment
Currently hosted on Render.com:  
[https://ocr-flask-app-0la0.onrender.com](https://ocr-flask-app-0la0.onrender.com)

### Deployment Features:
- **Auto-scaling**: Handles traffic spikes
- **Dockerized**: Consistent environment
- **Continuous Deployment**: GitHub integration
- **SSL**: Secure HTTPS connection

---

[Rest of the README remains unchanged...]
