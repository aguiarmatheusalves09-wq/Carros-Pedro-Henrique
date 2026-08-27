from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, modelo, marca, categoria):
        super().__init__(placa, modelo, marca)
        self.__categoria = categoria


    def __str__(self):
        return (f'Modelo: {self.__modelo}\nMarca: {self.__marca}\n'
            f'Placa: {self.__placa}\nAlugado: {self.__alugado}\nCilindrada: '
            f'Categoria: {self.__categoria}')
    
    def get_categoria(self):
        return self.__categoria

    def cadastrar_veiculo(self, placa, modelo, marca, categoria):
        return self.__carros.append(placa, modelo, marca)