# controllers/__init__.py
from flask_mail import Mail


 # Configuración de Flask-Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'socialchat2023@gmail.com'  # Tu dirección de correo electrónico
MAIL_PASSWORD = 'xxxxxxxxxxx'  # Tu contraseña de correo electrónico
MAIL_DEFAULT_SENDER = 'socialchat2023@gmail.com'  # Tu dirección de correo electrónico predeterminada
# Crea una instancia de Mail que será utilizada en los controladores
mail = Mail()
