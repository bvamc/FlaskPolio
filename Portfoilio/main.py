from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return render_template('index.html')

@app.route('/resume')
def show_resume():
    return render_template('resume.html')

@app.route('/projects')
def show_projects():
    return render_template('portfolio.html')

@app.route('/contact')
def show_contact():
    return render_template('contact.html')


@app.route('/download')
def downloadFile ():
    path = "static/resume.pdf"
    return send_file(path, as_attachment=True)