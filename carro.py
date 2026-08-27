from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placa, modelo, marca, quant_portas):
        super().__init__(placa, modelo, marca)
        self._quant_portas = quant_portas

    def __str__(self):
        return (f'Modelo: {self._modelo}\n'
            f'Marca: {self._marca}\nPlaca: {self._placa}\nQuantidade de Portas: {self._quant_portas}\n'
            f'Alugado: {self._alugado}')

    def get_quant_portas(self):
        return self._quant_portas

    def cadastrar_veiculo(self, placa, modelo, marca):
        self._lista.append((placa, modelo, marca))