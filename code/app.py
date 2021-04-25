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
    curr.execute("""SELECT id ,title, thumbnail FROM interview order by title; """)
    titles = curr.fetchall()
    curr.close()

    return render_template('index.html', titles=titles)

# individual interview pages
@app.route('/interview/<interviewid>')
def interview(interviewid):
    conn = psycopg2.connect("dbname=" + db + " user=" + user + " password=" + passw)
    curr = conn.cursor()
    curr.execute("""SELECT id ,title FROM interview WHERE id = (%s); """, interviewid)
    title = curr.fetchall()
    curr.close()

    return render_template('interview.html', title=title)

# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

# handle form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    rows = connect(request.form['query'])

    return render_template('my-result.html', rows=rows)

if __name__ == '__main__':
    app.run(debug = True)
