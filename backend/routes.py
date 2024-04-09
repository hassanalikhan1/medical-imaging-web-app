from flask import jsonify, request, Blueprint, make_response

# Create a Blueprint object for routes
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def index():
    return 'Hello, Flask!'

@routes_blueprint.route('/api/upload-dicom/', methods=["POST", "OPTIONS"])
def upload_dicom():
    
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST":
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        response = jsonify({'message': 'Upload successful'})

        return _corsify_actual_response(response)
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@routes_blueprint.route('/api/get-dicom/<file_id>', methods=['GET'])
def get_dicom(file_id):
    # Here you can add code to fetch and return the DICOM file based on file_id
    # For now, we'll just return a dummy response
    return jsonify({'file_id': file_id, 'data': 'DICOM file data'})

@routes_blueprint.route('/api/process-dicom/<file_id>', methods=['PUT'])
def process_dicom(file_id):
    # Here you can add code to process the DICOM file based on file_id
    # For now, we'll just return a success message
    return jsonify({'success': f'DICOM file {file_id} processed successfully'})
