from datetime import date
from carro import Carro
from moto import Moto
from seguro import Seguro

class Aluguel:
    def __init__(self, id, data_devolucao: date, tipo_veiculo):
        self.__id = str(id).strip()
        self.__data_retirada = date.today()
        self.__data_devolucao = data_devolucao
        self.__valor = None
        self.__tipo_veiculo = str(tipo_veiculo).strip()
        self.__veiculo = None
        self.__seguros = []  

        if self.__tipo_veiculo == "moto":
            self.__veiculo = Moto(placa=input("Placa: "), modelo=input("Modelo: "), marca=input("Marca: "), categoria=("Categoria: "))
        
        elif self.__tipo_veiculo == "carro":
            self.__veiculo = Carro(placa=input("Placa: "), modelo=input("Modelo: "), marca=input("Marca: "), quant_portas=("Quantidade de portas: "))

    def get_id(self):
        return self.__id

    def adicionar_seguro(self, tipo_seguro, valor_seguro):
        novo_seguro = Seguro(tipo_seguro, valor_seguro)
        self.__seguro.append(novo_seguro)

    def cancelar_seguro(self):
        if self.__seguro:
            self.__seguro.clear()  
            return True
        return False

    def gerar_valor(self):
        diferenca = (self.__data_devolucao - self.__data_retirada).days
        
        dias = max(diferenca, 1)

        if self.__tipo_veiculo == "moto":
            self.__valor = 250 * dias

        elif self.__tipo_veiculo == "carro":
            self.__valor = 500 * dias

        return self.__valor

    def __str__(self):
        texto_seguro = "Nenhum"
        if self.__seguro:
            texto_seguro = ", ".join([str(s) for s in self.__seguro])

        info_base = (
            f"ID: {self.__id} | Tipo: {self.__tipo_veiculo} | "
            f"Retirada: {self.__data_retirada.strftime('%d/%m/%Y')} | "
            f"Devolução: {self.__data_devolucao.strftime('%d/%m/%Y')} | "
            f"Valor: R$ {self.__valor:.2f} | Placa: {self.__placa} | "
            f"Modelo: {self.__modelo} | Marca: {self.__marca} | "
        )

        if self.__tipo_veiculo == "moto":
            info_base += f" | Categoria: {self.__veiculo.get_categoria} |"
        
        elif self.__tipo_veiculo == "carro":
            info_base += f" | Quantidade de portas: {self.__veiculo.get_quant_portas} |"

        info_base += f" | Seguro: [{texto_seguro} |"
        return info_base