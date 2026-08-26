from datetime import date
import datetime
from Veiculos import *

class Aluguel():
    def __init__(self, id, data_devolucao: date, valor: float, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, tipo_veiculo, cilindrada=None, tipo_partida=None, categoria=None):
        self.__id = id
        self.__data_retirada = date.today()
        self.__data_devolucao = data_devolucao
        self.__valor = float(valor)
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano_fabricacao = ano_fabricao
        self.__cor = cor
        self.__tanque = tanque
        self.__tipo = tipo
        self.__tipo_veiculo = tipo_veiculo
        self.__seguro = []

        if tipo_veiculo == "Moto":
            if cilindrada is None:
                    raise ValueError("Moto requer cilindrada.")
            self.__cilindrada = cilindrada
            self.__tipo_partida = tipo_partida
            self.__categoria = categoria

    def __str__(self):
        if self.__tipo_veiculo == "Carro":
            return f"ID: {self.__id}, Data de retirada: {self.__data_retirada}, Data de devolução: {self.__data_devolucao}, Valor: {self.__valor}, Placa: {self.__placa}, Modelo: {self.__modelo}, Marca:{self.__marca}, Ano de fabricação: {self.__ano_fabricacao}, Cor: {self.__cor}, Capacidade do tanque: {self.__tanque}, Tipo de carro{self.__tipo}"
        elif self.__tipo_veiculo == "Moto":
            return f"ID: {self.__id}, Data de retirada: {self.__data_retirada}, Data de devolução: {self.__data_devolucao}, Valor: {self.__valor}, Placa: {self.__placa}, Modelo: {self.__modelo}, Marca:{self.__marca}, Ano de fabricação: {self.__ano_fabricacao}, Cor: {self.__cor}, Capacidade do tanque: {self.__tanque}, Tipo de carro{self.__tipo}, Cilindradas: {self.__cilindrada}, Tipo de partida: {self.__tipo_partida}, Categoria: {self.__categoria}"

    def gerar_valor(self):
        tipo = self.__tipo.lower()
        diferenca = (self.__data_devolucao - self.__data_retirada).days
        if tipo in ("comum", "comum"):
            self.__valor = diferenca * 250
        elif tipo == "eco":
            self.__valor = diferenca * 500
        else:
            self.__valor = diferenca * 800
        return self.__valor

    def get_id(self):
        return self.__id

    def adicionar_seguro(self, tipo_seguro, valor_seguro):
        self.__seguro.append(Seguro(valor_seguro, tipo_seguro))
        print("Seguro adicionado!")

    def cancelar_seguro(self, tipo_seguro, valor_seguro):
        if Seguro(valor_seguro, tipo_seguro) not in self.__seguro:
            print("Esse seguro não está cadastrado!")
        else:
            self.__seguro.append(Seguro(valor_seguro, tipo_seguro))
        

class Seguro():
    def __init__(self, valor_seguro, tipo_seguro):
        self.__valor_seguro = valor_seguro
        self.__tipo_seguro = tipo_seguro

    