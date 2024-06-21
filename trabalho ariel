"""
Aplicação para gerenciamento de estacionamento.

Autor: Paulo Gabriel Noss
Data de Criação: 19/06/2024
"""

# Dicionário para armazenar os veículos estacionados
veiculos_estacionados = {}

# Adiciona um veículo padrão
veiculos_estacionados['ABC123'] = {
    'marca': 'vw',
    'modelo': 'saveiro',
    'cor': 'Prata',
    'proprietario': 'Paulo Gabriel Noss'
}

while True:
    # Exibe o menu
    print("\nMenu:")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # Estacionar veículo
        placa = input("Digite a placa do veículo: ").upper()  # Solicita a placa e converte para maiúsculas
        if placa in veiculos_estacionados:
            print("Erro: Veículo já está estacionado.")
        else:
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            cor = input("Digite a cor do veículo: ")
            proprietario = input("Digite o nome do proprietário: ")
            # Adiciona o veículo ao dicionário
            veiculos_estacionados[placa] = {
                'marca': marca,
                'modelo': modelo,
                'cor': cor,
                'proprietario': proprietario
            }
            print("Veículo estacionado com sucesso.")

    elif opcao == '2':
        # Retirar veículo
        placa = input("Digite a placa do veículo: ").upper()  # Solicita a placa e converte para maiúsculas
        if placa in veiculos_estacionados:
            # Remove o veículo do dicionário
            del veiculos_estacionados[placa]
            print("Veículo retirado com sucesso.")
        else:
            print("Erro: Veículo não encontrado.")

    elif opcao == '3':
        # Listar veículos estacionados
        if veiculos_estacionados:
            print("Veículos estacionados:")
            for placa, dados in veiculos_estacionados.items():
                # Exibe os detalhes do veículo
                print(f"{placa}: {dados['marca']} {dados['modelo']} ({dados['cor']}) - Proprietário: {dados['proprietario']}")
        else:
            print("Nenhum veículo estacionado.")

    elif opcao == '4':
        # Verificar se o veículo está estacionado
        placa = input("Digite a placa do veículo: ").upper()  # Solicita a placa e converte para maiúsculas
        if placa in veiculos_estacionados:
            dados = veiculos_estacionados[placa]
            # Exibe os detalhes do veículo
            print(f"Veículo encontrado: {dados['marca']} {dados['modelo']} ({dados['cor']}) - Proprietário: {dados['proprietario']}")
        else:
            print("Erro: Veículo não encontrado.")

    elif opcao == '0':
        # Sair do programa
        print("Saindo do programa.")
        break

    else:
        # Opção inválida
        print("Opção inválida. Tente novamente.")