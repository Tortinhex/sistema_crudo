from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# APP
app = Flask(__name__)
app.config.from_object('config')

# DB
db  = SQLAlchemy(app)

# Cuida das migracoes do DB
migrate = Migrate(app, db)

# Cuida dos comandos de inicializacao
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import address, contact, product, provider

from app.routes import routes
from app.controllers import product, provider