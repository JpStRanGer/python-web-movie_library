from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    SubmitField,
    TextAreaField,
    URLField,
    PasswordField,
)
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(
                min=1878, max=2023, message="Please enter a year between 1878 and 1952"
            ),
        ],
    )

    submit = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = StringField("Description")
    video_link = StringField("Video link")

    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    email = StringField(
        "Email", validators=[InputRequired(), Email(check_deliverability=True)]
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=5, message="Your password is to short!"),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo(
                "password",
                message="This password did not match the one in the password field!",
            ),
        ],
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[InputRequired(), Email(check_deliverability=True)]
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=5, message="Your password is to short!"),
        ],
    )
    submit = SubmitField("Register")
