import json
import random
import string
from collections import OrderedDict
from ..database import DatabaseConnection

class Usuario:
    def __init__(self, id=None, nombre=None, apellido=None, email=None, contraseña=None, fecha_nacimiento=None, avatar=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento
        self.avatar = avatar

    def serializar(self):
        # Serializa el objeto Usuario en un diccionario
        usuario_dict = OrderedDict()
        usuario_dict['id'] = self.id
        usuario_dict['nombre'] = self.nombre
        usuario_dict['apellido'] = self.apellido
        usuario_dict['email']= self.email
        usuario_dict['password']= self.contraseña
        usuario_dict['fecha_nacimiento']= str(self.fecha_nacimiento)  # Convertir fecha a cadena
        usuario_dict['avatar']= self.avatar
        # Serializar el OrderedDict a JSON
        #return usuario_dict
        return usuario_dict
        

    def agregar_usuario(usuario):
        # Insertar un nuevo usuario en la base de datos
        consulta = "INSERT INTO socialchat.usuarios (nombre, apellido, email, contraseña, fecha_nacimiento, avatar) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (usuario.nombre, usuario.apellido, usuario.email, usuario.contraseña, usuario.fecha_nacimiento, usuario.avatar)
        
        cursor = DatabaseConnection.execute_query(consulta, params=valores)
        usuario.id = cursor.lastrowid  # Obtener el ID generado automáticamente

    def obtener_usuario_por_id(id):
        # Buscar un usuario por ID en la base de datos
        consulta = "SELECT * FROM socialchat.usuarios WHERE id = %s"
        valores = (id,)
        
        usuario = DatabaseConnection.fetch_one(consulta, params=valores)
        
        if usuario:
            id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar = usuario
            return Usuario(id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar).serializar()
        
        return None

    def obtener_todos_los_usuarios():
        # Obtener todos los usuarios de la base de datos
        consulta = "SELECT * FROM socialchat.usuarios"
        
        usuarios = DatabaseConnection.fetch_all(consulta)
        
        usuarios_serializados = []
        for usuario in usuarios:
            id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar = usuario
            usuarios_serializados.append(Usuario(id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar).serializar())
        
        return usuarios_serializados

    def eliminar_usuario_por_id(id):
        # Eliminar un usuario por ID de la base de datos
        consulta = "DELETE FROM socialchat.usuarios WHERE id = %s"
        valores = (id,)
        
        DatabaseConnection.execute_query(consulta, params=valores)

    # Cerrar la conexión cuando hayas terminado
    DatabaseConnection.close_connection()

    @classmethod
    def obtener_usuario_por_email(cls, email):
    # Buscar un usuario por dirección de correo electrónico en la base de datos
     consulta = "SELECT * FROM socialchat.usuarios WHERE email = %s"
     valores = (email,)
            
     usuario = DatabaseConnection.fetch_one(consulta, params=valores)
            
     if usuario:
        id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar = usuario
        return Usuario(id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar).serializar()
            
     return None
    
    @classmethod
    def obtener_usuario_por_email_servidores(cls, email):
    # Buscar un usuario por dirección de correo electrónico en la base de datos
     consulta = "SELECT * FROM socialchat.usuarios WHERE email = %s"
     valores = (email,)
            
     usuario = DatabaseConnection.fetch_one(consulta, params=valores)
            
     if usuario:
        id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar = usuario
        return Usuario(id, nombre, apellido, email, contraseña, fecha_nacimiento, avatar)
            
     return None

    def actualizar_usuario(self):
        # Verificar si el usuario tiene un ID válido
        if self.id is None:
            raise ValueError("El usuario debe tener un ID válido para actualizarlo")

        # Construir la consulta SQL de actualización
        consulta = "UPDATE socialchat.usuarios SET nombre = %s, apellido = %s,contraseña = %s, fecha_nacimiento = %s, avatar = %s WHERE id = %s"

        # Valores a actualizar en la base de datos
        valores = (self.nombre, self.apellido,self.contraseña, self.fecha_nacimiento, self.avatar, self.id)

        # Ejecutar la consulta SQL de actualización
        DatabaseConnection.execute_query(consulta, params=valores)

        # Confirmar la transacción
        DatabaseConnection.commit()

    @classmethod
    def generar_nueva_contraseña(cls):
        # Genera una nueva contraseña aleatoria
        longitud = 12  # Puedes ajustar la longitud según tus necesidades
        caracteres = string.ascii_letters + string.digits  # Letras y números
        nueva_contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return nueva_contraseña

    def actualizar_contraseña(self, email, nueva_contraseña):
        # Actualiza la contraseña del usuario en la base de datos
        consulta = "UPDATE socialchat.usuarios SET contraseña = %s WHERE email = %s"
        valores = (nueva_contraseña,email)
        DatabaseConnection.execute_query(consulta, params=valores)
        DatabaseConnection.commit()        