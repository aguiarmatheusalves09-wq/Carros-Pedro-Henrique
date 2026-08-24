from veiculo import Veiculo
from carro import Carro
from moto import Moto
from aluguel import Aluguel
from seguro import Seguro 
from contato import Contato
from cliente import Cliente
import os 

while True:
    print("Bem vindo!")
    print("(1) Registrar aluguel")
    print("(2) Cancelar aluguel")
    print("(3) Cadastrar cliente")
    print("(4) Contratar seguro") 
    print("(5) Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            novo_aluguel = Aluguel(input("Data de devolução: "), float(input("Valor: ")), input("Placa: "), input("Modelo: "), input("Marca: "), input("Ano de fabricação: "), input("Cor"), input("Tanque"))
            novo_aluguel.registrar_aluguel(input("CPF: "))
            print("Aluguel realizado com sucesso!")

        case 2:
            aluguel.cancelar_aluguel(input("CPF: ")) 
            print("Aluguel cancelado!")

        case 3:
            novo_contato = Contato(input("Nome do cliente: "), input("CPF do cliente: "), input("Telefone: "))
            print("Cliente cadastrado com sucesso!")

        case 4:
            novo_seguro = Seguro(input("Tipo seguro"), input("Valor seguro: "))
            print("Seguro contratado com sucesso!")

        case 5:
            print("Saindo do sistema...")
            quit()
        case _:  
            print("Opção inválida!")


