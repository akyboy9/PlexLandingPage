from flask import request, render_template, redirect
from views import app
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

@app.route('/landingToRequest', methods=['GET','POST'])
def landingToRequest():
    if request.method == 'POST':
        return redirect('/request_plex')

@app.route('/request_plex')
def request_plex():
    return render_template('request.html')

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    if request.method == 'POST':
        requested = request.form['text_2']
        requested = requested.upper()
        print requested
        return redirect('/request_plex')
