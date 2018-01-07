from flask import request, render_template, redirect, Flask
from plexapi.myplex import MyPlexAccount

app = Flask(__name__)


# def verify_plex_access(username, password):



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
                return redirect('/home')
        return redirect('/')


@app.route('/home')
def login():
    return render_template('landing.html')


@app.route('/landingToRequest', methods=['GET','POST'])
def landing_to_request():
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


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
