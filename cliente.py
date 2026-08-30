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
        return f"\nNome: {self.__nome} \nCPF: {self.__cpf} \n{self.__contato} \n{self.__aluguel}"
    
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_aluguel(self):
        return self.__aluguel

    def adicionar_aluguel(self, data_devolucao, tipo_veiculo, lista_carros, lista_motos):
        self.__aluguel = Aluguel(data_devolucao, tipo_veiculo, lista_carros, lista_motos)

    def cancelar_aluguel(self):
        if self.__aluguel:
            self.__aluguel = None
            return True
        return False
    

    
