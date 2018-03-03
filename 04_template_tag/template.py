# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/user/<name>')
def user(name='Juan'):
    return render_template('index.html', nombre=name)


if __name__ == '__main__':
    app.run(debug = True,  port= 8000)

# http://127.0.0.1:8000/user/maria

