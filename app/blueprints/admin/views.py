from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.services.product_service import (
    get_all_products_admin,
    get_product_by_id,
    get_products_by_category,
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
    platforms = get_products_by_category('platform')
    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        price = request.form.get('price')
        code = request.form.get('code')
        currency = request.form.get('currency', 'C$')

        platform_1_id = request.form.get('platform_1_id')
        platform_2_id = request.form.get('platform_2_id')
        platform_3_id = request.form.get('platform_3_id')
        original_price = request.form.get('original_price')
        discount = request.form.get('discount')
        inherited_image_1 = request.form.get('inherited_image_1')
        inherited_image_2 = request.form.get('inherited_image_2')
        inherited_image_3 = request.form.get('inherited_image_3')

        # Procesar Imagen 1 (principal)
        image_file = request.files.get('image')
        image_url = inherited_image_1 or "imagenes/Individuales/1.svg"
        if image_file and image_file.filename != '':
            try:
                image_url = save_uploaded_image(image_file)
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('admin/product_form.html', action='Crear', platforms=platforms)

        features = {'image_1': image_url}
        if platform_1_id:
            features['platform_1_id'] = platform_1_id
        if platform_2_id:
            features['platform_2_id'] = platform_2_id
        if platform_3_id:
            features['platform_3_id'] = platform_3_id
        if original_price:
            try:
                features['original_price'] = float(original_price)
            except ValueError:
                pass
        if discount:
            try:
                features['discount'] = float(discount)
            except ValueError:
                pass

        # Procesar Imagen 2 (segunda plataforma para combos duo y trío)
        image_file_2 = request.files.get('image_2')
        image_2_url = inherited_image_2 or None
        if image_file_2 and image_file_2.filename != '':
            try:
                image_2_url = save_uploaded_image(image_file_2)
            except ValueError as e:
                flash(f'Error en Imagen 2: {str(e)}', 'danger')
                return render_template('admin/product_form.html', action='Crear', platforms=platforms)

        if image_2_url:
            features['image_2'] = image_2_url

        # Procesar Imagen 3 (tercera plataforma para combos trío)
        image_file_3 = request.files.get('image_3')
        image_3_url = inherited_image_3 or None
        if image_file_3 and image_file_3.filename != '':
            try:
                image_3_url = save_uploaded_image(image_file_3)
            except ValueError as e:
                flash(f'Error en Imagen 3: {str(e)}', 'danger')
                return render_template('admin/product_form.html', action='Crear', platforms=platforms)

        if image_3_url:
            features['image_3'] = image_3_url

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

    return render_template('admin/product_form.html', action='Crear', product=None, platforms=platforms)

@admin_bp.route('/product/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = get_product_by_id(product_id)
    platforms = get_products_by_category('platform')
    if not product:
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')

        platform_1_id = request.form.get('platform_1_id')
        platform_2_id = request.form.get('platform_2_id')
        platform_3_id = request.form.get('platform_3_id')
        original_price = request.form.get('original_price')
        discount = request.form.get('discount')
        inherited_image_1 = request.form.get('inherited_image_1')
        inherited_image_2 = request.form.get('inherited_image_2')
        inherited_image_3 = request.form.get('inherited_image_3')

        features_update = {}
        if platform_1_id:
            features_update['platform_1_id'] = platform_1_id
        if platform_2_id:
            features_update['platform_2_id'] = platform_2_id
        if platform_3_id:
            features_update['platform_3_id'] = platform_3_id
        if original_price:
            try:
                features_update['original_price'] = float(original_price)
            except ValueError:
                pass
        if discount:
            try:
                features_update['discount'] = float(discount)
            except ValueError:
                pass
        
        # Verificar si subió una nueva Imagen 1
        image_file = request.files.get('image')
        new_image_url = None
        if image_file and image_file.filename != '':
            try:
                new_image_url = save_uploaded_image(image_file)
                features_update['image_1'] = new_image_url
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('admin/product_form.html', action='Editar', product=product, platforms=platforms)
        elif inherited_image_1 and not product.image_1:
            new_image_url = inherited_image_1
            features_update['image_1'] = inherited_image_1

        # Verificar si subió una nueva Imagen 2
        image_file_2 = request.files.get('image_2')
        if image_file_2 and image_file_2.filename != '':
            try:
                new_image_2_url = save_uploaded_image(image_file_2)
                features_update['image_2'] = new_image_2_url
            except ValueError as e:
                flash(f'Error en Imagen 2: {str(e)}', 'danger')
                return render_template('admin/product_form.html', action='Editar', product=product, platforms=platforms)
        elif inherited_image_2 and not product.image_2:
            features_update['image_2'] = inherited_image_2

        # Verificar si subió una nueva Imagen 3
        image_file_3 = request.files.get('image_3')
        if image_file_3 and image_file_3.filename != '':
            try:
                new_image_3_url = save_uploaded_image(image_file_3)
                features_update['image_3'] = new_image_3_url
            except ValueError as e:
                flash(f'Error en Imagen 3: {str(e)}', 'danger')
                return render_template('admin/product_form.html', action='Editar', product=product, platforms=platforms)
        elif inherited_image_3 and not product.image_3:
            features_update['image_3'] = inherited_image_3

        update_product_price_and_image(
            product_id=product.id,
            new_price=price,
            new_image_url=new_image_url,
            title=title,
            features=features_update if features_update else None
        )
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/product_form.html', action='Editar', product=product, platforms=platforms)

@admin_bp.route('/product/toggle/<int:product_id>', methods=['POST'])
@login_required
def toggle_product(product_id):
    is_active = toggle_product_active(product_id)
    estado = "activado" if is_active else "desactivado"
    flash(f'Producto {estado} correctamente.', 'info')
    return redirect(url_for('admin.dashboard'))