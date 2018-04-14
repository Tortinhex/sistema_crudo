from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ProviderForm(FlaskForm):
    trading_name     = StringField('Nome Fantasia', validators=[DataRequired()])
    company_name     = StringField('Razão Social',  validators=[DataRequired()])
    document_number  = StringField('CNPJ',          validators=[DataRequired()], render_kw={'placeholder': 'Ex: 99.999.9999/9999-99'})
    cnae             = StringField('CNAE', render_kw={'placeholder': 'Ex: 9999-9/99'})
    ie               = StringField('IE', render_kw={'placeholder': 'Ex: 999999999'})
    im               = StringField('IM', render_kw={'placeholder': 'Ex: 9.999.999-9'})