from application import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def updates(posts=None):
    return render_template('courses.html')
