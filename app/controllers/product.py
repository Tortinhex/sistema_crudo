from app import app, db
from flask import render_template, redirect, url_for, request, flash
from app.forms.product import ProductForm
from app.forms.provider import ProviderForm
from app.models.product import Product
from app.models.provider import Provider

"""
    CLASSE DE CONTROLE DOS PRODUTOS
"""

@app.route('/product', methods=['GET'])
def indexProduct():
    products = Product.query.all()
    return render_template('product/list.html', products=products)


@app.route('/product/new', methods=['GET', 'POST'])
def createProduct():
    productForm  = ProductForm()
    providerForm = ProviderForm()
    choices = [(p.id, p.trading_name) for p in Provider.query.order_by('trading_name')]
    choices.insert(0, ('0', 'Selecione'))
    productForm.provider.choices = choices
    providers = Provider.query.all()

    if productForm.validate_on_submit():

        provider_id = None
        if "0" != productForm.provider.data:
            provider_id = productForm.provider.data

        product = Product(
            productForm.product_name.data,
            productForm.serial_number.data,
            productForm.branch.data,
            productForm.model.data,
            productForm.quantity.data,
            productForm.category.data,
            productForm.description.data,
            productForm.coast.data,
            productForm.status.data,
            provider_id
        )

        db.session.add(product)
        db.session.commit()
        flash('Produto criado com sucesso!', 'success')

        return redirect(url_for('indexProduct'))

    return render_template(
        'product/form.html', 
        productForm=productForm,
        providerForm=providerForm,
        providers=providers
    )


@app.route('/product/update/<int:id>', methods=['GET', 'POST'])
def updateProduct(id):
    productData  = Product.query.get(id)
    productForm  = ProductForm(request.form, obj=productData, provider=productData.provider_id)
    providerForm = ProviderForm()
    choices = [(p.id, p.trading_name) for p in Provider.query.order_by('trading_name')]
    choices.insert(0, ('0', 'Selecione'))
    productForm.provider.choices = choices
    providers = Provider.query.all()

    if "POST" == request.method:
        if productForm.validate_on_submit():
            productData.product_name  = productForm.product_name.data
            productData.serial_number = productForm.serial_number.data
            productData.branch        = productForm.branch.data
            productData.model         = productForm.model.data
            productData.category      = productForm.category.data
            productData.description   = productForm.description.data
            productData.coast         = productForm.coast.data
            productData.status        = productForm.status.data
            productData.provider_id   = productForm.provider.data
            db.session.commit()

            flash('Produto atualizado com sucesso!', 'success')
            return redirect(url_for('indexProduct'))

    return render_template(
        'product/form.html', 
        productForm=productForm,
        providerForm=providerForm,
        providers=providers
    )


@app.route('/product/delete/<int:id>', methods=['GET'])
def deleteProduct(id):
    productData  = Product.query.get(id)
    db.session.delete(productData)

    db.session.commit()
    flash('Produto deletado com sucesso!', 'success')

    return redirect(url_for('indexProduct'))



    # form = ProductForm()
    # if form.validate_on_submit():
    #     print(form.branch.data)
    # return render_template('product/form.html', form=form)

# @app.route('/teste')
# def teste():
#     i = Product("Caneta", "D3UI3N", "BIC", "JHF3J893", "Caneta de material escolar", "20.00")
#     db.session.add(i)
#     db.session.commit()
#     return "hello"