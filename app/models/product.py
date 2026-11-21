import json
from datetime import datetime
from app.database import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=True)             # Ejemplo: "26101"
    title = db.Column(db.String(100), nullable=False)          # Ejemplo: "Netflix Premium"
    category = db.Column(db.String(50), nullable=False)        # 'platform', 'combosDuo', 'combotres'
    price = db.Column(db.Float, nullable=False, default=0.0)    # Ejemplo: 140.00 (Editable desde web)
    currency = db.Column(db.String(10), default="C$")          # Moneda: C$
    period = db.Column(db.String(20), default="mes")           # Periodo: mes
    image_url = db.Column(db.String(255), nullable=False)      # Ruta de la imagen (Estática o Upload)
    _features = db.Column('features', db.Text, nullable=True)  # Guardado internamente como JSON en texto
    is_active = db.Column(db.Boolean, default=True)            # Para activar / desactivar visibilidad
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Propiedad helper para convertir automáticamente JSON a diccionario de Python
    @property
    def features(self):
        if self._features:
            try:
                return json.loads(self._features)
            except json.JSONDecodeError:
                return {}
        return {}

    @features.setter
    def features(self, dict_value):
        if isinstance(dict_value, dict):
            self._features = json.dumps(dict_value, ensure_ascii=False)
        else:
            self._features = json.dumps({})

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "category": self.category,
            "price": f"{self.price:.2f}",
            "currency": self.currency,
            "period": self.period,
            "image": self.image_url,
            "image_1": self.image_1,
            "image_2": self.image_2,
            "features": self.features,
            "is_active": self.is_active
        }
    
    @property
    def image(self):
        return self.image_url

    @property
    def image_1(self):
        return self.features.get('image_1') or self.image_url

    @property
    def image_2(self):
        return self.features.get('image_2')