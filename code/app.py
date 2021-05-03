#! /usr/bin/python3


import psycopg2
from config import config
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
 
# Database creds
user = 'postgres'
passw = 'tcnjslap2'
db = 'proj2'


# app.py

app = Flask(__name__)
app.secret_key = 'csc315'
bcrypt = Bcrypt(app)

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
    sql = ("SELECT * FROM interview WHERE id = %s")
    curr.execute(sql, (interviewid,))
    title = curr.fetchall()

    sql = ("SELECT * FROM assets WHERE fid = %s")
    curr.execute(sql, (interviewid,))
    assets = curr.fetchall()
    curr.close()

    return render_template('interview.html', title=title, assets=assets)

# individual interview assets
@app.route('/interview/<interviewid>/assets')
def assets(interviewid):
    conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
    curr = conn.cursor()
    sql = ("SELECT * FROM interview WHERE id = %s")
    curr.execute(sql, (interviewid,))
    title = curr.fetchall()

    sql = ("SELECT * FROM assets WHERE fid = %s order by timestamp")
    curr.execute(sql, (interviewid,))
    assets = curr.fetchall()
    curr.close()

    return render_template('assets.html', title=title, assets=assets)


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
        curr.execute('SELECT users.userid, username, password, permissions FROM users LEFT JOIN administrator ON users.userid=administrator.userid WHERE username = %s', (username,))
        account = curr.fetchone()
        curr.close()

        if account and bcrypt.check_password_hash(account[2], password):
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
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        curr.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = curr.fetchone()

        if account:
            error = 'Account already exists'

        elif not username or not password:
            error = 'Information missing in fields, please try again'
        else:
            curr.execute('INSERT INTO users (username, password) VALUES(%s, %s)', (username, pw_hash,))
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

@app.route('/delete-handler', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        inp = request.form.get('del')
        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        sql = ("DELETE FROM assets WHERE fid = %s")
        curr.execute(sql, (inp,))
        sql = ("DELETE FROM interview WHERE id = %s")
        curr.execute(sql, (inp,))
        conn.commit()
        curr.close()


    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    alert = None
    if request.method == 'POST' and 'title' in request.form and 'date' in request.form and 'audio' in request.form and 'thumbnail' in request.form and 'script' in request.form:
        title = request.form['title']
        date = request.form['date']
        audio = request.form['audio']
        thumbnail = request.form['thumbnail']
        script = request.form['script']
        uid = session.get('userid')

        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        curr.execute('SELECT * FROM interview WHERE title = %s', (title,))
        interview = curr.fetchone()

        if interview:
            alert = 'That interview already exists, please try again'

        elif not title or not date or not audio or not thumbnail or not script:
            alert = 'Information missing in fields, please try again'

        else:
            curr.execute('INSERT INTO interview (title, date, audio, thumbnail, script, uid) VALUES (%s, %s, %s, %s, %s, %s)', (title, date, audio, thumbnail, script, uid,))
            conn.commit()
            return redirect(url_for('index'))

        curr.close()

    return render_template('add.html', alert=alert)

@app.route('/addasset', methods=['GET', 'POST'])
def addasset():
    alert = None
    if request.method == 'POST' and 'title' in request.form and 'date' in request.form and 'audio' in request.form and 'thumbnail' in request.form and 'script' in request.form:
        title = request.form['title']
        date = request.form['date']
        audio = request.form['audio']
        thumbnail = request.form['thumbnail']
        script = request.form['script']
        uid = session.get('userid')

        conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
        curr = conn.cursor()
        curr.execute('SELECT * FROM interview WHERE title = %s', (title,))
        interview = curr.fetchone()

        if interview:
            alert = 'That interview already exists, please try again'

        elif not title or not date or not audio or not thumbnail or not script:
            alert = 'Information missing in fields, please try again'

        else:
            curr.execute('INSERT INTO interview (title, date, audio, thumbnail, script, uid) VALUES (%s, %s, %s, %s, %s, %s)', (title, date, audio, thumbnail, script, uid,))
            conn.commit()
            return redirect(url_for('index'))

        curr.close()

    return render_template('addasset.html', alert=alert)

if __name__ == '__main__':
    app.run(debug = True)
