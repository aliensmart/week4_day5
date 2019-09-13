from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/something', methods=['GET', 'POST'])
def add_numbers():
    data = request.json
    return jsonify({'data':data})


if __name__=="__main__":
    app.run(debug=True)


