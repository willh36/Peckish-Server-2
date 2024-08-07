from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Peckish home page!"

@app.route('/api', methods=['GET'])
def api():
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    return jsonify("i'am am the api response")

if __name__ == '__main__':
    app.run(debug=True)