from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    id                  = StringField('ID do Produto', validators=[DataRequired()])
    phone               = StringField('Telefone', validators=[DataRequired()])
    email               = StringField('E-mail', validators=[DataRequired()])
    employee_name       = StringField('Nome do contato', validators=[DataRequired()])
    employee_department = StringField('Departamento do contato')