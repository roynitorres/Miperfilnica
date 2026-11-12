from app import create_app
from app.database import db
from app.models.product import Product

app = create_app()

with app.app_context():
    # Solo agrega si no hay productos
    if Product.query.count() == 0:
        p1 = Product(
            code="26101",
            title="Netflix Premium",
            category="platform",
            price=140.00,
            currency="C$",
            period="mes",
            image_url="imagenes/Individuales/1.svg",
            features={"Calidad": "4K Ultra HD", "Pantallas": "1 pantalla a la vez"}
        )
        p2 = Product(
            code="261003",
            title="Disney+ Standard",
            category="platform",
            price=130.00,
            currency="C$",
            period="mes",
            image_url="imagenes/Individuales/3.svg",
            features={"Calidad": "HD / Full HD", "Conexión": "1 dispositivo a la vez"}
        )
        p3 = Product(
            code="261005",
            title="HBO Max",
            category="platform",
            price=90.00,
            currency="C$",
            period="mes",
            image_url="imagenes/Individuales/5.svg",
            features={"Calidad": "4K Ultra HD", "Conexión": "1 dispositivo a la vez"}
        )
        db.session.add_all([p1, p2, p3])
        db.session.commit()
        print(" ¡Productos de prueba insertados con éxito!")
    else:
        print("ℹ La base de datos ya contiene productos.")