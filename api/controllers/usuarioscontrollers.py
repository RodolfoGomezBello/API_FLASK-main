from ..models.usuariosmodels import Usuario #, agregar_usuario,obtener_usuario_por_email ,obtener_usuario_por_id, obtener_todos_los_usuarios, eliminar_usuario_por_id
from flask import request, session, jsonify
from ..models.exceptions import InvalidDataError, UsuarioNotFound, MensajeNotFound
from ..models.servidoresmodels import Servidor
from ..models.canalesmodels import Canal
from ..models.mensajesmodels import Mensaje
from datetime import datetime, timedelta


class UsuarioController:

    """Usuario controller class"""

    @classmethod
    def create(cls):
        data = request.json

        # Validación de correo electrónico único
        if cls.email_exists(data['email']):
            return {'error': 'El correo electrónico ya está en uso'}, 400

        # Validaciones de otros datos del usuario
        if len(data.get('nombre', '')) < 3:
            return {'error': 'El nombre debe tener al menos tres caracteres'}, 400

        # Más validaciones de campos aquí...

        nuevo_usuario = Usuario(**data)
        Usuario.agregar_usuario(nuevo_usuario)
        return {'message': 'Usuario creado exitosamente'}, 201

    @classmethod
    def login(cls):
        data = request.json
        email = data.get('email')
        contraseña = data.get('contraseña')
    
        # Crear una instancia de Usuario con valores en blanco o None para los campos no utilizados
        usuario = Usuario(
          id=None,
          nombre=None,
          apellido=None,
          email=email,
          contraseña=contraseña,
          fecha_nacimiento=None,
          avatar=None
        )
    
        if cls.authenticate(usuario):
          session['email'] = email
          print(session)
          return {"success":True,"message": "Sesión iniciada"}, 200
        else:
          return {"success":False,"message": "Correo electrónico o contraseña incorrectos"}, 401
    
    @classmethod
    def show_profile(cls):
        email = session.get('email')
        print(email)
        usuario = Usuario.obtener_usuario_por_email(email=email)
        if usuario:
            return jsonify(usuario), 200
        else:
            return jsonify({"success":False,"message": "Usuario no encontrado"}), 404
    
    @classmethod
    def update(cls):
      data = request.json
      email = session.get('email')

      # Obtener el usuario por su dirección de correo electrónico
      usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

      if usuario:
          try:
              # Actualizar los campos del usuario con los nuevos valores
              if 'nombre' in data:
                  usuario.nombre = data['nombre']
              if 'apellido' in data:
                  usuario.apellido = data['apellido']
              if 'fecha_nacimiento' in data:
                  usuario.fecha_nacimiento = data['fecha_nacimiento']
              if 'avatar' in data:
                  usuario.avatar = data['avatar']

              # Realizar la operación de actualización en la base de datos
              Usuario.actualizar_usuario(usuario)

              return jsonify(usuario.serializar()), 200
          except Exception as e:
              return jsonify({"message": str(e)}), 500
      else:
          return jsonify({"message": "Usuario no encontrado"}), 404

    
    
    @classmethod
    def logout(cls):
        session.pop('email', None)
        return {"message": "Sesión cerrada"}, 200

    @classmethod
    def authenticate(cls, usuario):
      # Aquí se implementa la autenticación del usuario utilizando los datos proporcionados
      # Se utiliza la función obtener_usuario_por_email para buscar el usuario por correo electrónico
      # y luego se verifica si la contraseña coincide con la proporcionada en los datos
      usuario_existente = Usuario.obtener_usuario_por_email(usuario.email) 
      if usuario_existente and usuario_existente['password'] == usuario.contraseña:
         return True
      return False
      
    @classmethod
    def get(cls, usuario_id):
        usuario = Usuario.obtener_usuario_por_id(usuario_id)
        if usuario:
            return usuario, 200
        else:
            raise UsuarioNotFound(usuario_id)

    @classmethod
    def get_all(cls):
        usuarios = Usuario.obtener_todos_los_usuarios()
        return usuarios, 200

    @classmethod
    def delete(cls, usuario_id):
        Usuario.eliminar_usuario_por_id(usuario_id)
        return {'message': 'Usuario eliminado exitosamente'}, 204

    @classmethod
    def email_exists(cls, email):
        # Verificar si el correo electrónico ya existe en la base de datos
        usuarios = Usuario.obtener_todos_los_usuarios()
        for usuario in usuarios:
            if usuario['email'] == email:
                return True
        return False
    
    @classmethod
    def obtener_servidores_usuario(cls):
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)
        print(usuario)
        if usuario:
            try:
                # Obtiene todos los servidores del usuario o de todos los servidores si no tiene ninguno
                servers = Servidor.obtener_servidores_por_usuario(usuario.id)
                print(servers)
                return jsonify([servidor.serializar() for servidor in servers]), 200
            except Exception as e:
                return jsonify({"success":False,"message": str(e)}), 500
        else:
            return jsonify({"success":False,"message": "Usuario no encontrado"}), 404

    @classmethod
    def crear_servidor(cls):
        data = request.json
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
                nuevo_servidor = Servidor.crear_servidor(
                    nombre=data.get('nombre'),
                    propietario_id=usuario.id,
                    icono_serv=data.get('icono_serv')
                )
                
                Servidor.agregar_miembro_al_servidor(nuevo_servidor.id_servidor, usuario.id)
                
                return jsonify(nuevo_servidor.serializar()), 201
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404

    @classmethod
    def eliminar_servidor(cls, servidor_id):
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email(email=email)

        if usuario:
            try:
                eliminado = Servidor.eliminar_servidor(servidor_id, usuario.id)
                if eliminado:
                    return jsonify({"message": "Servidor eliminado exitosamente"}), 200
                else:
                    return jsonify({"message": "El servidor no existe o no tienes permiso para eliminarlo"}), 404
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
        
    @classmethod
    def eliminar_relacion_servidor(cls, servidor_id):
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email(email=email)

        if usuario:
            try:
                eliminado = Servidor.eliminar_relacion_servidor(servidor_id, usuario.id)
                if eliminado:
                    return jsonify({"message": "Relación entre usuario y servidor eliminada exitosamente"}), 200
                else:
                    return jsonify({"message": "La relación no existe o no tienes permiso para eliminarla"}), 404
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
        

    @classmethod
    def unirse_a_servidor_existente(cls, servidor_id):
        print(servidor_id)
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
               # Verificar si el usuario ya es miembro del servidor
               if Servidor.es_miembro_del_servidor(servidor_id, usuario.id):
                    return jsonify({"message": "Ya eres miembro de este servidor"}), 400

               # Unirse al servidor existente
               Servidor.unirse_a_servidor(servidor_id, usuario.id)

               return jsonify({"message": "Te has unido al servidor exitosamente"}), 200
            except Exception as e:
                 return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404   

    @classmethod
    def obtener_todos_los_servidores(cls):
        try:
           servers = Servidor.obtener_todos_los_servidores()
           return jsonify([servidor.serializar() for servidor in servers]), 200
        except Exception as e:
          return jsonify({"message": str(e)}), 500

    @classmethod
    def buscar_servidores_por_nombre(cls):
        nombre = request.args.get('nombre')
        try:
           servidores = Servidor.buscar_servidores_por_nombre(nombre)
           return jsonify([servidor.serializar() for servidor in servidores]), 200
        except Exception as e:
           return jsonify({"message": str(e)}), 500


    @classmethod
    def obtener_canales_servidor(cls, servidor_id):
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
                # Obtiene todos los canales del servidor
                canales = Canal.obtener_canales_por_servidor(servidor_id)
                return jsonify([canal.serializar() for canal in canales]), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404

    @classmethod
    def crear_canal(cls, servidor_id):
        data = request.json
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
                nuevo_canal = Canal.crear_canal(
                    nombre=data.get('nombre'),
                    servidor_id=servidor_id,
                    creador_id=usuario.id,
                    icono=data.get('icono')
                )

               # Canal.unirse_a_canal(nuevo_canal.id_canal, usuario.id)

                return jsonify(nuevo_canal.serializar()), 201
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404

    """ 
    Para Aplicar este metodo debemos crear una tabla intermedia llamada usuarios_canales
    @classmethod
    def unirse_a_canal(cls, servidor_id, canal_id):
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
                # Verificar si el usuario ya es miembro del canal
                if Canal.verificar_pertenencia_a_canal(canal_id, usuario.id):
                    return jsonify({"message": "Ya eres miembro de este canal"}), 400

                # Unirse al canal existente
                Canal.unirse_a_canal(canal_id, usuario.id)

                return jsonify({"message": "Te has unido al canal exitosamente"}), 200
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404

    """

    @classmethod
    def obtener_mensajes_canal(cls, servidor_id, canal_id):
        try:
            # Implementa la lógica para obtener todos los mensajes de un canal
            mensajes = Mensaje.obtener_mensajes_por_canal(canal_id)
            return jsonify([mensaje.serializar() for mensaje in mensajes]), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 500

   
    @classmethod
    def obtener_mensajes_por_id(cls, servidor_id, canal_id, id_mensaje):
        try:
           # Implementa la lógica para obtener el contenido de un mensaje por su ID
           contenido_mensaje = Mensaje.obtener_mensaje_por_id_edit(id_mensaje)
           return jsonify({"contenido": contenido_mensaje}), 200
        except MensajeNotFound as e:
           return jsonify({"message": str(e)}), 404  # Mensaje no encontrado
        except Exception as e:
         return jsonify({"message": str(e)}), 500  # Otros errores internos del servidor
    
    
    
    @classmethod
    def enviar_mensaje(cls, servidor_id, canal_id):
        data = request.json
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
                nuevo_mensaje = Mensaje.crear_mensaje(
                    contenido=data.get('contenido'),
                    canal_id=canal_id,
                    usuario_id=usuario.id
                )

                return jsonify(nuevo_mensaje.serializar()), 201
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404

    @classmethod
    def borrar_mensaje(cls, servidor_id, canal_id, mensaje_id):
        email = session.get('email')
        usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

        if usuario:
            try:
                if Mensaje.borrar_mensaje(mensaje_id, usuario.id):
                    return jsonify({"message": "Mensaje eliminado exitosamente"}), 200
                else:
                    return jsonify({"message": "No tienes permiso para borrar este mensaje o ha pasado más de 1 minuto"}), 403
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
        

    @classmethod
    def modificar_mensaje(cls, servidor_id, canal_id, mensaje_id):
      email = session.get('email')
      usuario = Usuario.obtener_usuario_por_email_servidores(email=email)

      if usuario:
         try:
             # Obtén el nuevo contenido del mensaje desde la solicitud
             nuevo_contenido = request.json.get('contenido')

             if nuevo_contenido:
                # Intenta editar el mensaje
                if Mensaje.editar_mensaje(mensaje_id, nuevo_contenido):
                    return jsonify({"message": "Mensaje editado exitosamente"}), 200
                else:
                    return jsonify({"message": "Error al editar el mensaje"}), 500
             else:
                 return jsonify({"message": "Contenido del mensaje no proporcionado"}), 400
         except Exception as e:
             return jsonify({"message": str(e)}), 500
      else:
         return jsonify({"message": "Usuario no encontrado"}), 404