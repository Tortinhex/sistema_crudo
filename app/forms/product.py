from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    product_name  = StringField('Nome do Produto', validators=[DataRequired()])
    serial_number = StringField('Número de Série', validators=[DataRequired()])
    branch        = StringField('Marca')
    model         = StringField('Modelo', validators=[DataRequired()])
    description   = TextAreaField('Descrição')
    coast         = StringField('Custo Unitário (R$)', validators=[DataRequired()], render_kw={'placeholder': 'Ex: 30,00'})
    quantity      = StringField('Quantidade', validators=[DataRequired()], render_kw={'placeholder': 'Ex: 10'})
    category      = StringField('Categoria', validators=[DataRequired()])
    provider      = SelectField('Fornecedor', coerce=int)
    status        = SelectField('Status', coerce=int, choices=[(1, 'Ativo'), (2, 'Inativo')])