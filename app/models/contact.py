from app import db
from datetime import datetime

"""
    CLASSE DE MODELO DO CONTACT
    Exemplo de desenvolvimento:
        http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#simple-relationships
"""

class Contact(db.Model):
    __tablename__ = "contact"

    id                  = db.Column(db.Integer,    primary_key=True)
    phone               = db.Column(db.String(30), nullable=False)
    email               = db.Column(db.String(30), nullable=False)
    employee_name       = db.Column(db.String(30), nullable=False)
    employee_department = db.Column(db.String(30), nullable=False)
    status              = db.Column(db.String(1),  nullable=False, default='1')
    created_by          = db.Column(db.String(30), nullable=True)
    created_at          = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow)
    updated_by          = db.Column(db.String(30), nullable=True)
    updated_at          = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow)

    provider_id         = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=True)
    # contact             = db.relationship('Provider', foreign_keys=contact_id)

    # Classe inicializadora do modelo
    def __init__(self, phone, email, employee_name, employee_department, provider_id):
        self.phone               = phone
        self.email               = email
        self.employee_name       = employee_name
        self.employee_department = employee_department
        self.provider_id         = provider_id
        
    # Utilizado para exibir os registros do banco de dados de uma forma mais resumida
    def __repr__(self):
        return "<Contact %r>" % self.id