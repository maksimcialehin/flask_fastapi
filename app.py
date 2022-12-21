from flask import Flask, render_template, request, redirect, jsonify
from model.dbHandler import match_exact, match_like


app = Flask(__name__)

@app.route('/')
def index():
    response = request.args.getlist('word')
    return response


@app.route('/search')
def search():
    return render_template('index.html')


@app.route('/dict')
def dictionary():
    words = request.args.getlist('word')

    if not words:
        return jsonify({'word': words, 'status': 'error', 'data': 'not found'})
    
    response = {'words': []}

    for word in words:
        definitions = match_exact(word)

        if definitions:
            response['words'].append({'word': word, 'status': 'success', 'data': definitions})
        else:
            definitions = match_like(word)
            if definitions:
                response['words'].append({'word': word, 'status': 'partial', 'data': definitions})
            else:
                response['words'].append({'word': word, 'success': 'error', 'data': 'not found'})
    
    return jsonify(response)


if __name__ == '__main__':
    app.run()
