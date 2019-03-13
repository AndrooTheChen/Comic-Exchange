# app/listings/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, DecimalField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo
from .. import db
from sqlalchemy import text
from ..models import comicbook
from ..models import Selling
from datetime import datetime
        

class ListingForm(FlaskForm):
    """
    Form for users to post listings
    """
    publisher= StringField('Publisher', validators=[DataRequired()])
    series = StringField('Series', validators=[DataRequired()])
    issueNum = IntegerField('Issue #', validators=[DataRequired()])
    primaryCharacter = StringField('Primary Character', validators=[DataRequired()])
    primaryVillain = StringField('Primary Villain', validators=[DataRequired()])
    genre = SelectField('Genre', choices=[('action', 'action'), ('horror', 'horror'), ('adventure', 'adventure')])
    author = StringField('Primary Author', validators=[DataRequired()])
    price = DecimalField('Price ($)', places = 10, validators=[DataRequired()])
    datePosted = DateTimeField(label='DatePosted',format="%Y-%m-%dT%H:%M:%S",
        default=datetime.utcnow(), ## Now it will call it everytime.
        validators=[DataRequired()])
    submit = SubmitField('Post Listing')