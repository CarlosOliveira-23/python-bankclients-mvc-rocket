from flask import Blueprint, request, jsonify
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository

pessoa_fisica_bp = Blueprint('pessoa_fisica', __name__)
repo = PessoaFisicaRepository()


@pessoa_fisica_bp.route('/pessoa_fisica/<int:cliente_id>/sacar', methods=['POST'])
def sacar(cliente_id):
    data = request.get_json()
    valor = data.get('valor')
    try:
        repo.sacar_dinheiro(cliente_id, valor)
        return jsonify({"message": "Saque realizado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@pessoa_fisica_bp.route('/pessoa_fisica/<int:cliente_id>/extrato', methods=['GET'])
def extrato(cliente_id):
    extrato = repo.realizar_extrato(cliente_id)
    return jsonify(extrato), 200
