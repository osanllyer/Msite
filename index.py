'''
Created on Oct 29, 2014

@author: lifenbo
'''


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<username>')
def hello_world(username=None):
    return render_template('index.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)