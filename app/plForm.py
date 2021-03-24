from flask_wtf  import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf.recaptcha import validators
from wtforms import StringField, TextAreaField, SelectField, FileField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class PropertyListingForm(FlaskForm):

    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    roomNum = IntegerField('No. of Rooms', validators=[DataRequired()],  render_kw="placeholder": 3)
    bRoomNum = IntegerField('No. of Bedrooms', validators=[DataRequired()], render_kw="placeholder": 2 )
    price = DecimalField('Price', validators=[DataRequired()],  render_kw="placeholder": 15000000.0)
    propertyType = SelectField('Property type', choices=[('Apartment', 'Apartment'), ('House', 'House')] )
    location = StringField('Location', validators=[DataRequired()],  render_kw="placeholder": "10 Waterloo Rd")
    photo = FileField('Photos', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
