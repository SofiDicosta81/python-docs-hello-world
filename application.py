from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return jsonify({'about': 'Hello world'}),

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result' : num*10})

@app.route('/add/<int:val>', methods=['GET'])
def get_Sum(val):
    return jsonify({'result': val+20})

if __name__ == "__main__":
    app.run(debug=True)
