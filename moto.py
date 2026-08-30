from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, modelo, marca, categoria):
        super().__init__(placa, modelo, marca)
        self.__categoria = categoria

    def __str__(self):
        return (f'\nModelo: {self._modelo}'
                f'\nMarca: {self._marca}'
                f'\nPlaca: {self._placa}'
                f'\nAlugado: {self._alugado}'
                f'\nCategoria: {self.__categoria}')

    def get_categoria(self):
        return self.__categoria

    def cadastrar_veiculo(self, placa, modelo, marca):
        super().cadastrar_veiculo(placa, modelo, marca)   