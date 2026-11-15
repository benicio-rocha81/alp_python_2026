
import random

nomes = []

while True:
    nome = input("Digite o nome do comprador (ou 'sair' para finalizar): ")

    if nome.lower() == "sair":
        break

    nomes.append(nome)

if len(nomes) > 0:
    ganhador = random.choice(nomes)

    print("\n=== RESULTADO DO SORTEIO ===")
    print("O ganhador foi:", ganhador)
else:
    print("Nenhum participante cadastrado!")

