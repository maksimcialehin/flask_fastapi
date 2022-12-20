from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/greet')
def index():
    name = request.args.get('name')
    if not name:
        return jsonify({'status': 'error'})


    response = {'data': f'Hello {name} you are an asshole'}
    return jsonify(response)
