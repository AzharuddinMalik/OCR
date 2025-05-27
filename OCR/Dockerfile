# Use official Python slim image
FROM python:3.11-slim

# Install system dependencies including tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Create the uploads directory and ensure correct permissions
# The 'uploads' directory will be at /app/uploads because of WORKDIR /app and COPY . .
RUN mkdir -p uploads && chmod -R 777 uploads

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (Flask default)
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["sh", "-c", "gunicorn Backend.app:app --workers 1 --threads 2 --timeout 60 --bind 0.0.0.0:$PORT"]
