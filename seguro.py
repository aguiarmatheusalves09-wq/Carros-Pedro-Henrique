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