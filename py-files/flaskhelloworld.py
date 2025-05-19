app.py
from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/load')
def simulate_load():
    time.sleep(5)  # Simulate a delay to increase load
    return 'Load simulated!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
