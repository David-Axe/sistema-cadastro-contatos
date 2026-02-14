contatos = []

def mostrar_menu():
    print("\n=== SISTEMA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("0 - Sair")

def executar():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Adicionar contato")
        elif opcao == "2":
            print("Listar contatos")
        elif opcao == "3":
            print("Buscar contato")
        elif opcao == "4":
            print("Remover contato")
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

executar()