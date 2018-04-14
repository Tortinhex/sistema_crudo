from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ProviderForm(FlaskForm):
    trading_name     = StringField('Nome Fantasia', validators=[DataRequired()])
    company_name     = StringField('Razão Social',  validators=[DataRequired()])
    document_number  = StringField('CNPJ',          validators=[DataRequired()])
    cnae             = StringField('CNAE')
    ie               = StringField('IE')
    im               = StringField('IM')