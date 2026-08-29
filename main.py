from cliente import Cliente
import os 
from datetime import datetime

clientes = []
carros = []
motos =[]

def limpar_tela():
    os.system('cls')

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente.get_cpf().strip() == cpf.strip():
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
    print("(8) Exibir veículos disponíveis")
    print("(9) Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        limpar_tela()
        print("Por favor, digite um número válido!")
        continue

    match opcao:
        case 1:
            cpf = input("CPF do cliente: ").strip()
            if buscar_cliente(cpf):
                limpar_tela()
                print("Já existe um cliente cadastrado com este CPF!")
            else:
                novo_cliente = Cliente(
                    nome=input("Nome do cliente: ").strip(),
                    cpf=cpf,
                    tipo=input("Tipo de contato (email/telefone): ").strip(),
                    contato=input("Contato: ").strip()
                )
                clientes.append(novo_cliente)
                limpar_tela()
                print("Cliente cadastrado com sucesso!")

        case 2:
            cpf = input("Informe o CPF do cliente: ").strip()
            cliente = buscar_cliente(cpf)

            if not cliente:
                limpar_tela()
                print("Cliente não encontrado! Cadastre o cliente primeiro.")
            else:
                tipo_veiculo = input("Qual o tipo de veículo (Moto/Carro): ").strip().lower()
                novo_aluguel = None

                if tipo_veiculo == "moto" or tipo_veiculo == "carro":
                    cliente.adicionar_aluguel(id=input("ID do aluguel: ").strip(), data_devolucao=datetime.strptime(input("Data de devolução (DD/MM/AAAA): ").strip(), "%d/%m/%Y").date(), tipo_veiculo=tipo_veiculo)
                    limpar_tela()
                    print(f"Aluguel vinculado com sucesso ao cliente {cliente.get_nome()}!")
                else:
                    limpar_tela()
                    print("Veículo inválido! Escolha Moto ou Carro.")

        case 3:
            cpf = input("Informe o CPF do cliente: ").strip()
            cliente = buscar_cliente(cpf)

            if cliente:
                cancela = cliente.cancelar_aluguel(cliente.get_aluguel.get_id)
                if cancela:
                    limpar_tela()
                    print("Aluguel cancelado com sucesso!")
                else:
                    limpar_tela()
                    print("Aluguel não encontrado para este cliente!")
            else:
                limpar_tela()
                print("Cliente não encontrado!")

        case 4:
            cpf = input("Informe o CPF do cliente: ").strip()
            cliente = buscar_cliente(cpf)

            if cliente:
                aluguel = cliente.get_aluguel()

                if aluguel:
                    tipo_seguro = input("Qual tipo de seguro deseja: ").strip()
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
            cpf = input("Informe o CPF do cliente: ").strip()
            cliente = buscar_cliente(cpf)

            if cliente:
                aluguel = cliente.get_aluguel()

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
            cpf = input("Informe o CPF do cliente: ").strip()
            cliente = buscar_cliente(cpf)

            limpar_tela()
            if cliente:
                if not cliente.get_aluguel():
                    print(f"O cliente {cliente.get_nome()} não possui aluguéis registrados.")
                else:
                    print(f"--- ALUGUÉIS DO CLIENTE: {cliente.get_nome()} ---")
                    print(cliente.get_aluguel())
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
            print("Seção de Motos")

        case 9:
            print("Saindo do sistema...")
            break

        case _:  
            limpar_tela()
            print("Opção inválida!")