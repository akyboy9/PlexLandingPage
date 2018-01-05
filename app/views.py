from flask import render_template, redirect, request
from app import app
from plexapi.myplex import MyPlexAccount

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index', methods=['GET','POST'])
def index_login():
	if request.method == 'POST':
		username = request.form['text']
		password = request.form['pass']
		password = password.upper()
		username = username.upper()
		if username == 'USERNAME':
			if password == 'PASSWORD':
				return redirect('/login')
		return redirect('/')

@app.route('/login')
def login():
	return render_template('landing.html')

