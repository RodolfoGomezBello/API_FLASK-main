
from collections import OrderedDict
from ..database import DatabaseConnection

class Canal:
    def __init__(self, id_canal=None, nombre=None, servidor_id=None, creador_id=None, icono=None):
        self.id_canal = id_canal
        self.nombre = nombre
        self.servidor_id = servidor_id
        self.creador_id = creador_id
        self.icono = icono

    def serializar(self):
        # Serializa el objeto Canal en un diccionario
        canal_dict = OrderedDict()
        canal_dict['id_canal'] = self.id_canal
        canal_dict['nombre'] = self.nombre
        canal_dict['servidor_id'] = self.servidor_id
        canal_dict['creador_id'] = self.creador_id
        canal_dict['icono'] = self.icono
        # Serializar el OrderedDict a JSON
        return canal_dict

    @classmethod
    def obtener_canales_por_servidor(cls, servidor_id):
        # Implementa la lógica para obtener todos los canales de un servidor
        consulta = "SELECT * FROM socialchat.canales WHERE servidor_id = %s"
        valores = (servidor_id,)

        canales = DatabaseConnection.fetch_all(consulta, params=valores)
        canales_obj = [Canal(id_canal=c[0], nombre=c[1], servidor_id=c[2], creador_id=c[3], icono=c[4]) for c in canales]
        return canales_obj

    @classmethod
    def crear_canal(cls, nombre, servidor_id, creador_id, icono):
        # Implementa la lógica para crear un nuevo canal en un servidor
        consulta = "INSERT INTO socialchat.canales (nombre, servidor_id, creador_id, icono) VALUES (%s, %s, %s, %s)"
        valores = (nombre, servidor_id, creador_id, icono)

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            nuevo_canal = Canal(id_canal=cursor.lastrowid, nombre=nombre, servidor_id=servidor_id, creador_id=creador_id, icono=icono)
            return nuevo_canal
        except Exception as e:
            raise Exception("Error al crear el canal")

    """
    Aplicar estos metodos si es que no se quiere que los usuarios participen en todos los canales
    y quieran elegir en que canales participar, crear tabla usuarios_canales
    @classmethod
    def unirse_a_canal(cls, canal_id, usuario_id):
        # Implementa la lógica para permitir que un usuario se una a un canal existente
        consulta = "INSERT INTO socialchat.usuarios_canales (usuario_id, canal_id) VALUES (%s, %s)"
        valores = (usuario_id, canal_id)

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            return True
        except Exception as e:
            raise Exception("Error al unirse al canal")
    
    @classmethod
    def obtener_canales_usuario(cls, usuario_id, servidor_id):
        # Implementa la lógica para obtener todos los canales a los que un usuario pertenece en un servidor
        consulta = "SELECT c.* FROM socialchat.canales c INNER JOIN socialchat.usuarios_canales uc ON c.id_canal = uc.canal_id WHERE uc.usuario_id = %s AND c.servidor_id = %s"
        valores = (usuario_id, servidor_id)

        canales = DatabaseConnection.fetch_all(consulta, params=valores)
        canales_obj = [Canal(id_canal=c[0], nombre=c[1], servidor_id=c[2], creador_id=c[3], icono=c[4]) for c in canales]
        return canales_obj

    @classmethod
    def verificar_pertenencia_a_canal(cls, canal_id, usuario_id):
        # Verificar si un usuario es miembro de un canal
        consulta = "SELECT 1 FROM socialchat.usuarios_canales WHERE canal_id = %s AND usuario_id = %s"
        valores = (canal_id, usuario_id)

        resultado = DatabaseConnection.fetch_one(consulta, params=valores)
        return resultado is not None
    """
    @classmethod
    def obtener_todos_los_canales(cls):
        # Obtener todos los canales de la base de datos
        consulta = "SELECT * FROM socialchat.canales"

        canales = DatabaseConnection.fetch_all(consulta)

        canales_obj = [Canal(id_canal=c[0], nombre=c[1], servidor_id=c[2], creador_id=c[3], icono=c[4]) for c in canales]
        return canales_obj

    @classmethod
    def buscar_canales_por_nombre(cls, nombre):
        # Buscar canales por nombre
        consulta = "SELECT * FROM socialchat.canales WHERE nombre LIKE %s"
        valores = (f'%{nombre}%',)

        canales = DatabaseConnection.fetch_all(consulta, params=valores)

        canales_obj = [Canal(id_canal=c[0], nombre=c[1], servidor_id=c[2], creador_id=c[3], icono=c[4]) for c in canales]
        return canales_obj


