from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.services.product_service import (
    get_all_products_admin,
    get_product_by_id,
    create_product,
    update_product_price_and_image,
    toggle_product_active
)
from app.services.storage_service import save_uploaded_image

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    products = get_all_products_admin()
    return render_template('admin/dashboard.html', products=products)

@admin_bp.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        price = request.form.get('price')
        code = request.form.get('code')
        currency = request.form.get('currency', 'C$')

        # Procesar Imagen 1 (principal)
        image_file = request.files.get('image')
        image_url = "imagenes/Individuales/1.svg" # Imagen por defecto si no sube una
        if image_file and image_file.filename != '':
            try:
                image_url = save_uploaded_image(image_file)
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('admin/product_form.html', action='Crear')

        features = {'image_1': image_url}

        # Procesar Imagen 2 (segunda plataforma para combos duo)
        image_file_2 = request.files.get('image_2')
        if image_file_2 and image_file_2.filename != '':
            try:
                image_2_url = save_uploaded_image(image_file_2)
                features['image_2'] = image_2_url
            except ValueError as e:
                flash(f'Error en Imagen 2: {str(e)}', 'danger')
                return render_template('admin/product_form.html', action='Crear')

        create_product(
            title=title,
            category=category,
            price=price,
            image_url=image_url,
            code=code,
            currency=currency,
            features=features
        )
        flash('Producto creado exitosamente.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/product_form.html', action='Crear', product=None)

@admin_bp.route('/product/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        
        # Verificar si subió una nueva Imagen 1
        image_file = request.files.get('image')
        new_image_url = None
        if image_file and image_file.filename != '':
            try:
                new_image_url = save_uploaded_image(image_file)
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('admin/product_form.html', action='Editar', product=product)

        # Verificar si subió una nueva Imagen 2
        image_file_2 = request.files.get('image_2')
        features_update = {}
        if new_image_url:
            features_update['image_1'] = new_image_url
            
        if image_file_2 and image_file_2.filename != '':
            try:
                new_image_2_url = save_uploaded_image(image_file_2)
                features_update['image_2'] = new_image_2_url
            except ValueError as e:
                flash(f'Error en Imagen 2: {str(e)}', 'danger')
                return render_template('admin/product_form.html', action='Editar', product=product)

        update_product_price_and_image(
            product_id=product.id,
            new_price=price,
            new_image_url=new_image_url,
            title=title,
            features=features_update if features_update else None
        )
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/product_form.html', action='Editar', product=product)

@admin_bp.route('/product/toggle/<int:product_id>', methods=['POST'])
@login_required
def toggle_product(product_id):
    is_active = toggle_product_active(product_id)
    estado = "activado" if is_active else "desactivado"
    flash(f'Producto {estado} correctamente.', 'info')
    return redirect(url_for('admin.dashboard'))