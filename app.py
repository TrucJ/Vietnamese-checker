from flask import Flask, request, jsonify
from main import Vietnamese_check

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Vietnamese checker"

@app.route('/check', methods=['POST'])
def vietnamese_check():
    try:
        data = request.get_json()
        print("req: ", data)
        if 'text' in data:
            text = data['text']
            is_vietnamese = Vietnamese_check(text)
            response = {'is_vietnamese': is_vietnamese}
            return jsonify(response)
        else:
            return jsonify({'error': 'Missing "text" in the request data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
