from flask import Flask, request, redirect, render_template
import cgi, re

app = Flask(__name__)
app.config['DEBUG'] = True

def error_verification():
    usrname = request.form['usrname']
    passw = request.form['passw']
    pass_verify = request.form['pass_verify']
    email = request.form['email']

    #initialize variables
    error_u = ''
    error_p = ''
    error_pv = ''
    error_e = ''

    #For username
    if len(usrname) < 3 or len(usrname) > 20:
        error_u = "That is not a valid username."

    #for Password
    if len(passw) < 3 or len(passw) > 20 or " " in passw:
        error_p = "That is not a valid password."

    #for second Password
    if passw != pass_verify:
        error_pv = "Passwords don't match."

    #for email
    if email:
        if len(email) < 3 or len(email) > 20 or " " in email:
            error_e = "That is not a valid email."

        #check special characters
        elif '@' not in email or '.' not in email or ' ' in email:
                error_e = "That is not a valid email."

        #too many special characters
        else:
            iterate_at = [m.start() for m in re.finditer('\@', email)]
            iterate_dot = [m.start() for m in re.finditer('\.', email)]
            if len(iterate_at) > 1:
                error_e = "That is not a valid email."

            elif len(iterate_dot) > 1:
                error_e = "That is not a valid email."

    if error_u or error_p or error_pv or error_e:
        #return "return redirect('/?error_u=' + error_u + '&error_p=' + error_p + '&error_pv=' + error_pv + '&error_e=' + error_e)"
        return redirect('/?error_u=' + error_u + '&error_p=' + error_p + '&error_pv=' + error_pv + '&error_e=' + error_e)

    else:
        return False

@app.route("/")
def index():
    #error codes
    encoded_error_u = request.args.get("error_u")
    encoded_error_p = request.args.get("error_p")
    encoded_error_pv = request.args.get("error_pv")
    encoded_error_e = request.args.get("error_e")

    return render_template('forms.html', error_u=encoded_error_u, error_p=encoded_error_p, error_pv=encoded_error_pv, error_e=encoded_error_e)

@app.route("/welcome", methods=['POST'])
def welcome():
    if error_verification():
        return error_verification()

    #Pass form input
    usrname = request.form['usrname']

    #If everything goes right
    return render_template('welcome.html', usrname=usrname)

app.run()
