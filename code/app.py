#! /usr/bin/python3


import psycopg2
from config import config
from flask import Flask, render_template, request, redirect, url_for, session
 
# Database creds
user = 'lion'
passw = 'lion'
db = 'projtest'


# app.py

app = Flask(__name__)
app.secret_key = 'csc315'

# main index page
@app.route('/')
def index():
    conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
    curr = conn.cursor()
    curr.execute("""SELECT id, title, thumbnail FROM interview order by title; """)
    titles = curr.fetchall()
    curr.close()

    return render_template('index.html', titles=titles)

# about page
@app.route('/about')
def about():
    return render_template('about.html')

# individual interview pages
@app.route('/interview/<interviewid>')
def interview(interviewid):
    conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
    curr = conn.cursor()
    curr.execute("""SELECT * FROM interview WHERE id = (%s); """, interviewid)
    title = curr.fetchall()

    curr.execute("""SELECT * FROM assets WHERE fid = (%s); """, interviewid)
    assets = curr.fetchall()
    curr.close()

    return render_template('interview.html', title=title, assets=assets)

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        #curr.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        curr.execute('SELECT * FROM users LEFT JOIN administrator ON users.userid=administrator.userid WHERE username = %s AND password = %s', (username, password,))
        account = curr.fetchone()
        curr.close()

        if account:
            session['loggedin'] = True
            session['username'] = account[1]
            session['userid'] = account[0]
            session['perm'] = account[3]
            return redirect(url_for('profile'))
        else:
            error = 'Invalid credentials, please try again'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('userid', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        curr.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = curr.fetchone()

        if account:
            error = 'Account already exists'

        elif not username or not password:
            error = 'Information missing in fields, please try again'
        else:
            curr.execute('INSERT INTO users (username, password) VALUES(%s, %s)', (username, password,))
            conn.commit()
            return redirect(url_for('login'))

        curr.close()

    elif request.method == 'POST':
        error = 'Please fill out the form'

    return render_template('register.html', error=error)


@app.route('/profile')
def profile():
    if 'loggedin' in session:
        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        curr.execute('SELECT * FROM users WHERE userid = %s', (session['userid'],))
        account = curr.fetchone()
        curr.close()

        return render_template('profile.html', account=account)

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug = True)
