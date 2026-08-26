from aluguel import Aluguel
from cliente import Cliente
import os 
from datetime import datetime

clientes = []

def limpar_tela():
    os.system('cls')

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

print("Bem-vindo ao Sistema de Locação!")

while True:
    print("\n(1) Cadastrar cliente")
    print("(2) Registrar aluguel para cliente")
    print("(3) Cancelar aluguel de cliente")
    print("(4) Contratar seguro") 
    print("(5) Cancelar seguro")
    print("(6) Listar aluguéis de um cliente")
    print("(7) Listar todos os clientes cadastrados")
    print("(8) Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            cpf = input("CPF do cliente: ")
            if buscar_cliente(cpf):
                limpar_tela()
                print("Já existe um cliente cadastrado com este CPF!")
            else:
                novo_cliente = Cliente(
                    nome=input("Nome do cliente: "),
                    cpf=cpf,
                    tipo=input("Tipo de contato (email/telefone): "),
                    contato=input("Contato: ")
                )
                clientes.append(novo_cliente)
                limpar_tela()
                print("Cliente cadastrado com sucesso!")

        case 2:
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf)

            if not cliente:
                limpar_tela()
                print("Cliente não encontrado! Cadastre o cliente primeiro.")
            else:
                tipo_veiculo = input("Qual o tipo de veículo (Moto/Carro): ").strip().capitalize()
                novo_aluguel = None

                if tipo_veiculo == "Moto":
                    novo_aluguel = Aluguel(
                        id=input("ID do aluguel: "),
                        data_devolucao=datetime.strptime(
                            input("Data de devolução (DD/MM/AAAA): "), "%d/%m/%Y"
                        ).date(),
                        valor=float(input("Valor: ")),
                        placa=input("Placa: "),
                        modelo=input("Modelo: "),
                        marca=input("Marca: "),
                        ano_fabricao=input("Ano de fabricação: "),
                        cor=input("Cor: "),
                        tanque=input("Tanque: "),
                        tipo=input("Tipo da moto: "),
                        tipo_veiculo="Moto",
                        cilindrada=input("Tipo de cilindrada: "),
                        tipo_partida=input("Tipo de partida: "),
                        categoria=input("Categoria da moto: ")
                    )
                elif tipo_veiculo == "Carro":
                    novo_aluguel = Aluguel(
                        id=input("ID do aluguel: "),
                        data_devolucao=datetime.strptime(
                            input("Data de devolução (DD/MM/AAAA): "), "%d/%m/%Y"
                        ).date(),
                        valor=float(input("Valor: ")),
                        placa=input("Placa: "),
                        modelo=input("Modelo: "),
                        marca=input("Marca: "),
                        ano_fabricao=input("Ano de fabricação: "),
                        cor=input("Cor: "),
                        tanque=input("Tanque: "),
                        tipo=input("Tipo de carro: "),
                        tipo_veiculo="Carro"
                    )
                else:
                    limpar_tela()
                    print("Veículo inválido! Escolha Moto ou Carro.")

                if novo_aluguel:
                    cliente.adicionar_aluguel(novo_aluguel)
                    limpar_tela()
                    print(f"Aluguel vinculado com sucesso ao cliente {cliente.nome}!")

        case 3:
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf)

            if cliente:
                id_busca = input("Informe o ID do aluguel a cancelar: ")
                if cliente.cancelar_aluguel(id_busca):
                    limpar_tela()
                    print("Aluguel cancelado com sucesso!")
                else:
                    limpar_tela()
                    print("Aluguel não encontrado para este cliente!")
            else:
                limpar_tela()
                print("Cliente não encontrado!")

        case 4:
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf)

            if cliente:
                id_busca = input("Informe o ID do aluguel: ")
                aluguel = cliente.buscar_aluguel_por_id(id_busca)

                if aluguel:
                    tipo_seguro = input("Qual tipo de seguro deseja: ")
                    valor_seguro = float(input("Qual o valor do seguro: "))
                    aluguel.adicionar_seguro(tipo_seguro, valor_seguro)
                    limpar_tela()
                    print("Seguro adicionado ao aluguel!")
                else:
                    limpar_tela()
                    print("Aluguel não encontrado para este cliente!")
            else:
                limpar_tela()
                print("Cliente não encontrado!")

        case 5:
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf)

            if cliente:
                id_busca = input("Informe o ID do aluguel: ")
                aluguel = cliente.buscar_aluguel_por_id(id_busca)

                if aluguel:
                    if aluguel.cancelar_seguro():
                        limpar_tela()
                        print("Seguro cancelado com sucesso!")
                    else:
                        limpar_tela()
                        print("Este aluguel não possui seguros registrados.")
                else:
                    limpar_tela()
                    print("Aluguel não encontrado para este cliente!")
            else:
                limpar_tela()
                print("Cliente não encontrado!")

        case 6:
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf)

            limpar_tela()
            if cliente:
                if not cliente.alugueis:
                    print(f"O cliente {cliente.nome} não possui aluguéis registrados.")
                else:
                    print(f"--- ALUGUÉIS DO CLIENTE: {cliente.nome} ---")
                    for aluguel in cliente.alugueis:
                        print(aluguel)
            else:
                print("Cliente não encontrado!")

        case 7:
            limpar_tela()
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                print("--- LISTA DE CLIENTES ---")
                for cliente in clientes:
                    print(cliente)
        
        case 8:
            print("Saindo do sistema...")
            break

        case _:  
            limpar_tela()
            print("Opção inválida!")