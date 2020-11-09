import os
from flask import Flask, render_template, request
from flask import render_template
from models import db

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/')
def start():
	return render_template('start.html')

@app.route('/canvas')
def canvas():
	return render_template('index.html')

@app.route('/result')
def result():
	return render_template('result.html')

@app.route('/statistics')
def statistics():
	return render_template('statistics.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        #--------------------------------------------------------
        #save한 이미지로 classification 진행
        #--------------------------------------------------------
        return 'success, tag: Apple'

if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    db.init_app(app) # app 설정값들을 초기화한다.
    db.app = app # models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣어준다.
    db.create_all()
    
    app.run(host='127.0.0.1', port=5000, debug=True)