from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    args = request.args.get('q')
    return redirect(f'https://www.google.com/search?q={args}')


if __name__ == '__main__':
    app.run()
