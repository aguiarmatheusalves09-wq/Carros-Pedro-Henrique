import random
import string

class veiculo():
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano_fabricao = ano_fabricao
        self.__cor = cor 
        self.__tanque = tanque
        self.__lista = []

    def gerar_placa(self):
        letras = ''
        numeros = ''
        for i in 4:
            letras += random.choice(string.ascii_uppercase)
        for i in 3:
            numeros += random.choice('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        return self.__placa == f'{letras}--{numeros}'

    def gerar_id(self):
        id = ''
        id += '1'
        for i in 3:
            id += random('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        return self.__lista.append(id)
    

class carro(veiculo):
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel):
        super().__init__(placa, modelo, marca, ano_fabricao, cor, tanque)
        self.__versao = versao
        self.__tp_combustivel = tp_combustivel

    def gerar_placa(self):
        letras = ''
        numeros = ''
        for i in 4:
            letras += random.choice(string.ascii_uppercase)
        for i in 3:
            numeros += random.choice('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        return self.__placa == f'{letras}--{numeros}'

    def gerar_id(self):
        id = ''
        id += '1'
        for i in 3:
            id += random('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        return self.__lista.append(id)
