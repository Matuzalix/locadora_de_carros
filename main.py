import os

carros = [
          ("Chevrolet Tracker", 120),
          ("Chevrolet Onix", 90),
          ("Hyundai HB20", 85),
          ("Hyundai Tucson", 120),
          ("Fiat Uno", 60),
          ("Fiat Mobi", 70),
          ("Fiat Pulse", 130)
          ]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, carros in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} / dia".format(i, carros[0], carros[1]))


mostrar_lista_de_carros(carros)

while True:
    os.system("cls")
    print("=" * 31)
    print("Bem vindos à locadora de carros")
    print("=" * 31)
    print("")
    print("O que você deseja fazer? ")
    print("0 - Mostrar Portifólio | 1 - Alugar um Carro | 2 - Devolver um Carro")
    menu = int(input("Digite aqui a opção desejada: "))

    os.system("cls")
    if menu == 0:
        mostrar_lista_de_carros(carros)

    elif menu == 1:
        mostrar_lista_de_carros(carros)
        print("=" * 31)
        cod_car = int(input("Escolha o Código do Carro: "))
        print("Por quantos dias você deseja alugar essse carro: ")
        dias = int(input())
        os.system("cls")

        print("Você escolheu {} por {} dias".format(carros[cod_car][0], dias))
        print("O valor do aluguel é de R$ {}, Deseja alugar? ".format(dias * carros[cod_car][1]))

        print("0 - Sim | 1 - Não ")
        confirmar = int(input())
        if confirmar == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

        elif confirmar == 1:
            os.system("cls")
            mostrar_lista_de_carros(carros)

        else:
            print("Escolha Inválida")

    elif menu == 2:
        if len(alugados) == 0:
            print("Não hà carros para devolver!")

        else:
            print("Segue lista de carros alugados, Qual você deseja devolver: ")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que você deseja devolver: ")
            cod = int(input())
            print("Você escolheu devolver o {}.".format(carros[cod_car][0]))
            print("0 - Sim | 1 - Não ")
            if cod == 0:
                print("Obrigado por devolver o carro {}.".format(alugados[cod_car][0]))
                carros.append(alugados.pop(cod_car))

            elif cod == 1:
                os.system("cls")
                mostrar_lista_de_carros(carros)

    print("")
    print("="*31)
    print("0 - Continuar | 1 - Sair")
    if int(input()) == 1:
        break
