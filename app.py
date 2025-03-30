from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/course-detail')
def course_detail():
    return render_template('course_detail.html')

@app.route('/about')
def about():
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 