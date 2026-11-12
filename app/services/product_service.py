from app.database import db
from app.models.product import Product

def get_products_by_category(category=None):
    """Obtiene productos activos filtrados por categoría (o todos)"""
    query = Product.query.filter_by(is_active=True)
    if category:
        query = query.filter_by(category=category)
    return query.all()

def get_product_by_id(product_id):
    """Busca un producto por su ID único"""
    return Product.query.get(product_id)

def get_all_products_admin():
    """Obtiene TODOS los productos para el panel de administración"""
    return Product.query.order_by(Product.category, Product.id).all()

def create_product(title, category, price, image_url, code=None, currency="C$", period="mes", features=None):
    """Crea un nuevo producto en la base de datos"""
    product = Product(
        title=title,
        category=category,
        price=float(price),
        image_url=image_url,
        code=code,
        currency=currency,
        period=period
    )
    if features:
        product.features = features
    
    db.session.add(product)
    db.session.commit()
    return product

def update_product_price_and_image(product_id, new_price=None, new_image_url=None, title=None, features=None):
    """Actualiza dinámicamente precio, imagen y datos del producto"""
    product = Product.query.get(product_id)
    if not product:
        return None

    if new_price is not None:
        product.price = float(new_price)
    
    if new_image_url:
        product.image_url = new_image_url

    if title:
        product.title = title

    if features is not None:
        product.features = features

    db.session.commit()
    return product

def toggle_product_active(product_id):
    """Activa o desactiva la visibilidad de un producto"""
    product = Product.query.get(product_id)
    if product:
        product.is_active = not product.is_active
        db.session.commit()
        return product.is_active
    return False