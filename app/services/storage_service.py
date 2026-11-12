import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app

 #Configuración de extensiones permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'svg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_image(file_storage):
    """
    Recibe un archivo subido por formulario HTML,
    valida la extensión, le asigna un nombre único y seguro
    y lo guarda en app/static/uploads/
    """
    if not file_storage or file_storage.filename == '':
        return None

    if not allowed_file(file_storage.filename):
        raise ValueError("Extensión de archivo no permitida. Usa PNG, JPG, WEBP o SVG.")

    # 1. Extraer la extensión primero de manera segura
    original_filename = secure_filename(file_storage.filename)
    extension = original_filename.rsplit('.', 1)[1].lower()

    # 2. Recomendación: Usar el UUID puro o limpiar caracteres para evitar nombres excesivamente largos
    unique_filename = f"{uuid.uuid4().hex}_{original_filename}"

    # 3. Obtener la ruta desde la configuración de la App de Flask
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)

    
    # 4. Guardar el archivo físicamente
    file_path = os.path.join(upload_folder, unique_filename)
    file_storage.save(file_path)

    # Retorna la ruta relativa para guardar en la BD (ej: "uploads/archivo.png")
    return f"uploads/{unique_filename}"



"""
 uuid(Universally Unique Identifier) es una librería de Python que genera identificadores únicos universales.
"""