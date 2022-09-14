from flask import Blueprint

from app.controllers.user_controller import index, save, show, update, delete

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)

user_bp.route('/create', methods=['POST'])(save)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)
