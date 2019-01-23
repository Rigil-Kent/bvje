from wtforms import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectMultipleField, FileField
from wtforms.validators import DataRequired, Email, EqualTo




class SignupForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[Email()])
    passwd = PasswordField('Password: ', validators=[DataRequired()])
    passrepeat = PasswordField('Repeat Password: ', validators=[EqualTo(passwd)])
    voice = SelectMultipleField('Voice: ', choices=[('soprano', 'Soprano'), ('alto', 'Alto'), ('tenor', 'Tenor'), ('baritone', 'Baritone'), ('bass', 'Bass')], validators=[DataRequired()])
    file = FileField('Attach MP3: ', )
    other = TextAreaField('Additional information: ')
    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[Email()])
    phone = StringField('Phone: ', validators=[DataRequired()])
    request = StringField('Song Request(s): ', validators=[DataRequired()])
    other = TextAreaField('Additional information: ')
    submit = SubmitField('Submit')