class PessoaJuridicaView:
    def __init__(self, pessoa_juridica_controller):
        self.pessoa_juridica_controller = pessoa_juridica_controller

    def cadastrar_pessoa_juridica(self, request):
        try:
            # Obter os parâmetros do request
            faturamento = request.get('faturamento')
            idade = request.get('idade')
            nome_fantasia = request.get('nome_fantasia')
            celular = request.get('celular')
            email = request.get('email')
            categoria = request.get('categoria')
            saldo = request.get('saldo')

            # Chamar o método da controladora para cadastrar pessoa jurídica
            self.pessoa_juridica_controller.criar_pessoa_juridica(
                faturamento=faturamento,
                idade=idade,
                nome_fantasia=nome_fantasia,
                celular=celular,
                email=email,
                categoria=categoria,
                saldo=saldo
            )

            # Retornar uma mensagem de sucesso
            return "Pessoa jurídica cadastrada com sucesso."

        except Exception as e:
            # Lidar com exceção
            return str(e)

    def consultar_saldo(self, request):
        try:
            # Obter o nome da pessoa jurídica do request
            nome_pessoa_juridica = request.get('nome_pessoa_juridica')

            # Chamar o método da controladora para consultar saldo
            saldo = self.pessoa_juridica_controller.consultar_saldo(nome_pessoa_juridica)

            # Retornar o saldo
            return f"Saldo da pessoa jurídica {nome_pessoa_juridica}: {saldo}"

        except Exception as e:
            # Lidar com exceção
            return str(e)

    def sacar_dinheiro(self, request):
        try:
            # Obter os parâmetros do request
            quantia = request.get('quantia')
            nome_pessoa_juridica = request.get('nome_pessoa_juridica')

            # Chamar o método da controladora para sacar dinheiro
            mensagem = self.pessoa_juridica_controller.sacar_dinheiro(quantia, nome_pessoa_juridica)

            # Retornar a mensagem de saque
            return mensagem

        except Exception as e:
            # Lidar com exceção
            return str(e)

    def realizar_extrato(self, request):
        try:
            # Obter o nome da pessoa jurídica do request
            nome_pessoa_juridica = request.get('nome_pessoa_juridica')

            # Chamar o método da controladora para realizar extrato
            extrato = self.pessoa_juridica_controller.realizar_extrato(nome_pessoa_juridica)

            # Retornar o extrato
            return extrato

        except Exception as e:
            # Lidar com exceção
            return str(e)
