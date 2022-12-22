from flask import Flask, request, send_file, jsonify
from bin.filters import apply_filter


# Filters available in PIL
filters_available = [
    "blur" ,
    "contour" ,
    "detail" ,
    "edge_enhance" ,
    "edge_enhance_more" ,
    "emboss" ,
    "find_edges" ,
    "sharpen" ,
    "smooth" ,
    "smooth_more" ,
    ]


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = {
        'filters_available': filters_available,
        'usage': {'http_methos': 'POST', 'URL': '/<filter>'}
    }
    return jsonify(response)


@app.post('/<filter>')
def image_filter(filter):
    
    if filter not in filters_available:
        response = {'error': 'incorrect filter'}
        return jsonify(response)

    file = request.files['image']
    if not file:
        response = {'error': 'no file provided'}
        return jsonify(response)

    filtered_image = apply_filter(file, filter)

    return send_file(filtered_image, mimetype='image/JPEG')


if __name__ == '__main__':
    app.run()
