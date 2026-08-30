from datetime import date
from carro import Carro
from moto import Moto
from seguro import Seguro

class Aluguel:
    def __init__(self, data_devolucao: date, tipo_veiculo, lista_carros, lista_motos):
        self.__data_retirada = date.today()
        self.__data_devolucao = data_devolucao
        self.__valor = 0.0
        self.__tipo_veiculo = str(tipo_veiculo).strip().lower()
        self.__veiculo = None
        self.__seguros = []

        placa = input("Placa: ").strip().upper()

        if self.__tipo_veiculo == "moto":
            self.__veiculo = self._buscar(lista_motos, placa)
        elif self.__tipo_veiculo == "carro":
            self.__veiculo = self._buscar(lista_carros, placa)

        if self.__veiculo is None:
            raise ValueError(f"Veículo com placa {placa} não encontrado.")
        if self.__veiculo._alugado:
            raise ValueError(f"Veículo com placa {placa} já está alugado.")

        self.__veiculo.set_alugado()
        self.gerar_valor()

    def _buscar(self, lista, placa):
        for v in lista:
            if v.get_placa().strip().upper() == placa:
                return v
        return None

    def adicionar_seguro(self, tipo_seguro, valor_seguro):
        novo_seguro = Seguro(tipo_seguro, valor_seguro)
        self.__seguros.append(novo_seguro)

    def cancelar_seguro(self):
        if self.__seguros:
            self.__seguros.clear()
            return True
        return False

    def gerar_valor(self):
        diferenca = (self.__data_devolucao - self.__data_retirada).days
        dias = max(diferenca, 1)

        if self.__tipo_veiculo == "moto":
            self.__valor = 250.00 * dias
        elif self.__tipo_veiculo == "carro":
            self.__valor = 500.00 * dias

        return self.__valor

    def __str__(self):
        seguros_str = " ".join(str(i) for i in self.__seguros) if self.__seguros else "Sem seguros"
        return (f"\nTipo: {self.__tipo_veiculo}"
                f"\nRetirada: {self.__data_retirada.strftime('%d/%m/%Y')}"
                f"\nDevolução: {self.__data_devolucao.strftime('%d/%m/%Y')}"
                f"\nValor: R$ {self.__valor:.2f}"
                f"\n{self.__veiculo} "
                f"\n{seguros_str}")