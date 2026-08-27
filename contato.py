class Contato():
    def __init__(self, tipo, contato):
        self.__tipo = tipo
        self.__contato = contato

    def __str__(self):
        return f"Tipo de contato: {self.__tipo}, Contato: {self.__contato}"