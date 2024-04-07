from backend import app
from flask import jsonify

@app.route('/api/upload-dicom', methods=['POST'])
def upload_dicom():
    # Handle DICOM upload logic here
    return jsonify({'success': 'DICOM file uploaded successfully'})