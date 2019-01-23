import os
from threading import Thread
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from flask_mail import Mail, Message
from forms import ContactForm, SignupForm




basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
UPLOAD_FOLDER = ''
FORBIDDEN_EXTENSIONS = set(['exe'])
ALLOWED_EXTENSISONS = set(['mp3', 'aac', 'wav', 'ogg', 'flac'])
app.config['SECRET_KEY'] = 'a cappella'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[BVJE]'
app.config['FLASKY_MAIL_SENDER'] = 'BVJE Admin <no-reply@bvje.com>'
bootstrap =  Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSISONS



def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt.', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return thread




class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
   


    def __repr__(self):
        return '<User {}>'.format(self.username)







@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about/director')
def director():
    return render_template('director.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/members')
def members():
    return render_template('members.html')


@app.route('/members/<username>')
def user(username):
    return render_template('members.html', username=username)


@app.route('/repertoire')
def repertoire():
    return render_template('repertoire.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        session['name'] = form.name.data 
        session['email'] = form.email.data
        session['phone'] = form.phone.data
        session['request'] = form.request.data
        session['other'] = form.other.data
        return redirect(url_for('index'))

    return render_template('contact.html', form=form, name=session.get('name'), email=session.get('email'), phone=session.get('phone'), request=session.get('request'), other=session.get('other'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['username'] = form.username.data
        form.username.data = ''
        return redirect(url_for('index'))


        '''session['email'] = form.email.data
        session['password'] = form.password.data
        session['repeatpass'] = form.repeatpass.data
        session['voice'] = form.voice.data
        session['mp3'] = form.mp3.data
        session['info'] = form.info.data'''

    return render_template('signup.html', form=form, username=session.get('username'), email=session.get('email'), password=session.get('password'), repeatpass=session.get('repeatpass'), voice=session.get('voice'), info=session.get('info'), known=session.get('known', False))


def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run()