from flask import Blueprint, request, jsonify
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository

pessoa_juridica_bp = Blueprint('pessoa_juridica', __name__)
repo = PessoaJuridicaRepository()


@pessoa_juridica_bp.route('/pessoa_juridica/<int:cliente_id>/sacar', methods=['POST'])
def sacar(cliente_id):
    data = request.get_json()
    valor = data.get('valor')
    try:
        repo.sacar_dinheiro(cliente_id, valor)
        return jsonify({"message": "Saque realizado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@pessoa_juridica_bp.route('/pessoa_juridica/<int:cliente_id>/extrato', methods=['GET'])
def extrato(cliente_id):
    extrato = repo.realizar_extrato(cliente_id)
    return jsonify(extrato), 200
