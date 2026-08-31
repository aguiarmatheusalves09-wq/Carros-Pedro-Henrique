from cliente import Cliente
from carro import Carro
from moto import Moto
import os 
from datetime import datetime

clientes = []
carros = [
    Carro("ABC-1234", "Onix", "Chevrolet", 4),
    Carro("DEF-5678", "HB20", "Hyundai", 4),
    Carro("GHI-9012", "Fiat Argo", "Fiat", 4),
    Carro("JKL-3456", "Corolla", "Toyota", 4),
    Carro("MNO-7890", "Civic", "Honda", 4),
    Carro("PQR-2345", "Ka", "Ford", 4),
    Carro("STU-6789", "T-Cross", "Volkswagen", 4),
    Carro("VWX-0123", "S10", "Chevrolet", 4),
]
motos = [
    Moto("ABC-1234", "NCR 170", "Honda", "Esportiva"),
    Moto("DEF-5678", "MT-07", "Yamaha", "Naked"),
    Moto("GHI-9012", "Scrambler 400", "Benelli", "Scrambler"),
    Moto("JKL-3456", "FZ 25", "Yamaha", "Esportiva"),
    Moto("MNO-7890", "XRE 300", "Honda", "Aventura"),
    Moto("PQR-2345", "CB 300R", "Honda", "Naked"),
    Moto("STU-6789", "Vulcan 250", "Yamaha", "Cruiser"),
]
  

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
    print("(5) Cancelar seguros")
    print("(6) Listar clientes")
    print("(7) Exibir veículos disponíveis")
    print("(8) Adicionar Veículo")
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

                if tipo_veiculo == "moto":
                    cliente.adicionar_aluguel(datetime.strptime(input("\nData de devolução (DD/MM/AAAA): ").strip(), "%d/%m/%Y").date(), tipo_veiculo, carros, motos)
                    limpar_tela()
                    print(f"Aluguel vinculado com sucesso ao cliente {cliente.get_nome()}!")

                elif tipo_veiculo == "carro":
                    cliente.adicionar_aluguel(datetime.strptime(input("\nData de devolução (DD/MM/AAAA): ").strip(), "%d/%m/%Y").date(), tipo_veiculo, carros, motos)
                    limpar_tela()
                    print(f"Aluguel vinculado com sucesso ao cliente {cliente.get_nome()}!")

                else:
                    limpar_tela()
                    print("Veículo inválido! Escolha Moto ou Carro.")

        case 3:
            cpf = input("Informe o CPF do cliente: ").strip()
            cliente = buscar_cliente(cpf)

            if cliente:
                cancela = cliente.cancelar_aluguel(cliente.get_aluguel)
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
            limpar_tela()
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                print("--- LISTA DE CLIENTES ---")
                for cliente in clientes:
                    print(cliente)
                    print("-" * 30)

        case 7:
            print("Seção de Carros")
            print("-" * 30)
            for carro in carros:
                print(carro)
                print("-" * 30)   
            print("Seção de Motos") 
            print("-" * 30)
            for moto in motos:
                print(moto)
                print("-" * 30) 

        case 8:
            veiculo = input("Qual veículo deseja adicionar (Moto/Carro): ").strip().lower()
            if veiculo == "moto":
                motos.append(Moto(placa=input("Placa: "), modelo=input("Modelo:"), marca=input("Marca: "), categoria=input("Categoria: ")))
                limpar_tela()
                print("Veículo cadastrado com sucesso!")
            elif veiculo == "carro":
                carros.append(Carro(placa=input("Placa: "), modelo=input("Modelo:"), marca=input("Marca: "), quant_portas=input("Quantidade de portas: ")))
                limpar_tela()
                print("Veículo cadastrado com sucesso!")
            else:
                limpar_tela()
                print("Veículo inválido! Escolha Moto ou Carro.")


        case 9:
            print("Saindo do sistema...")
            break

        case _:  
            limpar_tela()
            print("Opção inválida!")