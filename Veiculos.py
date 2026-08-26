class Veiculo():
    def __init__(self, placa, modelo, marca):
        self._placa = placa
        self._modelo = modelo
        self._marca = marca
        self._alugado = False
        self._lista = []

    def __str__(self):

        return (f'Modelo: {self._modelo}\nMarca: {self._marca}\n'
            f'Placa: {self._placa}\nAlugado: {self._alugado}')


    def cadastrar_veiculo(self, placa, modelo, marca):
        self._lista.append((placa, modelo, marca))

    def set_alugado(self):
        self._alugado = True

class Carro(Veiculo):
    def __init__(self, placa, modelo, marca, quant_portas):
        super().__init__(placa, modelo, marca)
        self._quant_portas = quant_portas

    def __str__(self):
        return (f'Modelo: {self._modelo}\n'
            f'Marca: {self._marca}\nPlaca: {self._placa}\nQuantidade de Portas: {self._quant_portas}\n'
            f'Alugado: {self._alugado}')

    def cadastrar_veiculo(self, placa, modelo, marca):
        self._lista.append((placa, modelo, marca))

class Moto(Veiculo):
    def __init__(self, placa, modelo, marca, categoria):
        super().__init__(placa, modelo, marca)
        self.__categoria = categoria


    def __str__(self):
        return (f'Modelo: {self.__modelo}\nMarca: {self.__marca}\n'
            f'Placa: {self.__placa}\nAlugado: {self.__alugado}\nCilindrada: '
            f'Categoria: {self.__categoria}')

    def cadastrar_veiculo(self, placa, modelo, marca, categoria):
        return self.__carros.append(placa, modelo, marca)


