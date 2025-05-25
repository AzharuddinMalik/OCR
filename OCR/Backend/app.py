from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from ocr_processor import process_image # Assuming this import is correct

# Configure Flask app
app = Flask(__name__,
           template_folder='../templates',
           static_folder='../static')

# Set the upload folder to be at the project root level
# We use os.path.abspath(__file__) to get the current file's path, then navigate up two levels (..)
# to reach the OCR_PROJECT root, and then into the 'uploads' directory.
UPLOAD_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# --- IMPORTANT FIX FOR SERVING UPLOADED IMAGES ---
# Define a route to serve files from the 'uploads' directory
# This route will handle requests like /static/uploads/your_image.jpg
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    # send_from_directory is the correct way to serve files from a specific directory
    # It takes the directory path and the filename as arguments.
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# --- END IMPORTANT FIX ---


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            file.save(filepath)
            # Process the file
            extracted_text = process_image(filepath)
            # Return the filename along with the text so result.html can display the image
            return jsonify({'text': extracted_text, 'image_filename': filename})
        except Exception as e:
            # Catch any error during file saving or OCR processing
            print(f"Error during file processing: {e}") # Log the error on the server
            return jsonify({'error': f'Document analysis failed: {str(e)}'}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/result')
def show_result():
    extracted_text = request.args.get('text', 'No text extracted.')
    image_filename = request.args.get('image_filename', 'none') # Get image filename from query parameter
    return render_template('result.html', text=extracted_text, image_filename=image_filename)

if __name__ == '__main__':
    # Ensure the uploads directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
