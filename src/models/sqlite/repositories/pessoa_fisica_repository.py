from src.interfaces.cliente_repository import ClienteRepository
from src.settings.connection import get_db_connection


class PessoaFisicaRepository(ClienteRepository):

    @staticmethod
    def sacar_dinheiro(cliente_id: int, valor: float) -> None:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT saldo FROM pessoa_fisica WHERE id = ?", (cliente_id,))
        saldo = cur.fetchone()[0]

        if saldo < valor:
            raise ValueError("Saldo insuficiente")

        cur.execute("UPDATE pessoa_fisica SET saldo = saldo - ? WHERE id = ?", (valor, cliente_id))
        conn.commit()
        conn.close()

    @staticmethod
    def realizar_extrato(cliente_id: int) -> dict:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pessoa_fisica WHERE id = ?", (cliente_id,))
        extrato = cur.fetchone()
        conn.close()
        return {
            "id": extrato[0],
            "renda_mensal": extrato[1],
            "idade": extrato[2],
            "nome_completo": extrato[3],
            "celular": extrato[4],
            "email": extrato[5],
            "categoria": extrato[6],
            "saldo": extrato[7]
        }
