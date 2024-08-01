class PessoaFisicaView:
    def __init__(self, pessoa_fisica_controller):
        self.pessoa_fisica_controller = pessoa_fisica_controller

    def cadastrar_pessoa_fisica(self, request):
        try:
            # Obter os parâmetros do request
            renda_mensal = request.get('renda_mensal')
            idade = request.get('idade')
            celular = request.get('celular')
            email = request.get('email')
            categoria = request.get('categoria')
            saldo = request.get('saldo')

            # Chamar o método da controladora para cadastrar pessoa física
            self.pessoa_fisica_controller.criar_pessoa_fisica(
                renda_mensal=renda_mensal,
                idade=idade,
                celular=celular,
                email=email,
                categoria=categoria,
                saldo=saldo
            )

            # Retornar uma mensagem de sucesso
            return "Pessoa física cadastrada com sucesso."

        except Exception as e:
            # Lidar com exceção
            return str(e)

    def consultar_saldo(self, request):
        try:
            # Obter o nome da pessoa física do request
            nome_pessoa_fisica = request.get('nome_pessoa_fisica')

            # Chamar o método da controladora para consultar saldo
            saldo = self.pessoa_fisica_controller.consultar_saldo(nome_pessoa_fisica)

            # Retornar o saldo
            return f"Saldo da pessoa física {nome_pessoa_fisica}: {saldo}"

        except Exception as e:
            # Lidar com exceção
            return str(e)

    def sacar_dinheiro(self, request):
        try:
            # Obter os parâmetros do request
            quantia = request.get('quantia')
            nome_pessoa_fisica = request.get('nome_pessoa_fisica')

            # Chamar o método da controladora para sacar dinheiro
            mensagem = self.pessoa_fisica_controller.sacar_dinheiro(quantia, nome_pessoa_fisica)

            # Retornar a mensagem de saque
            return mensagem

        except Exception as e:
            # Lidar com exceção
            return str(e)

    def realizar_extrato(self, request):
        try:
            # Obter o nome da pessoa física do request
            nome_pessoa_fisica = request.get('nome_pessoa_fisica')

            # Chamar o método da controladora para realizar extrato
            extrato = self.pessoa_fisica_controller.realizar_extrato(nome_pessoa_fisica)

            # Retornar o extrato
            return extrato

        except Exception as e:
            # Lidar com exceção
            return str(e)
