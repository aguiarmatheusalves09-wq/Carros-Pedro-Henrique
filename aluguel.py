from datetime import date
import datetime

class Seguro:
    def __init__(self, tipo_seguro, valor_seguro):
        self.__tipo_seguro = tipo_seguro
        self.__valor_seguro = float(valor_seguro)

    def tipo_seguro(self):
        return self.__tipo_seguro

    def valor_seguro(self):
        return self.__valor_seguro

    def __str__(self):
        return f"Seguro: {self.__tipo_seguro} (R$ {self.__valor_seguro:.2f})"


class Aluguel:
    def __init__(
        self,
        id,
        data_devolucao: date,
        valor: float,
        placa,
        modelo,
        marca,
        ano_fabricao,
        cor,
        tanque,
        tipo,
        tipo_veiculo,
        cilindrada=None,
        tipo_partida=None,
        categoria=None,
    ):
        self.__id = id
        self.__data_retirada = date.today()
        self.__data_devolucao = data_devolucao

        self.__valor = float(valor)
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano_fabricacao = ano_fabricao
        self.__cor = cor
        self.__tanque = tanque
        self.__tipo = tipo
        self.__tipo_veiculo = tipo_veiculo
        self.__seguro = []  

        if tipo_veiculo == "Moto":
            if cilindrada is None:
                raise ValueError("Moto requer cilindrada.")
            self.__cilindrada = cilindrada
            self.__tipo_partida = tipo_partida
            self.__categoria = categoria

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
        if tipo in ("comum", "standard"):
            self.__valor = diferenca * 250
        elif tipo == "eco":
            self.__valor = diferenca * 500
        else:
            self.__valor = diferenca * 800
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
            f"Tanque: {self.__tanque} | Categoria/Tipo: {self.__tipo}"
        )

        if self.__tipo_veiculo == "Moto":
            info_base += f" | Cilindradas: {self.__cilindrada} | Partida: {self.__tipo_partida} | Cat. Moto: {self.__categoria}"

        info_base += f" | Seguro: [{texto_seguro}]"
        return info_base