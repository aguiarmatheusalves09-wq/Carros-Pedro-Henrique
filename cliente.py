from aluguel import Aluguel

class cliente():
    def __init__(self, nome, cpf, id, data_devolucao:date):
        self.__nome = nome
        self.__cpf = cpf
        self.__clientes = []
        self.__aluguel = Aluguel(id, data_devolucao)

    def cadastrar(self, nome, cpf):
        return self.__clientes.append(nome, cpf)
    
    def listar(self):
        if not self.__clientes:
            return "Não há clientes cadastrados."
        return "\n---\n".join(str(cliente) for cliente in self.__clientes)

    def remover(self, nome):
        for i in enumerate(self.__clientes):
            if self.__clientes == nome:
                self.__clientes.pop(i)
                return True
    

    
class contato():
    def __init__(self, tipo, contato):
        self.__tipo = tipo
        self.__contato = contato

    def __str__(self):
        return print(f"Tipo: {self.__tipo} /nContato")