from datetime import date
import datetime
from cliente import *
from Veiculos import *

class aluguel():
    def __init__(self, data_devolucao:date):
        self.__data_retirada = date.today
        self.__data_devolucao = data_devolucao
        self.__valor = float
        self.__alugueis = []

    def gerar_valor(self, tipo):
        diferenca = self.__data_devolucao - self.__data_retirada
        if tipo == "comun" or "COMUN":
            return self.__valor == diferenca * 250
        elif tipo == "Eco" or "eco":
            return self.__valor == diferenca * 500
        else:
            return self.__valor == diferenca * 800
    
    def registrar_aluguel(self, devolucao, valor):
        return self.__alugueis.append(self.__data_retirada, self.__data_devolucao, self.__valor)

    def cancelar_aluguel(self):
        