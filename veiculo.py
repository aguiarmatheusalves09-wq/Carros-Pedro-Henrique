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






