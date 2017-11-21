from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{

            }}
            h1 {{

            }}
        </style>
    </head>
    <body>
      <h1>Signup</h1>
      <form action='/' method='post'>
        <label for='usrname'>Username:</label>
        <input id='usrname' type='text' name='usrname' value="{0}"/>
      </form>
      <form action='/' method='post'>
        <label for='pass'>Password:</label>
        <input id='pass' type='text' name='pass'/>
      </form>
      <form action='/' method='post'>
        <label for='pass_verify'>Verify Password:</label>
        <input id='pass_verify' type='text' name='pass_verify'/>
      </form>
      <form action='/' method='post'>
        <label for='email'>Email (Optional):</label>
        <input id='email' type='text' name='email' value="{0}"/>
      </form>
      <input type='submit' />
    </body>
</html>
'''

@app.route("/")
def index():
    return form.format('')

app.run()
