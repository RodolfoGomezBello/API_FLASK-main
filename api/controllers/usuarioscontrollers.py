from ..models.usuariosmodels import Usuario #, agregar_usuario,obtener_usuario_por_email ,obtener_usuario_por_id, obtener_todos_los_usuarios, eliminar_usuario_por_id
from flask import request, session, jsonify
from ..models.exceptions import InvalidDataError, UsuarioNotFound
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
          return {"message": "Sesión iniciada"}, 200
        else:
          return {"message": "Correo electrónico o contraseña incorrectos"}, 401
    
    @classmethod
    def show_profile(cls):
        email = session.get('email')
        print(email)
        usuario = Usuario.obtener_usuario_por_email(email=email)
        if usuario:
            return jsonify(usuario), 200
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