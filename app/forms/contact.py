from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    phone               = StringField('Telefone', validators=[DataRequired()], render_kw={'placeholder': 'Ex: +99 99 9 9999-9999'})
    email               = StringField('E-mail', validators=[DataRequired()], render_kw={'placeholder': 'Ex: contato@contato.com'})
    employee_name       = StringField('Nome do contato', validators=[DataRequired()], render_kw={'placeholder': 'Ex: John Doe'})
    employee_department = StringField('Departamento do contato', render_kw={'placeholder': 'Nome do Departamento do funcionário'})