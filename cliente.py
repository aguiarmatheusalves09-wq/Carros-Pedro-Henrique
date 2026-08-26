from datetime import date


class Cliente:
    def __init__(self, nome, cpf, tipo, contato):
        self.__nome = nome
        self.__cpf = cpf  
        self.__contato = Contato(tipo, contato)
        self.__alugueis = []  

    def __str__(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | {self.__contato}"
    
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_alugueis(self):
        return self.__alugueis

    def adicionar_aluguel(self, aluguel):
        self.__alugueis.append(aluguel)

    def buscar_aluguel_por_id(self, id_aluguel):
        for aluguel in self.__alugueis:
            if str(aluguel.get_id()) == str(id_aluguel):
                return aluguel
        return None

    def cancelar_aluguel(self, id_aluguel):
        aluguel = self.buscar_aluguel_por_id(id_aluguel)
        if aluguel:
            self.__alugueis.remove(aluguel)
            return True
        return False

class Contato():
    def __init__(self, tipo, contato):
        self.__tipo = tipo
        self.__contato = contato

    def __str__(self):
        return f"Tipo de contato: {self.__tipo}, Contato: {self.__contato}"
    

    
