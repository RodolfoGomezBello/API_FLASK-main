from flask import Blueprint, request, jsonify
from ..controllers.usuarioscontrollers import UsuarioController

usuarios_routes = Blueprint('usuarios_routes', __name__)

usuarios_routes.route('/login', methods=['POST'])(UsuarioController.login)
usuarios_routes.route('/perfil', methods=['GET'])(UsuarioController.show_profile)
usuarios_routes.route('/logout', methods=['GET'])(UsuarioController.logout)
usuarios_routes.route('/usuarios', methods=['POST'])(UsuarioController.create)
usuarios_routes.route('/<int:usuario_id>', methods=['GET'])(UsuarioController.get)
usuarios_routes.route('/', methods=['GET'])(UsuarioController.get_all)
usuarios_routes.route('/usuarios/<int:usuario_id>', methods=['DELETE'])(UsuarioController.delete)
usuarios_routes.route('/servers', methods=['GET'])(UsuarioController.obtener_servidores_usuario)
usuarios_routes.route('/servers', methods=['POST'])(UsuarioController.crear_servidor)
usuarios_routes.route('/servers/<int:servidor_id>', methods=['DELETE'])(UsuarioController.eliminar_relacion_servidor)
usuarios_routes.route('/servers/all', methods=['GET'])(UsuarioController.obtener_todos_los_servidores)
usuarios_routes.route('/servers/join/<int:servidor_id>',methods=['POST'])(UsuarioController.unirse_a_servidor_existente)
usuarios_routes.route('/servers/<int:servidor_id>/canales', methods=['GET'])(UsuarioController.obtener_canales_servidor)
usuarios_routes.route('/servers/<int:servidor_id>/canales', methods=['POST'])(UsuarioController.crear_canal)
#usuarios_routes.route('/servers/<int:servidor_id>/canales/<int:canal_id>/unirse', methods=['POST'])(UsuarioController.unirse_a_canal) todos los canales estan habilitados para participar
usuarios_routes.route('/servers/<int:servidor_id>/canales/<int:canal_id>/mensajes', methods=['GET'])(UsuarioController.obtener_mensajes_canal)
usuarios_routes.route('/servers/<int:servidor_id>/canales/<int:canal_id>/mensajes', methods=['POST'])(UsuarioController.enviar_mensaje)
usuarios_routes.route('/servers/<int:servidor_id>/canales/<int:canal_id>/mensajes/<int:mensaje_id>', methods=['DELETE'])(UsuarioController.borrar_mensaje)

