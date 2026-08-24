from datetime import date
import datetime
from cliente import *

class aluguel(cliente):
    def __init__(self, data_devolucao:date, valor):
        self.__data_retirada = datetime
        self.__data_devolucao = data_devolucao
        self.__valor = valor

    def registrar_aluguel(self, cpf):
        cliente_encontrado = cliente.buscar_por_cpf(cpf)
        if cliente_encontrado is None:
            return False
        cliente_encontrado.adicionar_aluguel(self)
        return True

    def registrar_veiculo(self, cpf):
        return self.registrar_aluguel(cpf)

    
