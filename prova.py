import random
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("1 - 1 a 10")
    print("2 - 1 a 20")
    print("3 - 1 a 30")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        limite = 10
    elif nivel == 2:
        limite = 20
    elif nivel == 3:
        limite = 30
    else:
        print("Nível inválido!")
        input("ENTER para continuar...")
        continue

    numero = random.randint(1, limite)
    acertou = False

    for tentativa in range(3):
        palpite = int(input("Digite seu número: "))

        if palpite == numero:
            print("Parabéns, você acertou!")
            acertou = True
            break
        elif palpite < numero:
            print("Você errou!")
            print("Tente um número maior.")
        else:
            print("Você errou!")
            print("Tente um número menor.")

    if acertou == False:
        print("Você perdeu! Fim de jogo.")
        print("O número era:", numero)

    jogar = input("Jogar novamente? (s/n): ")

    if jogar.lower() != "s":
        break


# LOGIN

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
