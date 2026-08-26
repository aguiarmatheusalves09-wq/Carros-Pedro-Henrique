class Veiculo():
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo):
        self._placa = placa
        self._modelo = modelo
        self._marca = marca
        self._ano_fabricao = ano_fabricao
        self._cor = cor
        self._tanque = tanque
        self._tipo = tipo
        self._alugado = False
        self._lista = []

    def __str__(self):

        return (f'Modelo: {self._modelo}\nTipo: {self._tipo}\nMarca: {self._marca}\n'
            f'Placa: {self._placa}\nAno: {self._ano_fabricao}\nCor: {self._cor}\n'
            f'Tanque: {self._tanque}\nAlugado: {self._alugado}')


    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, *dados):
        self._lista.append((placa, modelo, marca, ano_fabricao, cor, tanque, *dados))

    def set_alugado(self):
        self._alugado = True

class Carro(Veiculo):
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, versao, tp_combustivel, quant_portas):
        super().__init__(placa, modelo, marca, ano_fabricao, cor, tanque, tipo)
        self._versao = versao
        self._tp_combustivel = tp_combustivel
        self._quant_portas = quant_portas

    def __str__(self):
        return (f'Modelo: {self._modelo}\nTipo: {self._tipo}\nVersão: {self._versao}\n'
            f'Marca: {self._marca}\nPlaca: {self._placa}\nAno: {self._ano_fabricao}\n'
            f'Cor: {self._cor}\nTanque: {self._tanque}\nTipo de Combustível: '
            f'{self._tp_combustivel}\nQuantidade de Portas: {self._quant_portas}\n'
            f'Alugado: {self._alugado}')

    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, *dados):
        self._lista.append((placa, modelo, marca, ano_fabricao, cor, tanque, *dados))

class Moto(Veiculo):
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria):
        super().__init__(placa, modelo, marca, ano_fabricao, cor, tanque, tipo)
        self._tipo_partida = tipo_partida
        self._cilindrada = cilindrada
        self._categoria = categoria
        self._carros = []


    def __str__(self):
            return (f'Modelo: {self._modelo}\nTipo: {self._tipo}\nMarca: {self._marca}\n'
                f'Placa: {self._placa}\nAno: {self._ano_fabricao}\nCor: {self._cor}\n'
                f'Tanque: {self._tanque}\nAlugado: {self._alugado}\nCilindrada: '
                f'{self._cilindrada}\nTipo de partida: {self._tipo_partida}\n'
                f'Categoria: {self._categoria}')

 #   def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, *dados):
#        self._lista.append((placa, modelo, marca, ano_fabricao, cor, tanque, *dados))
 #       self.__versao = versao
 #       self.__tp_combustivel = tp_combustivel
  #      self.__quant_portas = quant_portas
  #      self.__carros = []

    def __str__(self):
        return f'Modelo: {self.__modelo} /nTipo: {self.__tipo} /nVersão: {self.__versao} /nMarca: {self.__marca} /nPlaca: {self.__placa} /nAno: {self.__ano_fabricao} /nCor: {self.__cor} /nTanque: {self.__tanque} /nTipo de Combustivel: {self.__tp_combustivel} /nQuantidade de Portas: {self.__quant_portas} /nAlugado: {self.__alugado}'

    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel, tipo_carro, quant_portas):
        return self.__carros.append(placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel, tipo_carro, quant_portas)

    def lista(self):
        return self.__lista.append(self.__carros)
    
class moto(Veiculo):
    def __init__(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria):
        super().__init__(placa, modelo, marca, ano_fabricao, cor, tanque, tipo)
        self.__tipo_partida = tipo_partida
        self.__cilindrada = cilindrada
        self.__categoria = categoria
        self.__moto = []


    def __str__(self):
            return f'Modelo: {self.__modelo} /nMarca: {self.__marca} /nPlaca: {self.__placa} /nAno: {self.__ano_fabricao} /nCor: {self.__cor} /nTanque: {self.__tanque} /nAlugado: {self.__alugado} /nCilindrada: {self.__cilindrada} /nTipo de partida: {self.__tipo_partida} /nCategoria: {self.__categoria}'

    def cadastrar_veiculo(self, placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria):
        return self.__moto.append(placa, modelo, marca, ano_fabricao, cor, tanque, tipo, cilindrada, tipo_partida, categoria)

    def lista(self):
            return self.__lista.append(self.__moto)

