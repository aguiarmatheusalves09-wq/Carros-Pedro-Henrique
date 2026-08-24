from datetime import date
import datetime
from atacadao.atacadao import Veiculos
from cliente import *
from Veiculos import *

class aluguel():
    def __init__(self, id, data_devolucao:date):
        self.__id = id
        self.__data_retirada = date.today
        self.__data_devolucao = data_devolucao
        self.__valor = float
        self.__aluguel = []

    def gerar_valor(self):
        tipo = Veiculos()
        diferenca = self.__data_devolucao - self.__data_retirada
        if tipo == "comun" or "COMUN":
            return self.__valor == diferenca * 250
        elif tipo == "Eco" or "eco":
            return self.__valor == diferenca * 500
        else:
            return self.__valor == diferenca * 800
    
    def registrar_aluguel(self, devolucao, valor):
        return self.__aluguel.append(self.__data_retirada, self.__data_devolucao, self.__valor)

    def cancelar_aluguel(self, id):
        for i in enumerate(self.__aluguel):
            if self.__aluguel == id:
                self.__aluguel.pop(i)
                return True

    