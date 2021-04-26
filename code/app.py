#! /usr/bin/python3


import psycopg2
from config import config
from flask import Flask, render_template, request, redirect, url_for
 
# Database creds
user = 'lion'
passw = 'lion'
db = 'projtest'


# app.py

app = Flask(__name__)

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
        curr.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        
        account = curr.fetchone()
        curr.close()

        if account:
                return redirect(url_for('index'))
        else:
                error = 'Invalid credentials, please try again'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug = True)
