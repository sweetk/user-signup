from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('forms.html', error=encoded_error)

@app.route("/welcome", methods=['POST'])
def welcome():

    #Pass form input
    usrname = request.form['usrname']
    #passw = request.form['passw']
    #pass_verify = request.form['pass_verify']
    #email = request.form['email']

    #Perform error verification
    #Just for username first?
    if len(usrname) < 3 or len(usrname) > 20:
        error = "That is not a valid username."
        return redirect("/?error=" + error)

    #If everything goes right
    return render_template('welcome.html', usrname=usrname)

app.run()
