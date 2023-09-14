import json
from database import DatabaseConnection

class Usuario:
    def __init__(self, nombre, apellido, email, contraseña, fecha_nacimiento, avatar=None):
        self.id = None
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento
        self.avatar = avatar

    def serializar(self):
        # Serializa el objeto Usuario en un diccionario
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'fecha_nacimiento': str(self.fecha_nacimiento),  # Convertir fecha a cadena
            'avatar': self.avatar
        }

def agregar_usuario(usuario):
    # Insertar un nuevo usuario en la base de datos
    consulta = "INSERT INTO usuarios (nombre, apellido, email, contraseña, fecha_nacimiento, avatar) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (usuario.nombre, usuario.apellido, usuario.email, usuario.contraseña, usuario.fecha_nacimiento, usuario.avatar)
    
    cursor = DatabaseConnection.execute_query(consulta, params=valores)
    usuario.id = cursor.lastrowid  # Obtener el ID generado automáticamente

def obtener_usuario_por_id(id):
    # Buscar un usuario por ID en la base de datos
    consulta = "SELECT * FROM usuarios WHERE id = %s"
    valores = (id,)
    
    usuario = DatabaseConnection.fetch_one(consulta, params=valores)
    
    if usuario:
        id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar = usuario
        return Usuario(nombre, apellido, email, contraseña, fecha_nacimiento, avatar).serializar()
    
    return None

def obtener_todos_los_usuarios():
    # Obtener todos los usuarios de la base de datos
    consulta = "SELECT * FROM usuarios"
    
    usuarios = DatabaseConnection.fetch_all(consulta)
    
    usuarios_serializados = []
    for usuario in usuarios:
        id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar = usuario
        usuarios_serializados.append(Usuario(nombre, apellido, email, contraseña, fecha_nacimiento, avatar).serializar())
    
    return usuarios_serializados

def eliminar_usuario_por_id(id):
    # Eliminar un usuario por ID de la base de datos
    consulta = "DELETE FROM usuarios WHERE id = %s"
    valores = (id,)
    
    DatabaseConnection.execute_query(consulta, params=valores)

# Cerrar la conexión cuando hayas terminado
DatabaseConnection.close_connection()
