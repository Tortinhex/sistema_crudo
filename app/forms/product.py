from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    product_name  = StringField('Nome do Produto', validators=[DataRequired()], render_kw={'placeholder': 'Nome do Produto'})
    serial_number = StringField('Número de Série', validators=[DataRequired()], render_kw={'placeholder': 'Ex: 67365AAE'})
    branch        = StringField('Marca', render_kw={'placeholder': 'Marca do Produto'})
    model         = StringField('Modelo', validators=[DataRequired()], render_kw={'placeholder': 'Modelo do Produto'})
    description   = TextAreaField('Descrição', render_kw={'placeholder': 'Descrição do Produto'})
    coast         = StringField('Custo Unitário (R$)', validators=[DataRequired()], render_kw={'placeholder': 'Ex: 30,00'})
    quantity      = StringField('Quantidade', validators=[DataRequired()], render_kw={'placeholder': 'Ex: 10'})
    category      = StringField('Categoria', validators=[DataRequired()], render_kw={'placeholder': 'Categoria do Produto'})
    provider      = SelectField('Fornecedor', coerce=int)
    status        = SelectField('Status', coerce=int, choices=[(1, 'Ativo'), (2, 'Inativo')])