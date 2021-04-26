#! /usr/bin/python3


import psycopg2
from config import config
from flask import Flask, render_template, request
 
# Database creds
user = 'postgres'
passw = 'tcnjslap2'
db = 'proj'


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

# individual interview pages
@app.route('/interview/<interviewid>')
def interview(interviewid):
    conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
    curr = conn.cursor()
    curr.execute("""SELECT id ,title, date FROM interview WHERE id = (%s); """, interviewid)
    title = curr.fetchall()

    curr.execute("""SELECT * FROM assets WHERE fid = (%s); """, interviewid)
    assets = curr.fetchall()
    curr.close()

    return render_template('interview.html', title=title, assets=assets)


if __name__ == '__main__':
    app.run(debug = True)
