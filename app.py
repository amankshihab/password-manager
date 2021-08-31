from logging import error
from flask import Flask, request, render_template, sessions, url_for
from werkzeug.utils import redirect

import postg

app = Flask(__name__, template_folder='templates')

# id = None


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        # from postg.py gets the user login from the database
        loginDetails = postg.fetchLogin(request.form["username"])
        if not loginDetails == None:
            if request.form["username"] == loginDetails[1] and request.form["password"] == loginDetails[2]:
                global id
                id = loginDetails[0]
                return redirect('/password')
            else:
                return render_template('login.html', error="Login failed!")
        else:
            return render_template('login.html', error="User does not exist!")

    return render_template('login.html')


@app.route('/password', methods=['GET', 'POST'])
def password():

    if request.method != 'POST':
        passwords = postg.fetchPassword(id)

        if password != None:
            return render_template('password.html', passwords=passwords)

        else:
            return render_template('password.html', text="No Passwords found!")


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        # from postg.py gets the user login from the database
        if request.form["username"] != '':
            if request.form["passw"] == request.form['confirmpass']:
                postg.makeUser(request.form['username'], request.form['passw'])
                return redirect('/')

    return render_template('register.html')







