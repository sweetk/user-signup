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
    passw = request.form['passw']
    pass_verify = request.form['pass_verify']
    email = request.form['email']

    #Perform error verification
    #For username
    if len(usrname) < 3 or len(usrname) > 20:
        error = "That is not a valid username."
        return redirect("/?error=" + error)

    #for Password
    if len(passw) < 3 or len(passw) > 20 or " " in passw:
        error = "That is not a valid password."
        return redirect("/?error=" + error)

    #for second Password
    if passw != pass_verify:
        error = "Passwords don't match."
        return redirect("/?error=" + error)

    #for email
    if email:
        if len(email) < 3 or len(email) > 20 or " " in email:
            error = "That is not a valid email."
            return redirect("/?error=" + error)
        #check special characters
        if '@' not in email or '.' not in email:
            error = "That is not a valid email."
            return redirect("/?error=" + error)

        #too many special characters

    #If everything goes right
    return render_template('welcome.html', usrname=usrname)

app.run()
