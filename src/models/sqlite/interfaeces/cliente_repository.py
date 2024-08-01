from abc import ABC, abstractmethod


class Cliente(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia):
        pass

    @abstractmethod
    def realizar_extrato(self, pessoa):
        pass
