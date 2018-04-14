from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    product_name  = StringField('Nome do Produto', validators=[DataRequired()])
    serial_number = StringField('Número de Série', validators=[DataRequired()])
    branch        = StringField('Marca')
    model         = StringField('Modelo', validators=[DataRequired()])
    description   = TextAreaField('Descrição')
    coast         = StringField('Custo', validators=[DataRequired()])
    provider      = SelectField('Fornecedor', coerce=int)