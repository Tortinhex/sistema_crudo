from app import db
from datetime import datetime

"""
    CLASSE DE MODELO DO FORNECEDOR
    Exemplo de desenvolvimento:
        http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#simple-relationships
"""

class Provider(db.Model):
    __tablename__ = "provider"

    id              = db.Column(db.Integer,    primary_key=True)
    trading_name    = db.Column(db.String(30), nullable=False)
    company_name    = db.Column(db.String(50), nullable=False)
    document_number = db.Column(db.String(14), nullable=False)
    cnae            = db.Column(db.String(10), nullable=False)
    ie              = db.Column(db.String(10), nullable=False)
    im              = db.Column(db.String(10), nullable=False)
    status          = db.Column(db.String(1),  nullable=True, default='1')
    created_by      = db.Column(db.String(30), nullable=True)
    created_at      = db.Column(db.DateTime,   nullable=True, default=datetime.utcnow)
    updated_by      = db.Column(db.String(30), nullable=True)
    updated_at      = db.Column(db.DateTime,   nullable=True, default=datetime.utcnow)

    address_id      = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    # address         = db.relationship('Address', foreign_keys=address_id)

    # Classe inicializadora do modelo
    def __init__(self, trading_name, company_name, document_number, cnae, ie, im, address_id):
        self.trading_name    = trading_name
        self.company_name    = company_name
        self.document_number = document_number
        self.cnae            = cnae
        self.ie              = ie
        self.im              = im
        self.address_id      = address_id

    # Utilizado para exibir os registros do banco de dados de uma forma mais resumida
    def __repr__(self):
        return "<Provider %r>" % self.id