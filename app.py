from flask import Flask, request, jsonify
import math

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Online Calculator API!"


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify(result=result)


@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify(result=result)


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify(result=result)


@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if data['b'] == 0:
        return jsonify(error="Division by zero is not allowed."), 400
    result = data['a'] / data['b']
    return jsonify(result=result)


@app.route('/sqrt', methods=['POST'])
def sqrt():
    data = request.get_json()
    if data['a'] < 0:
        return jsonify(error="Cannot take the square root of \
        a negative number."), 400
    result = math.sqrt(data['a'])
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
