from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET KEY'] = 'a cappella'
bootstrap =  Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html')


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


def gallery():
    return render_template('gallery.html')


def shop():
    return render_template('shop.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run()