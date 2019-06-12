from flask import Flask
#, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    #if (request.method == 'POST'):
    #    some_json = "Sunesh" 
        #request.GET_json()
    #    return jsonify({'You send': some_json}), 201
    #else:
    #return jsonify({'about': 'Hello world'})
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
