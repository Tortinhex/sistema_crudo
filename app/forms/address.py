from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class AddressForm(FlaskForm):
    street       = StringField('Logradouro', validators=[DataRequired()], render_kw={'placeholder': 'Logradouro'})
    number       = StringField('Número',     validators=[DataRequired()], render_kw={'placeholder': 'Ex: 99'})
    complement   = StringField('Complemento', render_kw={'placeholder': 'Ex: Sala 99'})
    district     = StringField('Bairro',     validators=[DataRequired()], render_kw={'placeholder': 'Bairro'})
    city         = StringField('Cidade',     validators=[DataRequired()], render_kw={'placeholder': 'Cidade'})
    state        = StringField('Estado',     validators=[DataRequired()], render_kw={'placeholder': 'Estado'})
    country      = StringField('País',       validators=[DataRequired()], render_kw={'placeholder': 'País'})
    postal_code  = StringField('CEP',        validators=[DataRequired()], render_kw={'placeholder': 'Ex: 99999-999'})