from app import app, db
from app.models.provider import Provider
from app.models.contact import Contact
from app.models.address import Address
from app.forms.provider import ProviderForm
from app.forms.contact import ContactForm
from app.forms.address import AddressForm
from flask import render_template, redirect, url_for, request, flash

"""
    CLASSE DE CONTROLE DOS FORNECEDORES
"""

@app.route('/provider', methods=['GET'])
def indexProvider():
    providers = Provider.query.all()
    print(providers)
    return render_template('provider/list.html', providers=providers)


@app.route('/provider/new', methods=['GET', 'POST'])
def createProvider():
    providerForm = ProviderForm()
    contactForm  = ContactForm()
    addressForm  = AddressForm()

    if providerForm.validate_on_submit():
        address = Address(
            addressForm.street.data,
            addressForm.number.data,
            addressForm.complement.data,
            addressForm.district.data,
            addressForm.city.data,
            addressForm.state.data,
            addressForm.country.data,
            addressForm.postal_code.data
        )

        db.session.add(address)
        db.session.commit()

        provider = Provider(
            providerForm.trading_name.data,
            providerForm.company_name.data,
            providerForm.document_number.data,
            providerForm.cnae.data,
            providerForm.ie.data,
            providerForm.im.data,
            address.id
        )

        db.session.add(provider)
        db.session.commit()

        contact = Contact(
            contactForm.phone.data,
            contactForm.email.data,
            contactForm.employee_name.data,
            contactForm.employee_department.data,
            provider.id
        )

        db.session.add(contact)
        db.session.commit()

        flash('Fornecedor cadastrado com sucesso!', 'success')
        return redirect(url_for('indexProvider'))
        
    return render_template(
        'provider/form.html', 
        providerForm=providerForm,
        contactForm=contactForm,
        addressForm=addressForm
    )

@app.route('/provider/update/<int:id>', methods=['GET', 'POST'])
def updateProvider(id):
    providerData = Provider.query.get(id)
    addressData  = Address.query.get(providerData.address_id)
    contactData  = Contact.query.filter_by(provider_id=providerData.id).first()

    providerForm = ProviderForm(request.form, obj=providerData)
    contactForm  = ContactForm(request.form,  obj=contactData)
    addressForm  = AddressForm(request.form,  obj=addressData)

    if providerForm.validate_on_submit():
        addressData.street      = addressForm.street.data
        addressData.number      = addressForm.number.data
        addressData.complement  = addressForm.complement.data
        addressData.district    = addressForm.district.data
        addressData.city        = addressForm.city.data
        addressData.state       = addressForm.state.data
        addressData.country     = addressForm.country.data
        addressData.postal_code = addressForm.postal_code.data

        providerData.trading_name    = providerForm.trading_name.data
        providerData.company_name    = providerForm.company_name.data
        providerData.document_number = providerForm.document_number.data
        providerData.cnae            = providerForm.cnae.data
        providerData.ie              = providerForm.ie.data
        providerData.im              = providerForm.im.data
        providerData.address_id      = addressData.id

        contactData.phone               = contactForm.phone.data
        contactData.email               = contactForm.email.data
        contactData.employee_name       = contactForm.employee_name.data
        contactData.employee_department = contactForm.employee_department.data
        contactData.provider_id         = providerData.id

        db.session.commit()
        flash('Fornecedor atualizado com sucesso!', 'success')
        return redirect(url_for('indexProvider'))
        
    return render_template(
        'provider/form.html', 
        providerForm=providerForm,
        contactForm=contactForm,
        addressForm=addressForm
    )

@app.route('/provider/delete/<int:id>', methods=['GET'])
def deleteProvider(id):
    providerData  = Provider.query.get(id)
    addressData   = Address.query.get(providerData.address_id)
    contactData   = Contact.query.filter_by(provider_id=providerData.id)

    db.session.delete(providerData)
    db.session.delete(addressData)

    for c in contactData:
        db.session.delete(c)

    db.session.commit()
    return redirect(url_for('indexProvider'))