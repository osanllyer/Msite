# -*- coding: utf-8 -*-
'''
Created on Oct 29, 2014

@author: lifenbo
'''


from flask import Flask, abort
from flask import render_template
import os, os.path
from flask.helpers import url_for
import common.definitions as Definitions

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ask')
def ask():
    return render_template('ask.html',backUrl="/")

# @app.route('/img/<filename>')
# def img_file(filename):
#     '访问图像文件'
#     return url_for('/static/img', filename=filename)

@app.route('/t/<template_name>')
def commonTemplate(template_name):
    '访问通用模板'
    filePath = os.path.dirname(__file__)
    '''check template exists'''
    if os.path.exists(filePath + '/templates/' + template_name + '.html'):
        path, filename = os.path.split(template_name)
        title = Definitions.template_title_map.get(filename)
        return render_template(template_name + '.html', title=title)
    else:
        abort(404)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('common/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)