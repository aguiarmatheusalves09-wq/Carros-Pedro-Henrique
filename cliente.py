from datetime import date
from aluguel import Aluguel
from contato import Contato


class Cliente:
    def __init__(self, nome, cpf, tipo, contato):
        self.__nome = nome
        self.__cpf = cpf  
        self.__contato = Contato(tipo, contato)
        self.__aluguel = None

    def __str__(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | {self.__contato} | Aluguel: {self.__aluguel}"
    
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_aluguel(self):
        return self.__aluguel

    def adicionar_aluguel(self, id, data_devolucao, tipo_veiculo):
        self.__aluguel = Aluguel(id, data_devolucao, tipo_veiculo)

    def cancelar_aluguel(self, id_aluguel):
        if aluguel:
            self.__aluguel = None
            return True
        return False
    

    
