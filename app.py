from flask import Flask, request, jsonify
from main import Vietnamese_check

app = Flask(__name__)

@app.route("/")
def index():
    return """
        Welcome to Vietnamese checker. Use cmd: 
        curl -X POST https://vietnamese-checker.vercel.app/ \
        --header 'Content-Type: application/json' \
        --data '{"text": "Việt"}'
    """

@app.route('/<word>')
def vietnamese_word_check(word):
    try:
        is_vietnamese = Vietnamese_check(word)
        response = {'result': is_vietnamese}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['POST'])
def vietnamese_check():
    try:
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            is_vietnamese = Vietnamese_check(text)
            response = {'result': is_vietnamese}
            return jsonify(response)
        else:
            return jsonify({'error': 'Missing "text" in the request data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
