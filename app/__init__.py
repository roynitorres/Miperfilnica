from flask import Flask
from flask_login import LoginManager
from app.config import Config
from app.database import db

login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar base de datos
    db.init_app(app)

    # Inicializar Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Inicia sesión para acceder al panel de administración.'
    login_manager.login_message_category = 'warning'

    # Registrar el cargador de usuarios para la sesión
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar Blueprints
    from app.blueprints.public.views import public_bp
    from app.blueprints.auth.views import auth_bp
    from app.blueprints.admin.views import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    # Crear tablas de BD y un usuario admin inicial si no existen
    with app.app_context():
        db.create_all()
        create_default_admin()

    return app

def create_default_admin():
    from app.models.user import User
    if not User.query.filter_by(username='administrador').first():
        admin = User(username='administrador', is_admin=True)
        admin.set_password('@dmin2026*')  # Contraseña inicial predeterminada
        db.session.add(admin)
        db.session.commit()