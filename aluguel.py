from datetime import date
from Veiculos import Carro, Moto

class Seguro:
    def __init__(self, tipo_seguro, valor_seguro):
        self.__tipo_seguro = str(tipo_seguro).strip()
        self.__valor_seguro = float(valor_seguro)

    def get_tipo_seguro(self):
        return self.__tipo_seguro

    def get_valor_seguro(self):
        return self.__valor_seguro

    def __str__(self):
        return f"Seguro: {self.__tipo_seguro} (R$ {self.__valor_seguro:.2f})"


class Aluguel:
    def __init__(self, id, data_devolucao: date, valor: float, tipo_veiculo):
        self.__id = str(id).strip()
        self.__data_retirada = date.today()
        self.__data_devolucao = data_devolucao
        self.__valor = float(valor)
        self.__tipo_veiculo = str(tipo_veiculo).strip()
        self.__seguro = []  

        if self.__tipo_veiculo == "moto":
            return Moto(placa=input("Placa: "), modelo=input("Modelo: "), marca=input("Marca: "), categoria=("Categoria: "))
        
        elif self.__tipo_veiculo == "carro":
            return Moto(placa=input("Placa: "), modelo=input("Modelo: "), marca=input("Marca: "), quant_portas=("Quantidade de portas: "))

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
        tipo = self.__tipo.lower()
        diferenca = (self.__data_devolucao - self.__data_retirada).days
        
        dias = max(diferenca, 1)

        if tipo in ("comum", "standard"):
            self.__valor = dias * 250.0
        elif tipo == "eco":
            self.__valor = dias * 500.0
        else:
            self.__valor = dias * 800.0
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
            f"Ano: {self.__ano_fabricacao} | Cor: {self.__cor} | "
            f"Categoria/Tipo: {self.__tipo}"
        )

        if self.__tipo_veiculo == "Moto":
            info_base += f" | Cilindradas: {self.__cilindrada} | Partida: {self.__tipo_partida} | Cat. Moto: {self.__categoria}"

        info_base += f" | Seguro: [{texto_seguro}]"
        return info_base