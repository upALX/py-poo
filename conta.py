class Conta:
    def __init__(self, numero_conta, correntista, saldo, limite):
        self.__number_account = numero_conta
        self.__correntista_name = correntista
        self.__saldo = saldo
        self.__limit = limite

    def transferir(self, conta_destino, valor):
        self.__saldo -= valor
        conta_destino += valor

    def extrato(self):
        print('Olá, {}!'.format(self.__correntista_name))
        print('O limite da conta é {}!'.format(self.__limit))
        print('O valor em conta é {}!'.format(self.__saldo))

    def depositar_dinheiro(self, valor_deposito):
        self.__saldo += valor_deposito

    def sacar_dinheiro(self, valor_saque):
        self.__saldo -= valor_saque

    @property
    def account_number(self):
        return self.__number_account

    @property
    def mostrar_saldo(self):
        return self.__saldo

    @property
    def correntista_name(self):
        return self.correntista_name

    @correntista_name.setter
    def correntista_name(self, new_name):
        self.__correntista_name = new_name

    @property
    def limite(self):
        return self.__limit

    @limite.setter
    def limite(self, novo_limite):
        self.__limit = novo_limite
