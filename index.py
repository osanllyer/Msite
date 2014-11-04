'''
Created on Oct 29, 2014

@author: lifenbo
'''


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ask')
def ask():
    return render_template('ask.html',backUrl="/")

@app.route('/t/<template_name>')
def commonTemplate(template_name):
    return render_template(template_name + '.html')


if __name__ == '__main__':
    app.run(debug=True)