from aluguel import Aluguel
from datetime import date


class Cliente():
    def __init__(self, nome, cpf, tipo, contato):
        self.__nome = nome
        self.__cpf = cpf, 
        self.__contato = Contato(tipo, contato)

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Contato: {self.__contato}"

    def cadastrar(self, nome, cpf):
        return self.__clientes.append(nome, cpf)

    def remover(self, nome):
        for i in enumerate(self.__clientes):
            if self.__clientes == nome:
                self.__clientes.pop(i)
                return True

class Contato():
    def __init__(self, tipo, contato):
        self.__tipo = tipo
        self.__contato = contato

    def __str__(self):
        return f"Tipo: {self.__tipo}, Contato: {self.__contato}"
    

    
