import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Added deploy script. 01/25/22 @10:10am'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
