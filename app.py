from flask import Flask
from flask import request
from src.shorter import Shorter

app = Flask(__name__)

@app.route('/', methods=['POST'])
def shorter_url():
    url = request.args.get('url', '')
    return 'url {}'.format(url)

@app.route('/s/<code>')
def open_shorter_url(code):
    shorter_url = Shorter(code)
    return shorter_url.get_code()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)