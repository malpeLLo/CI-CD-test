from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_text():
    data = request.get_json()
    text = data.get('text', '')
    reversed_text = text[::-1]
    return jsonify({'reversed_text': reversed_text})

if __name__ == "__main__":
    app.run(debug=True)