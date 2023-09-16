from collections import OrderedDict
from ..database import DatabaseConnection

class Servidor:
    def __init__(self,id_servidor=None, nombre=None, propietario_id=None, icono_serv=None):
        self.id_servidor = id_servidor
        self.nombre = nombre
        self.propietario_id = propietario_id
        self.icono_serv = icono_serv

    def serializar(self):
        # Serializa el objeto Servidor en un diccionario
        servidor_dict = OrderedDict()
        servidor_dict['id_servidor'] = self.id_servidor
        servidor_dict['nombre'] = self.nombre
        servidor_dict['propietario_id'] = self.propietario_id
        servidor_dict['icono_serv'] = self.icono_serv
        # Serializar el OrderedDict a JSON
        return servidor_dict

    @classmethod
    def obtener_servidores_por_usuario(cls, usuario_id):
        # Implementa la lógica para obtener todos los servidores de un usuario
        # Consulta la tabla intermedia para encontrar los servidores relacionados
        # con el usuario identificado por 'usuario_id'
        consulta = "SELECT s.* FROM socialchat.servidores s INNER JOIN socialchat.usuarios_servidores us ON s.id_servidor = us.servidor_id WHERE us.usuario_id = %s"
        valores = (usuario_id,)

        servidores = DatabaseConnection.fetch_all(consulta, params=valores)
        servidores_obj = [Servidor(id_servidor=s[0], nombre=s[1], propietario_id=s[2], icono_serv=s[3]) for s in servidores]
        print(servidores_obj)
        return servidores_obj

    @classmethod
    def crear_servidor(cls, nombre, propietario_id, icono_serv):
        # Implementa la lógica para crear un nuevo servidor
        consulta = "INSERT INTO socialchat.servidores (nombre, propietario_id, icono_serv) VALUES (%s, %s, %s)"
        valores = (nombre, propietario_id, icono_serv)

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            nuevo_servidor = Servidor(id_servidor=cursor.lastrowid, nombre=nombre, propietario_id=propietario_id, icono_serv=icono_serv)
            return nuevo_servidor
        except Exception as e:
            raise Exception("Error al crear el servidor")

    @classmethod
    def eliminar_servidor(cls, servidor_id, usuario_id):
        # Implementa la lógica para eliminar un servidor de la base de datos
        # Asegúrate de verificar si el servidor pertenece al usuario antes de eliminarlo
        consulta = "DELETE FROM socialchat.servidores WHERE id = %s AND propietario_id = %s"
        valores = (servidor_id, usuario_id)

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            if cursor.rowcount == 1:
                return True
            return False
        except Exception as e:
            raise Exception("Error al eliminar el servidor")
        
    @classmethod
    def eliminar_relacion_servidor(cls, servidor_id, usuario_id):
        # Implementa la lógica para eliminar la relación entre un usuario y un servidor
        consulta = "DELETE FROM socialchat.usuarios_servidores WHERE servidor_id = %s AND usuario_id = %s"
        valores = (servidor_id, usuario_id)

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            if cursor.rowcount == 1:
                return True
            return False
        except Exception as e:
            raise Exception("Error al eliminar la relación entre usuario y servidor")    
    
    @classmethod
    def agregar_miembro_al_servidor(cls, servidor_id, usuario_id):
        # Implementa la lógica para agregar al usuario como miembro del servidor
        consulta = "INSERT INTO socialchat.usuarios_servidores (usuario_id, servidor_id) VALUES (%s, %s)"
        valores = (usuario_id, servidor_id)

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            return True
        except Exception as e:
            raise Exception("Error al agregar al usuario como miembro del servidor")
        
    @classmethod
    def unirse_a_servidor(cls, servidor_id, usuario_id):
        # Implementa la lógica para permitir que un usuario se una a un servidor existente
        consulta = "INSERT INTO socialchat.usuarios_servidores (usuario_id, servidor_id) VALUES (%s, %s)"
        valores = (usuario_id, servidor_id)

        try:
           cursor = DatabaseConnection.execute_query(consulta, params=valores)
           return True
        except Exception as e:
         raise Exception("Error al unirse al servidor")   

    @classmethod
    def es_miembro_del_servidor(cls, servidor_id, usuario_id):
        # Verificar si un usuario es miembro de un servidor
        consulta = " SELECT 1 FROM socialchat.usuarios_servidores  WHERE servidor_id = %s AND usuario_id = %s"
        valores = (servidor_id, usuario_id)

        resultado = DatabaseConnection.fetch_one(consulta, params=valores)
        return resultado is not None

    
    
    @classmethod
    def obtener_todos_los_servidores(cls):
        # Obtener todos los servidores de la base de datos
        consulta = "SELECT * FROM socialchat.servidores"
    
        servidores = DatabaseConnection.fetch_all(consulta)
    
        servidores_obj = []
        for servidor in servidores:
            id, nombre, propietario_id, icono_serv = servidor
            servidores_obj.append(Servidor(id_servidor=id, nombre=nombre, propietario_id=propietario_id, icono_serv=icono_serv))

        return servidores_obj

    @classmethod
    def buscar_servidores_por_nombre(cls, nombre):
        # Buscar servidores por nombre
        consulta = "SELECT * FROM socialchat.servidores WHERE nombre LIKE %s"
        valores = (f'%{nombre}%',)
    
        servidores = DatabaseConnection.fetch_all(consulta, params=valores)
    
        servidores_obj = []
        for servidor in servidores:
            id, nombre, propietario_id, icono_serv = servidor
            servidores_obj.append(Servidor(id_servidor=id, nombre=nombre, propietario_id=propietario_id, icono_serv=icono_serv))

            return servidores_obj
     

