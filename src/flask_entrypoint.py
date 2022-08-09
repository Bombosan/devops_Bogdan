# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    x = x + 1
    return 'Ce faceti bai!? Bai nebunilor! Avem Python intrun Docker container!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)