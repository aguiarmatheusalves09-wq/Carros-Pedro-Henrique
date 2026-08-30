class Veiculo():
    def __init__(self, placa, modelo, marca):
        self._placa = placa
        self._modelo = modelo
        self._marca = marca
        self._alugado = False
        self._lista = []

    def __str__(self):
        return (f'\nModelo: {self._modelo} \nMarca: {self._marca}'
            f'\nPlaca: {self._placa}')

    def get_placa(self):
        return self._placa


    def cadastrar_veiculo(self, placa, modelo, marca):
        self._lista.append((placa, modelo, marca))

    def set_alugado(self):
        self._alugado = True






