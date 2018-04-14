from app import app, db
from flask import render_template
from app.forms.product import ProductForm
from app.models.product import Product

@app.route("/")
def index():
    return render_template('home/index.html')





# @app.route("/index/<user>")
# @app.route("/", defaults={'user': None})
# def index(user):
#     return render_template('home/index.html', user=user)
    
# @app.route("/teste")
# @app.route("/teste/<name>")
# def teste(name=None):
#     if name:
#         return "Olá, %s!" % name
#     else:
#         return "Olá, usuário"

# @app.route("/teste2", defaults={'name': None})
# @app.route("/teste2/<name>")
# def teste2(name):
#     if name:
#         return "Olá, %s!" % name
#     else:
#         return "Olá, usuário"

# @app.route("/teste3/<int:id>")
# def teste3(id):
#     return "Olá, usuário %d" % id

# @app.route("/teste4/", methods=['GET'])
# def teste4():
#     return "Olá, GET"