from collections import OrderedDict
from datetime import datetime, timedelta
from ..database import DatabaseConnection
from ..models.exceptions import MensajeNotFound

class Mensaje:
    def __init__(self, id_mensaje=None, contenido=None, canal_id=None, usuario_id=None, fecha_envio=None):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.canal_id = canal_id
        self.usuario_id = usuario_id
        self.fecha_envio = fecha_envio

    def serializar(self):
        # Serializa el objeto Mensaje en un diccionario
        mensaje_dict = OrderedDict()
        mensaje_dict['id_mensaje'] = self.id_mensaje
        mensaje_dict['contenido'] = self.contenido
        mensaje_dict['canal_id'] = self.canal_id
        mensaje_dict['usuario_id'] = self.usuario_id
        mensaje_dict['fecha_envio'] = self.fecha_envio.isoformat()  # ISO 8601 para la fecha
        # Serializar el OrderedDict a JSON
        return mensaje_dict

    @classmethod
    def obtener_mensaje_por_id(cls, mensaje_id):
        # Implementa la lógica para obtener un mensaje por su ID
        consulta = "SELECT * FROM socialchat.mensajes WHERE id_mensaje = %s"
        valores = (mensaje_id,)

        mensaje = DatabaseConnection.fetch_one(consulta, params=valores)

        if mensaje:
            return Mensaje(id_mensaje=mensaje[0], contenido=mensaje[1], canal_id=mensaje[2], usuario_id=mensaje[3], fecha_envio=mensaje[4])
        else:
            raise MensajeNotFound(mensaje_id)

    @classmethod
    def obtener_mensajes_por_canal(cls, canal_id):
        # Implementa la lógica para obtener todos los mensajes de un canal
        consulta = "SELECT * FROM socialchat.mensajes WHERE canal_id = %s"
        valores = (canal_id,)

        mensajes = DatabaseConnection.fetch_all(consulta, params=valores)
        mensajes_obj = [Mensaje(id_mensaje=m[0], contenido=m[1], canal_id=m[2], usuario_id=m[3], fecha_envio=m[4]) for m in mensajes]
        return mensajes_obj

    @classmethod
    def crear_mensaje(cls, contenido, canal_id, usuario_id):
        # Implementa la lógica para crear un nuevo mensaje en un canal
        consulta = "INSERT INTO socialchat.mensajes (contenido, canal_id, usuario_id, fecha_envio) VALUES (%s, %s, %s, %s)"
        valores = (contenido, canal_id, usuario_id, datetime.now())

        try:
            cursor = DatabaseConnection.execute_query(consulta, params=valores)
            nuevo_mensaje = Mensaje(id_mensaje=cursor.lastrowid, contenido=contenido, canal_id=canal_id, usuario_id=usuario_id, fecha_envio=datetime.now())
            return nuevo_mensaje
        except Exception as e:
            raise Exception("Error al crear el mensaje")

    @classmethod
    def borrar_mensaje(cls, mensaje_id, usuario_id):
        # Implementa la lógica para borrar un mensaje por su ID si el usuario es el autor y el mensaje es reciente
        mensaje = cls.obtener_mensaje_por_id(mensaje_id)

        if mensaje.usuario_id == usuario_id:
            # Verifica si el mensaje es reciente (dentro de los últimos 60 segundos)
            tiempo_actual = datetime.now()
            tiempo_diferencia = tiempo_actual - mensaje.fecha_envio
            if tiempo_diferencia.total_seconds() <= 60:
                consulta = "DELETE FROM socialchat.mensajes WHERE id_mensaje = %s"
                valores = (mensaje_id,)
                try:
                    DatabaseConnection.execute_query(consulta, params=valores)
                    return True
                except Exception as e:
                    raise Exception("Error al borrar el mensaje")
            else:
                raise Exception("El mensaje no se puede borrar porque ha pasado más de 1 minuto desde que se envió")
        else:
            raise Exception("No tienes permiso para borrar este mensaje")


