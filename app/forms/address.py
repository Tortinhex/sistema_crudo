from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class AddressForm(FlaskForm):
    street       = StringField('Logradouro', validators=[DataRequired()])
    number       = StringField('Número',     validators=[DataRequired()])
    complement   = StringField('Complemento')
    district     = StringField('Bairro',     validators=[DataRequired()])
    city         = StringField('Cidade',     validators=[DataRequired()])
    state        = StringField('Estado',     validators=[DataRequired()])
    country      = StringField('País',       validators=[DataRequired()])
    postal_code  = StringField('CEP',        validators=[DataRequired()])