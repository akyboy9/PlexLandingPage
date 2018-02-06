from flask import request, render_template, redirect, Flask, abort, request, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from plexapi.myplex import MyPlexAccount
from pushbullet import Pushbullet
from validation import verify_plex_access
from datetime import timedelta
app = Flask(__name__)

# app config

app.config.update(
    DEBUG=True,
    SECRET_KEY="asdfasdfasfdasdfasdfasdfasdfasdfasdfasdf"
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index_login"

username = ""


class User(UserMixin):

    def __init__(self, ident):
        self.id = ident

    def __repr__(self):
        return "%d" % self.id


def push_to_bullet(pb_username, note):
    api_key = 'o.RjVLTnmk1r9gg2elzO90qbl7D8sdVSyJ'
    pb = Pushbullet(api_key)
    pb.push_note(pb_username, note)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def index_login():
    global username
    if request.method == 'POST':
        username = request.form['text']
        password = request.form['pass']
        if verify_plex_access(username, password):
            user = User(username)
            login_user(user)
            request.args.get('next')
            return redirect('/home')
        return redirect('/')


def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return a_response


@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route('/home')
@login_required
def login():
    return render_template('landing.html')


@app.route('/landingToRequest', methods=['GET','POST'])
@login_required
def landing_to_request():
    if request.method == 'POST':
        return redirect('/request_plex')


@app.route('/request_plex')
@login_required
def request_plex():
    return render_template('request.html')


@app.route('/process_request', methods=['GET', 'POST'])
@login_required
def process_request():
    if request.method == 'POST':
        requested = request.form['text_2']
        push_to_bullet(username, requested)
        return redirect('/request_plex')


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
