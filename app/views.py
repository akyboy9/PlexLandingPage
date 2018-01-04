from flask import render_template, redirect
from app import app
from plexapi.myplex import MyPlexAccount

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/index')
def index_login():
    username = request.form['text']
    password = request.form['pass']
    password = text.upper()
    username = text.upper()
    if login_sucesful(username, password):
		return redirect('/login')
    return redirect('/index')

def login_succesful(username, password):
	master_acc = MyPlexAccount(account_1, password_1)
	master_friends = master_acc.users()
	master_friends = str(master_friends)
	login_acc = MyPlexAccount(username, password)
	login_user = login_acc.username
	login_user = str(login_user)
	#check if its in friends list
	if login_user in master_friends:
		return True
	else:
		return False
