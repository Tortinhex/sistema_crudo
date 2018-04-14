from app import db
from datetime import datetime

"""
    CLASSE DE MODELO DE ENDERECO
    Exemplo de desenvolvimento:
        http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#simple-relationships
"""

class Address(db.Model):
    __tablename__ = "address"

    id          = db.Column(db.Integer,    primary_key=True)
    street      = db.Column(db.String(50), nullable=False)
    number      = db.Column(db.String(5) , nullable=False)
    complement  = db.Column(db.String(30), nullable=False)
    district    = db.Column(db.String(30), nullable=False)
    city        = db.Column(db.String(30), nullable=False)
    state       = db.Column(db.String(30), nullable=False)
    country     = db.Column(db.String(30), nullable=False)
    postal_code = db.Column(db.String(8),  nullable=False)
    status      = db.Column(db.String(1),  nullable=False, default='A')
    created_by  = db.Column(db.String(30), nullable=True)
    created_at  = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow)
    updated_by  = db.Column(db.String(30), nullable=True)
    updated_at  = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow)

    # Classe inicializadora do modelo
    def __init__(self, street, number, complement, district, city, state, country, postal_code):
        self.street      = street
        self.number      = number
        self.complement  = complement
        self.district    = district
        self.city        = city
        self.state       = state
        self.country     = country
        self.postal_code = postal_code
    
    # Utilizado para exibir os registros do banco de dados de uma forma mais resumida
    def __repr__(self):
        return "<Address %r>" % self.id