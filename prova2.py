import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=== LOGIN ===")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":
        print("Login realizado!")
        input("ENTER para continuar...")

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("=== MENU ===")
            print("1 - Gerenciar usuários")
            print("2 - Logout")
            print("3 - Encerrar")

            opcao = input("Escolha: ")

            if opcao == "1":
                print("Opção ainda não disponível.")
                input("ENTER para continuar...")

            elif opcao == "2":
                break

            elif opcao == "3":
                print("Programa encerrado!")
                exit()

            else:
                print("Opção inválida!")
                input("ENTER para continuar...")

    else:
        print("Usuário ou senha incorretos!")
        input("ENTER para tentar novamente...")
