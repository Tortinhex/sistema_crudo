from app import db
from datetime import datetime

"""
    CLASSE DE MODELO DO PRODUTO
    Exemplo de desenvolvimento:
        http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#simple-relationships
"""

class Product(db.Model):
    __tablename__ = "product"

    id            = db.Column(db.Integer,    primary_key=True)
    product_name  = db.Column(db.String(30), nullable=False)
    serial_number = db.Column(db.String(15), nullable=False)
    branch        = db.Column(db.String(15), nullable=False)
    model         = db.Column(db.String(15), nullable=False)
    quantity      = db.Column(db.String(10), nullable=False)
    category      = db.Column(db.String(15), nullable=False)
    description   = db.Column(db.Text      , nullable=False)
    coast         = db.Column(db.String(10), nullable=False)
    status        = db.Column(db.String(1),  nullable=True, default='A')
    created_by    = db.Column(db.String(30), nullable=True)
    created_at    = db.Column(db.DateTime,   nullable=True, default=datetime.utcnow)
    updated_by    = db.Column(db.String(30), nullable=True)
    updated_at    = db.Column(db.DateTime,   nullable=True, default=datetime.utcnow)

    provider_id   = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=True)
    # Provider      = db.relationship('Provider', foreign_keys=provider_id)

    # Classe inicializadora do modelo
    def __init__(self, product_name, serial_number, branch, model, quantity, category, description, coast, provider_id):
        self.product_name  = product_name
        self.serial_number = serial_number
        self.branch        = branch
        self.model         = model
        self.quantity      = quantity
        self.category      = category
        self.description   = description
        self.coast         = coast
        self.provider_id   = provider_id
        
    # Utilizado para exibir os registros do banco de dados de uma forma mais resumida
    def __repr__(self):
        return "<Product %r>" % self.id