from datetime import date
import datetime
from cliente import *
from Veiculos import *

class Aluguel():
    def __init__(self, id, data_devolucao:date, tipo_veiculo):
        self.__id = id
        self.__data_retirada = date.today
        self.__tipo = tipo_veiculo
        self.__id = id
        self.__data_retirada = date.today
        self.__tipo = tipo
        self.__data_devolucao = data_devolucao
        self.__valor = float
        if tipo_veiculo == "moto":
            self.__veiculos = veiculo()
        elif tipo_veiculo == "carro":
            self.__veiculos = veiculo
        self.__aluguel = []

    def gerar_valor(self):
        diferenca = self.__data_devolucao - self.__data_retirada
        if self.__tipo == "comun" or "COMUN":
            return self.__valor == diferenca * 250
        elif self.__tipo == "Eco" or "eco":
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

class Seguro():
    def __init__(self, valor_seguro, tipo_seguro):
        self.__valor_seguro = valor_seguro
        self.__tipo_seguro = tipo_seguro

    def valor_seguro(self):
        