from flask import request, render_template, redirect, Flask
from plexapi.myplex import MyPlexAccount
from pushbullet import Pushbullet

app = Flask(__name__)

def push_to_bullet(username, note):
    api_key ='o.RjVLTnmk1r9gg2elzO90qbl7D8sdVSyJ'
    pb = Pushbullet(api_key)
    push = pb.push_note(username, note)


def verify_plex_access(username, password):
    if username == 'USERNAME':
        if password == 'PASSWORD':
            return True
    return False



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
        kobe = verify_plex_access(username, password)
        if kobe == True:
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
        push_to_bullet('username',requested)
        return redirect('/request_plex')


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
