import os

# Ruta base del proyecto
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    # Clave secreta para sesiones seguras y formularios
    SECRET_KEY = os.environ.get('SECRET_KEY', 'miperfilnica_secret_key_2026_change_me')
    
    # Configuración de la base de datos SQLite (se guardará en la carpeta instance/)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'miperfilnica.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Carpeta donde se guardarán las imágenes subidas desde el panel web
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'uploads')
    
    # Tamaño máximo permitido para subir archivos (ejemplo: 5 MB)
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024