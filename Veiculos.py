class veiculo():
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano_fabricao = ano_fabricao
        self.__cor = cor 
        self.__tanque = tanque
        self.__tipo = tipo
        self.__alugado = False
        self.__lista = []

    def __str__(self):
        return print(f'Modelo: {self.__modelo} /nTipo: {self.__tipo}/nMarca: {self.__marca} /nPlaca: {self.__placa} /nAno: {self.__ano_fabricao} /nCor: {self.__cor} /nTanque: {self.__tanque} /nAlugado: {self.__alugado}')

    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque):
        return self.__lista.append(placa, modelo, marca, ano_fabricao, cor, tanque)

    def set_alugado(self):
        return self.__alugado == True

class carro(veiculo):
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, versao, tp_combustivel, quant_portas):
        super().__init__(placa, modelo, marca, ano_fabricao, cor, tanque, tipo)
        self.__versao = versao
        self.__tp_combustivel = tp_combustivel
        self.__quant_portas = quant_portas

    def __str__(self):
        return print(f'Modelo: {self.__modelo} /nTipo: {self.__tipo} /nVersão: {self.__versao} /nMarca: {self.__marca} /nPlaca: {self.__placa} /nAno: {self.__ano_fabricao} /nCor: {self.__cor} /nTanque: {self.__tanque} /nTipo de Combustivel: {self.__tp_combustivel} /nQuantidade de Portas: {self.__quant_portas} /nAlugado: {self.__alugado}')

    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel, tipo_carro, quant_portas):
        return self.__lista.append(placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel, tipo_carro, quant_portas)

class moto(veiculo):
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria):
        super().__init__(placa, modelo, marca, ano_fabricao, cor, tanque, tipo)
        self.__tipo_partida = tipo_partida
        self.__cilindrada = cilindrada
        self.__categoria = categoria


    def __str__(self):
            return print(f'Modelo: {self.__modelo} /nMarca: {self.__marca} /nPlaca: {self.__placa} /nAno: {self.__ano_fabricao} /nCor: {self.__cor} /nTanque: {self.__tanque} /nAlugado: {self.__alugado} /nCilindrada: {self.__cilindrada} /nTipo de partida: {self.__tipo_partida} /nCategoria: {self.__categoria}')

    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria):
        return self.__lista.append(placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria)
