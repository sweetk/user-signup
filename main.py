from flask import Flask, request, redirect, render_template
import cgi, re

app = Flask(__name__)
app.config['DEBUG'] = True

#Initialize global variables
global usrname_g
usrname_g = ''
global email_g
email_g = ''

def error_verification():
    global usrname_g
    usrname_g= request.form['usrname']
    passw = request.form['passw']
    pass_verify = request.form['pass_verify']
    global email_g
    email_g = request.form['email']

    #initialize variables
    error_u = ''
    error_p = ''
    error_pv = ''
    error_e = ''

    #For username
    if len(usrname_g) < 3 or len(usrname_g) > 20:
        error_u = "That is not a valid username."

    #for Password
    if len(passw) < 3 or len(passw) > 20 or " " in passw:
        error_p = "That is not a valid password."

    #for second Password
    if passw != pass_verify:
        error_pv = "Passwords don't match."

    #for email
    if email_g:
        if len(email_g) < 3 or len(email_g) > 20 or " " in email_g:
            error_e = "That is not a valid email."

        #check special characters
        #Why won't this stay where I put it damnit
        elif '@' not in email_g or '.' not in email_g or ' ' in email_g:
                error_e = "That is not a valid email."

        #too many special characters
        else:
            iterate_at = [m.start() for m in re.finditer('\@', email_g)]
            iterate_dot = [m.start() for m in re.finditer('\.', email_g)]
            if len(iterate_at) > 1:
                error_e = "That is not a valid email."

            elif len(iterate_dot) > 1:
                error_e = "That is not a valid email."

    #If there are any errors, redirect
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

    #TODO
    #HOW do I get it to save the usrname and email??
    #Need to set usrname_g and email_g to '' but not reset it?

    return render_template('forms.html', usrname_val = usrname_g, email_val = email_g, error_u=encoded_error_u, error_p=encoded_error_p, error_pv=encoded_error_pv, error_e=encoded_error_e)

@app.route("/welcome", methods=['POST'])
def welcome():
    if error_verification():
        return error_verification()

    #Pass form input
    #usrname = request.form['usrname']

    #If everything goes right
    return render_template('welcome.html', usrname=usrname_g)

app.run()
