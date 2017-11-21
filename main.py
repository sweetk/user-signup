from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    usrname = request.form['usrname']
    return render_template('welcome.html', usrname=usrname)

app.run()
