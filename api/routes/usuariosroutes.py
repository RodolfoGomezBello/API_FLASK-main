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
