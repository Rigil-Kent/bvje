from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectMultipleField 
from wtforms.validators import DataRequired, Email, EqualTo


app = Flask(__name__)
app.config['SECRET KEY'] = 'a cappella'
bootstrap =  Bootstrap(app)
moment = Moment(app)


class SignupForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[Email()])
    passwd = PasswordField('Password: ', validators=[DataRequired()])
    passrepeat = PasswordField('Repeat Password: ', validators=[EqualTo(passwd)])
    voice = SelectMultipleField('Voice: ', choices=[('soprano', 'soprano'), ('alto', 'alto'), ('tenor', 'tenor'), ('baritone', 'baritone'), ('bass', 'bass')], validators=[DataRequired()])

    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[Email()])
    phone = StringField('Phone: ', validators=[DataRequired()])
    request = StringField('Song Request(s): ', validators=[DataRequired()])
    submit = SubmitField('Submit')


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


def shop():
    return render_template('shop.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run()